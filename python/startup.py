import sys

from PyQt5.QtWidgets import QApplication
import cuemol as cm
import cuemol_internal as ci
#from main import MainWindow, event
import main
from qmqtgui import QtMolWidget

from PyQt5.QtCore import QCoreApplication, Qt
#QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

def launchCueMol(confpath):
    ci.initCueMol(confpath)

    evm = main.event.getEventManager()

    logMgr = cm.svc("MsgLog")
    accumMsg = logMgr.getAccumMsg()
    logMgr.removeAccumMsg()

    # evm = event.getEventManager()

    app = QApplication(sys.argv)
    main_window = main.MainWindow()

    QtMolWidget.setupTextRender()
    QtMolWidget.setupEventTimer()

    widget = main.ConsoleWidget()
    widget.show()

    #main_window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':

    confpath = ""

    if len(sys.argv)>=2:
        confpath = sys.argv[1]

    launchCueMol(confpath)
    
