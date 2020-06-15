# Author: Sharvin
# Title: Sudoku
# Description:
#       A simple sudoku game written in python.
#       Game will auto generate a sudoku game.
#       Check for duplicates in 3x3 grid, columns and rows.
#       A graphical user interface.
#       Have a save and resume option.
# Date Modified: 19:39 13/06/2020
# Version: 1.0

#
#
# Convert the .ui file from Qt Designer to .py file
#
# open cmd in the directory where the .ui file is and type in the command:
# pyuic5 -x nameOfFile.ui -o outputName.py
# Example: pyuic5 -x test.ui -o test.py
#
#


# import modules
from PyQt5 import QtWidgets
import sys

# creating a basic window.
def MainWindow():
    """This function creates an initialize the main window."""
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setGeometry(400, 200, 500, 500)
    window.setWindowTitle("Sharvin's Window")

    window.show()
    sys.exit(app.exec())


# call the MainWindow function to show the window.
MainWindow()

