import sys

from PyQt5.QtWidgets import QApplication
import cuemol_internal as cuemol
from main import MainWindow, event
from qmqtgui import QtMolWidget

from PyQt5.QtCore import QCoreApplication, Qt
#QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

confpath = ""

if len(sys.argv)>=2:
    confpath = sys.argv[1]

cuemol.initCueMol(confpath)
evm = event.getEventManager()

logMgr = cuemol.getService("MsgLog")
accumMsg = logMgr.getAccumMsg()
logMgr.removeAccumMsg()

# evm = event.getEventManager()

app = QApplication(sys.argv)
main_window = MainWindow()

QtMolWidget.setupTextRender()
QtMolWidget.setupEventTimer()

#main_window.show()
sys.exit(app.exec_())
