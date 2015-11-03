import logging
import logging.config
import os
import yaml


DEFAULT_LOGGING_CONFIG = {
    "level": logging.DEBUG
}


def setup_logging(
        config_path="logging.yaml",
        config_path_env="LOG_CFG_PATH"
):
    """Setup the python logger

    Args:
        config_path (str): Path to a default config file
        config_path_env (str): Env variable to specify alternate logging config
    """
    config_override = os.getenv(config_path_env, None)
    config_path = config_path if not config_override else config_override

    if os.path.exists(config_path):
        with open(config_path, "rt") as yaml_file:
            config = yaml.load(yaml_file.read())

        logging.config.dictConfig(config)

    else:
        logging.warning("No logging config found at {path}, using "
                        "defaults".format(path=config_path))
        logging.basicConfig(**DEFAULT_LOGGING_CONFIG)


class LogProducer(object):
    """Simple class to add in class-oriented logging"""
    USE_MODULE_PATH = True

    def __init__(self, use_module_path=None, subname=None):
        if use_module_path is None:
            use_module_path = self.USE_MODULE_PATH

        if use_module_path:
            logger_name = ".".join([
                self.__class__.__module__,
                self.__class__.__name__
            ])

        else:
            logger_name = self.__class__.__name__

        if subname:
            logger_name += " ({})".format(subname)
        self._log = logging.getLogger(logger_name)
