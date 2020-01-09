import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

NEW_LINE = []


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.d = Dialog_dop()
        self.loadTable()
        self.pushButton.clicked.connect(self.dialog)

    def dialog(self):
        self.d.show()

    def loadTable(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM sorts""").fetchall()
        names = list(map(lambda x: x[0], con.execute('SELECT * FROM sorts').description))
        self.tableWidget.setColumnCount(len(names))
        self.tableWidget.setHorizontalHeaderLabels(names)
        self.tableWidget.setRowCount(0)
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


class Dialog_dop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        name = self.lineEdit.text()
        stepen = self.comboBox.currentText()
        pomol = self.comboBox_2.currentText()
        description = self.plainTextEdit.toPlainText()
        price = self.spinBox_2.value()
        volume = self.spinBox.value()
        if name and stepen and pomol and price and volume:
            con = sqlite3.connect("coffee.db")
            cur = con.cursor()
            stepen = cur.execute("""SELECT id FROM degrees_of_roasting WHERE title = ?""", (stepen,)).fetchone()[0]
            pomol = cur.execute("""SELECT id FROM pomols WHERE title = ?""", (pomol,)).fetchone()[0]
            id = max(cur.execute("""SELECT id FROM sorts""").fetchall())[0] + 1
            cur.execute("""INSERT OR REPLACE INTO sorts VALUES(?, ?, ?, ?, ?, ?, ?)""",
                        (id, name, stepen, pomol, description, price, volume))
            con.commit()
            con.close()
            ex.loadTable()
            self.close()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())