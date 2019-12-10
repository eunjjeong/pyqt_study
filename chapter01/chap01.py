from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("chapter01/chap01.ui")
        ok = self.ui.btn_ok.clicked.connect(self.showProp)
        self.ui.show()

    def showProp(self):
        print("red {} green {} blue {}",
              self.ui.spin_red.value(), self.ui.spin_green.value(), self.ui.spin_blue.value())

        self.ui.spin_red.setValue(128)
        self.ui.spin_green.setValue(128)
        self.ui.spin_blue.setValue(128)
        # print(dir(self.ui.spin_red))