import json

from PySide6.QtCore import Slot

from app.unsplash import get_photo
from ui import Ui_MainWindow
from app.dialogs import SetAccessToken

from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_generate.clicked.connect(self.generate)
        self.ui.pushButton_setAccessToken.clicked.connect(self.set_access_token)

    @Slot()
    def generate(self):
        access_token = self.ui.label_accessTokenValue.text()
        url = self.ui.lineEdit_url.text()
        photo = get_photo(access_token, url)

        photo_obj = json.loads(photo)

        author = photo_obj["user"]["name"]
        author_link = photo_obj["user"]["links"]["html"]
        description = photo_obj["description"]
        image_url = photo_obj["links"]["html"]
        image_hotlink = photo_obj["urls"]["regular"]

        markdown = (
            f"<center>![]({image_hotlink})</center>\n\n<center><sub>{description}. "
            f"Photo by [{author}]({author_link}) on [Unsplash]({image_url}).</sub></center>\n"
        )

        self.ui.plainTextEdit_result.setPlainText(markdown)

    @Slot()
    def set_access_token(self):
        dialog = SetAccessToken()
        if dialog.exec():
            token: str = dialog.token
            if len(token) > 0:
                self.ui.label_accessTokenValue.setText(token)
            else:
                self.ui.label_accessTokenValue.setText("Not set")
