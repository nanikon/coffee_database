import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setAnimated(False)
        mainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 761, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Каталог кофе"))
        self.pushButton.setText(_translate("mainWindow", "Добавить новую запись"))


class Ui_Dialog_dop(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(342, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 301, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(2000)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 350, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление"))
        self.label.setText(_translate("MainWindow", "Добавить новую запись в таблицу"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Степень обжарки"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Очень светлая"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Светлая"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Средняя"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Темная"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Очень темная"))
        self.label_4.setText(_translate("MainWindow", "Помол"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "в зёрнах"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "молотый"))
        self.label_5.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_6.setText(_translate("MainWindow", "Цена в рублях"))
        self.label_7.setText(_translate("MainWindow", "Объем в граммах"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))


class MyWidget(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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


class Dialog_dop(QMainWindow, Ui_Dialog_dop):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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