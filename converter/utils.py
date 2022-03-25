
from dynaconf import Dynaconf
import logging


def get_settings():
    settings = Dynaconf(
        envvar_prefix="converter",
        settings_files=["settings.toml"],
        environments=True,
        load_dotenv=True,
    )
    return settings


def get_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
    return logging
