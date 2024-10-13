import json
from pathlib import Path

from app.config.models import Config


class ConfigProvider:
    __config: Config = Config()
    __config_path: str = "config.json"

    def init_config(self) -> None:
        if Path.is_file(Path(self.__config_path)):
            with open(self.__config_path, "r") as config_file:
                self.__config.__dict__ = json.load(config_file)
        else:
            with open(self.__config_path, "w") as config_file:
                json.dump(self.__config.__dict__, fp=config_file)

    def get_token(self) -> str:
        return self.__config.token

    def set_token(self, new_token) -> None:
        self.__config.token = new_token
        with open(self.__config_path, "w") as config_file:
            json.dump(self.__config.__dict__, fp=config_file)

    def get_template(self) -> str:
        return self.__config.template

    def set_template(self, new_template) -> None:
        self.__config.template = new_template
        with open(self.__config_path, "w") as config_file:
            json.dump(self.__config.__dict__, fp=config_file)
