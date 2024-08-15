from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
from Excel import Ui_MainWindow
from GetProduct import Product
from CalculPrice import Calculate
from PyQt5 import QtCore, QtGui, QtWidgets
class MainWindow(QMainWindow,Product,Calculate):
    def __init__(self):
        super().__init__()
        self.qt = Ui_MainWindow()
        self.qt.setupUi(self)

        print(self.GetCategories())
        self.qt.comboBox.addItems(self.GetCategories())
        Currency_string = str(self.CalculateCurrency())
        self.qt.DolarKuruText.setText(Currency_string)

        label_logo = QtWidgets.QLabel(self.qt.centralwidget)
        label_logo.setPixmap(QtGui.QPixmap("Dbu.png"))
        label_logo.move(280,460)

        self.qt.pushButton.clicked.connect(self.UrunGetir)

        self.qt.DolarKuruText.setReadOnly(True)
    def UrunGetir(self):

        urun = self.qt.AramaYapacagnUrun.text()
        list = self.FindProduct(urun)
        row = (len(list)) / 3
        self.qt.tableWidget.setRowCount(row)
        self.qt.tableWidget.setColumnCount(3)

        r = 0
        for i in range(len(list)):
            print(i)
            if i % 3 == 0:
                self.qt.tableWidget.setItem(r, 0, QTableWidgetItem(str(list[i])))
            if i % 3 == 1:
                self.qt.tableWidget.setItem(r, 1, QTableWidgetItem(str(list[i])+"  $"))
            if i % 3 == 2:
                self.qt.tableWidget.setItem(r, 2, QTableWidgetItem(str(list[i])+"  tl"))
                r = r + 1

app = QApplication([])
window = MainWindow()
window.show()
app.exec()


