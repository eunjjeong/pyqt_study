from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from chapter02.user_form import Userform

if __name__ == "__main__":
    # class 이용
    app = QApplication([])
    # w = MyApp()
    w = Userform()
    app.exec_()

    # UIC 이용
    # app = QApplication(sys.argv)
    # main_window = QMainWindow()
    # ui = hello_pyqt5.Ui_MainWindow()
    # ui.setupUi(main_window)
    # main_window.show()
    # sys.exit(app.exec_())