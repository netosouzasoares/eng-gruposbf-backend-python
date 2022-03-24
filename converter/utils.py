
from dynaconf import Dynaconf


def get_settings():
    settings = Dynaconf(
        envvar_prefix="converter",
        settings_files=["settings.toml"],
        environments=True,
        load_dotenv=True,
    )
    return settings
