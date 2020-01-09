import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.loadTable()

    def loadTable(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM sorts""").fetchall()
        names = list(map(lambda x: x[0], con.execute('SELECT * FROM sorts').description))
        self.tableWidget.setColumnCount(len(names))
        self.tableWidget.setHorizontalHeaderLabels(names)
        for i, elem in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(elem[0])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(elem[1])))
            degre = cur.execute("""SELECT title FROM degrees_of_roasting WHERE id = ?""", (elem[2],)).fetchall()[0][0]
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(degre)))
            pom = cur.execute("""SELECT title FROM pomols WHERE id = ?""", (elem[3],)).fetchall()[0][0]
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(pom)))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(elem[4])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(elem[5])))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(elem[6])))
        self.tableWidget.resizeColumnsToContents()
        con.close()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())