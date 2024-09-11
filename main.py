import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from app import MainWindow


if __name__ == "__main__":
    application = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(application.exec())
