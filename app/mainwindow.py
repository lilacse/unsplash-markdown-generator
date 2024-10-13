import json
import re

from PySide6.QtCore import Slot

from app.config import ConfigProvider
from app.unsplash import get_photo
from ui import Ui_MainWindow
from app.dialogs import SetAccessToken

from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    __config_provider: ConfigProvider = ConfigProvider()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__config_provider.init_config()
        self.__set_access_token(self.__config_provider.get_token())
        self.__set_template(self.__config_provider.get_template())

        self.ui.pushButton_generate.clicked.connect(self.generate)
        self.ui.pushButton_setAccessToken.clicked.connect(self.configure_access_token)

    @Slot()
    def generate(self):
        access_token = self.ui.label_accessTokenValue.text()
        url = self.ui.lineEdit_url.text()
        photo = get_photo(access_token, url)

        photo_obj = json.loads(photo)

        template = self.ui.plainTextEdit_template.toPlainText()
        list_to_replace: list[str] = re.findall("{[a-zA-Z0-9_.]+}", template)

        self.__config_provider.set_template(template)

        for placeholder in list_to_replace:
            json_keys = placeholder.removeprefix('{').removesuffix('}').split('.')
            json_value = photo_obj
            for key in json_keys:
                json_value = json_value[key]

            if json_value is None:
                json_value = ""

            template = template.replace(placeholder, json_value)

        self.ui.plainTextEdit_result.setPlainText(template)

    @Slot()
    def configure_access_token(self):
        dialog = SetAccessToken()
        if dialog.exec():
            token: str = dialog.token
            self.__set_access_token(token)

    def __set_access_token(self, token):
        self.__config_provider.set_token(token)
        if len(token) > 0:
            self.ui.label_accessTokenValue.setText(token)
        else:
            self.ui.label_accessTokenValue.setText("Not set")

    def __set_template(self, template):
        if len(template) > 0:
            self.ui.plainTextEdit_template.setPlainText(template)
