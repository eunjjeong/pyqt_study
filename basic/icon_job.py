from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QToolTip, QMainWindow, QHBoxLayout, QVBoxLayout


class MyIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("img/web.png"))
        self.setGeometry(300, 300, 300, 200)

        # self.statusBar().showMessage('Ready', 3000) # 3초지나면 사라짐


        btn = QPushButton("Quit", self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        btn2 = QPushButton("StatusMessage", self)
        btn2.move(150, 50)
        btn2.resize(btn2.sizeHint())

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(btn2)
        hbox.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(QPushButton("test"))
        hbox2.addWidget(QPushButton("test2"))
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)


        # 풍선 도움말
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # 종료
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.clicked.connect(self.clearStatus)
        # btn2.clicked.connect(self.setStatusMsg)
        self.show()

    def setStatusMsg(self):
        self.statusBar().showMessage("Set Message") # 상태바

    def clearStatus(self):
        self.statusBar().clearMessage() #버튼을 누르면 상태바 삭제


if __name__ == "__main__":
    app = QApplication([])
    w = MyIcon()
    app.exec_()

