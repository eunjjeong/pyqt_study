from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QAbstractItemView, QHeaderView, QTableWidgetItem, QAction, \
    QMessageBox


class DepartUI(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dept_form.ui")
        self.ui.show()
        self.ui.tableWidget.setHorizontalHeaderLabels(["부서번호", "부서명", "위치"])
        # row 단위로 선택
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 수정불가능
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 균일한 간격으로 재배치
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # slot/signal
        self.ui.btn_add.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_del.clicked.connect(self.delete_item)
        self.ui.btn_init.clicked.connect(self.init_item)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.ui.tableWidget)

        data = [(1, "마케팅", 8), (2, "개발", 10), (3, "인사", 20)]
        self.load_data(data)

    def load_data(self, data):
        for idx, (no, name, floor) in enumerate(data):
            item_no, item_name, item_floor = self.create_item(floor, name, no)
            nextIdx = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(nextIdx)
            self.ui.tableWidget.setItem(nextIdx, 0, item_no)
            self.ui.tableWidget.setItem(nextIdx, 1, item_name)
            self.ui.tableWidget.setItem(nextIdx, 2, item_floor)


    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction("수정", tv)
        delete_action = QAction("삭제", tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)

        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    def __update(self):
        selectionIdx = self.ui.tableWidget.selectedIndexes()[0]
        no = self.ui.tableWidget.item(selectionIdx.row(), 0).text()
        name = self.ui.tableWidget.item(selectionIdx.row(), 1).text()
        floor = self.ui.tableWidget.item(selectionIdx.row(), 2).text()

        self.ui.le_no.setText(no)
        self.ui.le_name.setText(name)
        self.ui.le_floor.setText(floor)

        # QMessageBox.information(self, 'Update', '확인', QMessageBox.Ok)

    def __delete(self):
        selectionIdx = self.ui.tableWidget.selectedIndexes()[0]
        self.ui.tableWidget.removeRow(selectionIdx.row())

        # QMessageBox.information(self, 'Delete', '확인', QMessageBox.Ok)

    def add_item(self):
        item_no, item_name, item_floor = self.get_item_form_le()
        currentIdx = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(currentIdx)
        self.ui.tableWidget.setItem(currentIdx, 0, item_floor)
        self.ui.tableWidget.setItem(currentIdx, 1, item_name)
        self.ui.tableWidget.setItem(currentIdx, 2, item_no)

        # 초기화
        self.init_item()

    def get_item_form_le(self):
        no = self.ui.le_no.text()
        name = self.ui.le_name.text()
        floor = self.ui.le_floor.text()

        return self.create_item(floor, name, no)

    def create_item(self, floor, name, no):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignCenter)
        item_no.setData(Qt.DisplayRole, no)

        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)

        item_floor = QTableWidgetItem()
        item_floor.setTextAlignment(Qt.AlignCenter)
        item_floor.setData(Qt.DisplayRole, floor)

        return item_floor, item_name, item_no

    def update_item(self):
        selectionIdx = self.ui.tableWidget.selectedIndexes()[0]

        no = self.ui.le_no.text()
        name = self.ui.le_name.text()
        floor = self.ui.le_floor.text()

        self.ui.tableWidget.item(selectionIdx.row(), 0).setText(no)
        self.ui.tableWidget.item(selectionIdx.row(), 1).setText(name)
        self.ui.tableWidget.item(selectionIdx.row(), 2).setText(floor)


    def delete_item(self):
        selectionIdx = self.ui.tableWidget.selectedIndexes()[0]
        self.ui.tableWidget.removeRow(selectionIdx.row())

    def init_item(self):
        self.ui.le_no.clear()
        self.ui.le_name.clear()
        self.ui.le_floor.clear()


if __name__ == "__main__":
    app = QApplication([])
    w = DepartUI()
    app.exec_()