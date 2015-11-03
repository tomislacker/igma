import git.exc
import os
from git import Repo
from igma.util import LogProducer


class IGMA(LogProducer):
    PRODUCTION_PATH = "/etc/igma"
    """Path to production firewall repository"""

    def __init__(self, path=None, ipt_save="iptables-save"):
        LogProducer.__init__(self, use_module_path=False)

        if not path:
            path = self.PRODUCTION_PATH

        self._path = path
        self._ipt_save = ipt_save
        self.use_sudo = (os.getuid() != 0)

        self._log.debug("Using path: {path}".format(path=self._path))
        self._log.debug("iptables-save: {path}".format(path=self._ipt_save))

        if not os.path.exists(self._path):
            self._log.debug("Creating path")
            os.mkdir(self._path)

        try:
            self.repo = Repo(self._path)
        except git.exc.InvalidGitRepositoryError:
            self._log.debug("Initializing repo")
            self.repo = Repo.init(self._path)

    def dump(self, tables=None):
        if not tables:
            tables = ["filter", "mangle", "nat"]

        for table in tables:
            table_path = os.path.join(self._path, table)
            if not os.path.isdir(table_path):
                self._log.debug("Creating table dir: {path}".format(
                    path=table_path
                ))
                os.mkdir(table_path)


