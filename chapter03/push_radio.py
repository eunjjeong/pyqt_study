from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QHeaderView


class PushRadioUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("push_radio_btns.ui")
        self.ui.show()

        self.ui.btn_ok.clicked.connect(self.clickshow)
        self.ui.btn_cancel.clicked.connect(self.clickshow3)
        self.ui.rd_main.pressed.connect(self.clickshow2)
        self.ui.rd_fmain.pressed.connect(self.clickshow4)

        self.tbl_widget = self.ui.table_widget
        self.tbl_widget.setItem(0,0, QTableWidgetItem("cell(0,0)"))

        item = QTableWidgetItem("cell(0,1)")
        item.setTextAlignment(Qt.AlignCenter)
        self.tbl_widget.setItem(0,1, item)

        item1 = QTableWidgetItem("cell(0,2)")
        item1.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tbl_widget.setItem(0,2, item1)

        table_header = ["첫번째", "두번째", "세번째"]
        self.tbl_widget.setHorizontalHeaderLabels(table_header)

        # row 단위로 선택
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 수정불가능
        self.tbl_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 균일한 간격으로 재배치
        self.tbl_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 테이블 추가버튼
        self.ui.btn_input.clicked.connect(self.input_tble_item)

        # 테이블 삭제버튼
        self.ui.btn_del.clicked.connect(self.tbl_del_item)

    def tbl_del_item(self):
        selectionIdxs = self.tbl_widget.selectedIndexes()[0]
        print(selectionIdxs.row(), " ", selectionIdxs.column())
        self.tbl_widget.removeRow(selectionIdxs.row())


    def input_tble_item(self):
        item = QTableWidgetItem("cell(1,1)")
        item.setTextAlignment(Qt.AlignCenter)
        currentRowCount = self.tbl_widget.rowCount()
        # print(currentRowCount)
        self.tbl_widget.insertRow(currentRowCount)

        v1 = self.ui.le_01.text()
        v2 = self.ui.le_02.text()
        v3 = self.ui.le_03.text()

        item01 = QTableWidgetItem(v1)
        item01. setTextAlignment(Qt.AlignCenter)
        item02 = QTableWidgetItem(v2)
        item02.setTextAlignment(Qt.AlignCenter)
        item03 = QTableWidgetItem(v3)
        item03.setTextAlignment(Qt.AlignCenter)

        self.tbl_widget.setItem(currentRowCount, 0, item01)
        self.tbl_widget.setItem(currentRowCount, 1, item02)
        self.tbl_widget.setItem(currentRowCount, 2, item03)




    def clickshow(self):
        self.ui.lbl_push_res.setText(self.ui.btn_ok.text())

    def clickshow2(self):
        self.ui.lbl_rd_res.setText(self.ui.rd_main.text())

    def clickshow3(self):
        self.ui.lbl_push_res.setText(self.ui.btn_cancel.text())

    def clickshow4(self):
        self.ui.lbl_rd_res.setText(self.ui.rd_fmain.text())


if __name__ == "__main__":
    app = QApplication([])
    w = PushRadioUI()
    app.exec_()