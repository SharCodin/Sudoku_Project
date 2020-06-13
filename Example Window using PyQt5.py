from PyQt5 import QtWidgets, uic
import sys


class MainWindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowMain, self).__init__()
        uic.loadUi('Assets\windowSudokuMain.ui',self)
        
        self.checkbutton.clicked.connect(self.onClick)
        self.Exit.clicked.connect(self.onClickExit)

    def onClick(self):
        print('onClick function was called.')
    
    def onClickExit(self):
        """Exit the app when the Exit button is clicked"""
        QtWidgets.QApplication.quit()

app = QtWidgets.QApplication([])
win = MainWindowMain()
win.show()
sys.exit(app.exec())