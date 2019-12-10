from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class Userform(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("chapter02/user_form.ui")
        self.ui.show()

if __name__ == "__main__":
    app = QApplication([])
    w = Userform()
    app.exec_()