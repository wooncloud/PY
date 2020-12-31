import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit
 
form_class = uic.loadUiType("bitcoinPriceCheckWindow.ui")[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
 
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)
 
    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        BTC = pykorbit.get_current_price("BTC")
        BCH = pykorbit.get_current_price("BCH")
        ETH = pykorbit.get_current_price("ETH")
        XRP = pykorbit.get_current_price("XRP")
        self.lineEdit.setText(str(BTC))
        self.lineEdit_2.setText(str(BCH))
        self.lineEdit_3.setText(str(ETH))
        self.lineEdit_4.setText(str(XRP))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()