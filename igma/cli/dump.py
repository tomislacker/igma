"""

Dumps out the IPTables configuration using iptables-dump

Usage:
    igma-dump --local
    igma-dump --path PATH
    igma-dump
    igma-dump [--help] [--version]

Options:
    -l, --local             Dump to the current working directory
    -P, --path PATH         Explicit path to dump to
    -h, --help              View this dialog
    -V, --version           View the version number
    -I, --ipt-save PATH     Path to 'iptables-save' application
"""
import logging
import sys
from igma import __version__
from igma.igma import IGMA
from igma.util import setup_logging

setup_logging()
CLI_NAME = "igma-dump"


def main(args=None):
    if args is None:
        args = sys.argv[1::]

    import os
    from docopt import docopt
    args = docopt(__doc__, argv=args, version=__version__)

    path = None
    if args['--path']:
        path = args['--path']
    elif args['--local']:
        path = os.getcwd()

    logger = logging.getLogger(CLI_NAME)
    try:
        mgr = IGMA(path)
        mgr.dump()

    except PermissionError as e:
        logger.critical(e)
        sys.exit(253)

    except Exception as e:
        logger.critical("Fatal: {eclass}".format(
            eclass=".".join([
                e.__class__.__module__,
                e.__class__.__name__
            ])), exc_info=True)
        sys.exit(254)


if __name__ == '__main__':
    main(sys.argv[1::])
