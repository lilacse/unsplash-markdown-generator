from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog

from ui.dialogs import Ui_dialog_setAccessToken


class SetAccessToken(QDialog):
    token: str = ""

    def __init__(self):
        super(SetAccessToken, self).__init__()
        self.ui = Ui_dialog_setAccessToken()
        self.ui.setupUi(self)

        self.ui.lineEdit_accessToken.setText(self.token)
        self.ui.buttonBox.accepted.connect(self.set_token)
        self.ui.buttonBox.rejected.connect(self.cancel)

    @Slot()
    def set_token(self):
        self.token = self.ui.lineEdit_accessToken.text()
        self.accept()

    @Slot()
    def cancel(self):
        self.reject()
