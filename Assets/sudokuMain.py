# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowSudokuMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 365)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.MainWindow_2 = QtWidgets.QWidget(MainWindow)
        self.MainWindow_2.setMinimumSize(QtCore.QSize(441, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MainWindow_2.setFont(font)
        self.MainWindow_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MainWindow_2.setObjectName("MainWindow_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lineEdit_06 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_06.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_06.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_06.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_06.setObjectName("lineEdit_06")
        
        self.gridLayout.addWidget(self.lineEdit_06, 1, 2, 1, 1)
        
        self.lineEdit_02 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_02.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_02.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_02.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_02.setObjectName("lineEdit_02")
        self.gridLayout.addWidget(self.lineEdit_02, 0, 1, 1, 1)
        self.lineEdit_01 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_01.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_01.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_01.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_01.setObjectName("lineEdit_01")
        self.gridLayout.addWidget(self.lineEdit_01, 0, 0, 1, 1)
        self.lineEdit_03 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_03.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_03.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_03.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_03.setObjectName("lineEdit_03")
        self.gridLayout.addWidget(self.lineEdit_03, 0, 2, 1, 1)
        self.lineEdit_05 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_05.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_05.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_05.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_05.setObjectName("lineEdit_05")
        self.gridLayout.addWidget(self.lineEdit_05, 1, 1, 1, 1)
        self.lineEdit_04 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_04.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_04.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_04.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_04.setObjectName("lineEdit_04")
        self.gridLayout.addWidget(self.lineEdit_04, 1, 0, 1, 1)
        self.lineEdit_07 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_07.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_07.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_07.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_07.setObjectName("lineEdit_07")
        self.gridLayout.addWidget(self.lineEdit_07, 2, 0, 1, 1)
        self.lineEdit_08 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_08.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_08.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_08.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_08.setObjectName("lineEdit_08")
        self.gridLayout.addWidget(self.lineEdit_08, 2, 1, 1, 1)
        self.lineEdit_09 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_09.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_09.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_09.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_09.setObjectName("lineEdit_09")
        self.gridLayout.addWidget(self.lineEdit_09, 2, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 100, 100))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_56 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_56.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_56.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_56.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.gridLayout_8.addWidget(self.lineEdit_56, 1, 2, 1, 1)
        self.lineEdit_57 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_57.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_57.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_57.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.gridLayout_8.addWidget(self.lineEdit_57, 0, 1, 1, 1)
        self.lineEdit_58 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_58.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_58.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_58.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.gridLayout_8.addWidget(self.lineEdit_58, 0, 0, 1, 1)
        self.lineEdit_59 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_59.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_59.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_59.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.gridLayout_8.addWidget(self.lineEdit_59, 0, 2, 1, 1)
        self.lineEdit_60 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_60.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_60.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_60.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.gridLayout_8.addWidget(self.lineEdit_60, 1, 1, 1, 1)
        self.lineEdit_61 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_61.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_61.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_61.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.gridLayout_8.addWidget(self.lineEdit_61, 1, 0, 1, 1)
        self.lineEdit_62 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_62.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_62.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_62.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.gridLayout_8.addWidget(self.lineEdit_62, 2, 0, 1, 1)
        self.lineEdit_63 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_63.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_63.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_63.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.gridLayout_8.addWidget(self.lineEdit_63, 2, 1, 1, 1)
        self.lineEdit_64 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_64.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_64.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_64.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.gridLayout_8.addWidget(self.lineEdit_64, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.MainWindow_2)
        self.label.setGeometry(QtCore.QRect(10, 110, 321, 16))
        self.label.setObjectName("label")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 250, 100, 100))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_9.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_9.setSpacing(10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lineEdit_65 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_65.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_65.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_65.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.gridLayout_9.addWidget(self.lineEdit_65, 1, 2, 1, 1)
        self.lineEdit_66 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_66.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_66.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_66.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.gridLayout_9.addWidget(self.lineEdit_66, 0, 1, 1, 1)
        self.lineEdit_67 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_67.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_67.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_67.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.gridLayout_9.addWidget(self.lineEdit_67, 0, 0, 1, 1)
        self.lineEdit_68 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_68.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_68.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_68.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.gridLayout_9.addWidget(self.lineEdit_68, 0, 2, 1, 1)
        self.lineEdit_69 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_69.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_69.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_69.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.gridLayout_9.addWidget(self.lineEdit_69, 1, 1, 1, 1)
        self.lineEdit_70 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_70.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_70.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_70.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.gridLayout_9.addWidget(self.lineEdit_70, 1, 0, 1, 1)
        self.lineEdit_71 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_71.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_71.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_71.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.gridLayout_9.addWidget(self.lineEdit_71, 2, 0, 1, 1)
        self.lineEdit_72 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_72.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_72.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_72.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.gridLayout_9.addWidget(self.lineEdit_72, 2, 1, 1, 1)
        self.lineEdit_73 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_73.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_73.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_73.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.gridLayout_9.addWidget(self.lineEdit_73, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.MainWindow_2)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 321, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.MainWindow_2)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 20, 341))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(120, 250, 100, 100))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_10.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_10.setSpacing(10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lineEdit_74 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_74.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_74.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_74.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.gridLayout_10.addWidget(self.lineEdit_74, 1, 2, 1, 1)
        self.lineEdit_75 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_75.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_75.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_75.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.gridLayout_10.addWidget(self.lineEdit_75, 0, 1, 1, 1)
        self.lineEdit_76 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_76.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_76.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_76.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.gridLayout_10.addWidget(self.lineEdit_76, 0, 0, 1, 1)
        self.lineEdit_77 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_77.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_77.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_77.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.gridLayout_10.addWidget(self.lineEdit_77, 0, 2, 1, 1)
        self.lineEdit_78 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_78.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_78.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_78.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.gridLayout_10.addWidget(self.lineEdit_78, 1, 1, 1, 1)
        self.lineEdit_79 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_79.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_79.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_79.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.gridLayout_10.addWidget(self.lineEdit_79, 1, 0, 1, 1)
        self.lineEdit_80 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_80.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_80.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_80.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.gridLayout_10.addWidget(self.lineEdit_80, 2, 0, 1, 1)
        self.lineEdit_81 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_81.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_81.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_81.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_81.setObjectName("lineEdit_81")
        self.gridLayout_10.addWidget(self.lineEdit_81, 2, 1, 1, 1)
        self.lineEdit_82 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_82.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_82.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_82.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_82.setObjectName("lineEdit_82")
        self.gridLayout_10.addWidget(self.lineEdit_82, 2, 2, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(120, 10, 100, 100))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_11.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_11.setSpacing(10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.lineEdit_83 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_83.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_83.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_83.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_83.setObjectName("lineEdit_83")
        self.gridLayout_11.addWidget(self.lineEdit_83, 1, 2, 1, 1)
        self.lineEdit_84 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_84.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_84.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_84.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_84.setObjectName("lineEdit_84")
        self.gridLayout_11.addWidget(self.lineEdit_84, 0, 1, 1, 1)
        self.lineEdit_85 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_85.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_85.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_85.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_85.setObjectName("lineEdit_85")
        self.gridLayout_11.addWidget(self.lineEdit_85, 0, 0, 1, 1)
        self.lineEdit_86 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_86.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_86.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_86.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_86.setObjectName("lineEdit_86")
        self.gridLayout_11.addWidget(self.lineEdit_86, 0, 2, 1, 1)
        self.lineEdit_87 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_87.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_87.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_87.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_87.setObjectName("lineEdit_87")
        self.gridLayout_11.addWidget(self.lineEdit_87, 1, 1, 1, 1)
        self.lineEdit_88 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_88.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_88.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_88.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_88.setObjectName("lineEdit_88")
        self.gridLayout_11.addWidget(self.lineEdit_88, 1, 0, 1, 1)
        self.lineEdit_89 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_89.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_89.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_89.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_89.setObjectName("lineEdit_89")
        self.gridLayout_11.addWidget(self.lineEdit_89, 2, 0, 1, 1)
        self.lineEdit_90 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_90.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_90.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_90.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_90.setObjectName("lineEdit_90")
        self.gridLayout_11.addWidget(self.lineEdit_90, 2, 1, 1, 1)
        self.lineEdit_91 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_91.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_91.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_91.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_91.setObjectName("lineEdit_91")
        self.gridLayout_11.addWidget(self.lineEdit_91, 2, 2, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(120, 130, 100, 100))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_12.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_12.setSpacing(10)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.lineEdit_92 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_92.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_92.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_92.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_92.setObjectName("lineEdit_92")
        self.gridLayout_12.addWidget(self.lineEdit_92, 1, 2, 1, 1)
        self.lineEdit_93 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_93.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_93.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_93.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_93.setObjectName("lineEdit_93")
        self.gridLayout_12.addWidget(self.lineEdit_93, 0, 1, 1, 1)
        self.lineEdit_94 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_94.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_94.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_94.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_94.setObjectName("lineEdit_94")
        self.gridLayout_12.addWidget(self.lineEdit_94, 0, 0, 1, 1)
        self.lineEdit_95 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_95.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_95.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_95.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_95.setObjectName("lineEdit_95")
        self.gridLayout_12.addWidget(self.lineEdit_95, 0, 2, 1, 1)
        self.lineEdit_96 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_96.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_96.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_96.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_96.setObjectName("lineEdit_96")
        self.gridLayout_12.addWidget(self.lineEdit_96, 1, 1, 1, 1)
        self.lineEdit_97 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_97.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_97.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_97.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_97.setObjectName("lineEdit_97")
        self.gridLayout_12.addWidget(self.lineEdit_97, 1, 0, 1, 1)
        self.lineEdit_98 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_98.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_98.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_98.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_98.setObjectName("lineEdit_98")
        self.gridLayout_12.addWidget(self.lineEdit_98, 2, 0, 1, 1)
        self.lineEdit_99 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_99.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_99.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_99.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_99.setObjectName("lineEdit_99")
        self.gridLayout_12.addWidget(self.lineEdit_99, 2, 1, 1, 1)
        self.lineEdit_100 = QtWidgets.QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_100.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_100.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_100.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_100.setObjectName("lineEdit_100")
        self.gridLayout_12.addWidget(self.lineEdit_100, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.MainWindow_2)
        self.label_4.setGeometry(QtCore.QRect(220, 10, 20, 341))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(230, 130, 100, 100))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_13.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_13.setSpacing(10)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lineEdit_101 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_101.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_101.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_101.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_101.setObjectName("lineEdit_101")
        self.gridLayout_13.addWidget(self.lineEdit_101, 1, 2, 1, 1)
        self.lineEdit_102 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_102.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_102.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_102.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_102.setObjectName("lineEdit_102")
        self.gridLayout_13.addWidget(self.lineEdit_102, 0, 1, 1, 1)
        self.lineEdit_103 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_103.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_103.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_103.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_103.setObjectName("lineEdit_103")
        self.gridLayout_13.addWidget(self.lineEdit_103, 0, 0, 1, 1)
        self.lineEdit_104 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_104.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_104.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_104.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_104.setObjectName("lineEdit_104")
        self.gridLayout_13.addWidget(self.lineEdit_104, 0, 2, 1, 1)
        self.lineEdit_105 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_105.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_105.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_105.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_105.setObjectName("lineEdit_105")
        self.gridLayout_13.addWidget(self.lineEdit_105, 1, 1, 1, 1)
        self.lineEdit_106 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_106.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_106.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_106.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_106.setObjectName("lineEdit_106")
        self.gridLayout_13.addWidget(self.lineEdit_106, 1, 0, 1, 1)
        self.lineEdit_107 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_107.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_107.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_107.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_107.setObjectName("lineEdit_107")
        self.gridLayout_13.addWidget(self.lineEdit_107, 2, 0, 1, 1)
        self.lineEdit_108 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_108.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_108.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_108.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_108.setObjectName("lineEdit_108")
        self.gridLayout_13.addWidget(self.lineEdit_108, 2, 1, 1, 1)
        self.lineEdit_109 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_109.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_109.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_109.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_109.setObjectName("lineEdit_109")
        self.gridLayout_13.addWidget(self.lineEdit_109, 2, 2, 1, 1)
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(230, 250, 100, 100))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_14.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_14.setSpacing(10)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.lineEdit_110 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_110.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_110.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_110.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_110.setObjectName("lineEdit_110")
        self.gridLayout_14.addWidget(self.lineEdit_110, 1, 2, 1, 1)
        self.lineEdit_111 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_111.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_111.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_111.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_111.setObjectName("lineEdit_111")
        self.gridLayout_14.addWidget(self.lineEdit_111, 0, 1, 1, 1)
        self.lineEdit_112 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_112.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_112.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_112.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_112.setObjectName("lineEdit_112")
        self.gridLayout_14.addWidget(self.lineEdit_112, 0, 0, 1, 1)
        self.lineEdit_113 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_113.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_113.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_113.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_113.setObjectName("lineEdit_113")
        self.gridLayout_14.addWidget(self.lineEdit_113, 0, 2, 1, 1)
        self.lineEdit_114 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_114.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_114.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_114.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_114.setObjectName("lineEdit_114")
        self.gridLayout_14.addWidget(self.lineEdit_114, 1, 1, 1, 1)
        self.lineEdit_115 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_115.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_115.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_115.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_115.setObjectName("lineEdit_115")
        self.gridLayout_14.addWidget(self.lineEdit_115, 1, 0, 1, 1)
        self.lineEdit_116 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_116.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_116.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_116.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_116.setObjectName("lineEdit_116")
        self.gridLayout_14.addWidget(self.lineEdit_116, 2, 0, 1, 1)
        self.lineEdit_117 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_117.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_117.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_117.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_117.setObjectName("lineEdit_117")
        self.gridLayout_14.addWidget(self.lineEdit_117, 2, 1, 1, 1)
        self.lineEdit_118 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_118.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_118.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_118.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_118.setObjectName("lineEdit_118")
        self.gridLayout_14.addWidget(self.lineEdit_118, 2, 2, 1, 1)
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.MainWindow_2)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(230, 10, 100, 100))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_15.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_15.setSpacing(10)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.lineEdit_119 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_119.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_119.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_119.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_119.setObjectName("lineEdit_119")
        self.gridLayout_15.addWidget(self.lineEdit_119, 1, 2, 1, 1)
        self.lineEdit_120 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_120.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_120.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_120.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_120.setObjectName("lineEdit_120")
        self.gridLayout_15.addWidget(self.lineEdit_120, 0, 1, 1, 1)
        self.lineEdit_121 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_121.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_121.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_121.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_121.setObjectName("lineEdit_121")
        self.gridLayout_15.addWidget(self.lineEdit_121, 0, 0, 1, 1)
        self.lineEdit_122 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_122.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_122.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_122.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_122.setObjectName("lineEdit_122")
        self.gridLayout_15.addWidget(self.lineEdit_122, 0, 2, 1, 1)
        self.lineEdit_123 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_123.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_123.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_123.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_123.setObjectName("lineEdit_123")
        self.gridLayout_15.addWidget(self.lineEdit_123, 1, 1, 1, 1)
        self.lineEdit_124 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_124.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_124.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_124.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_124.setObjectName("lineEdit_124")
        self.gridLayout_15.addWidget(self.lineEdit_124, 1, 0, 1, 1)
        self.lineEdit_125 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_125.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_125.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_125.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_125.setObjectName("lineEdit_125")
        self.gridLayout_15.addWidget(self.lineEdit_125, 2, 0, 1, 1)
        self.lineEdit_126 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_126.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_126.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_126.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_126.setObjectName("lineEdit_126")
        self.gridLayout_15.addWidget(self.lineEdit_126, 2, 1, 1, 1)
        self.lineEdit_127 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_127.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_127.setMaximumSize(QtCore.QSize(20, 20))
        self.lineEdit_127.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_127.setObjectName("lineEdit_127")
        self.gridLayout_15.addWidget(self.lineEdit_127, 2, 2, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.MainWindow_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 10, 91, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.checkbutton.setObjectName("checkbutton")
        self.verticalLayout.addWidget(self.checkbutton)
        self.savebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.savebutton.setObjectName("savebutton")
        self.verticalLayout.addWidget(self.savebutton)
        self.Load = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Load.setObjectName("Load")
        self.verticalLayout.addWidget(self.Load)
        self.Exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Exit.setObjectName("Exit")
        self.verticalLayout.addWidget(self.Exit)
        self.label_4.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.gridLayoutWidget_4.raise_()
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_3.raise_()
        self.gridLayoutWidget_4.raise_()
        self.gridLayoutWidget_5.raise_()
        self.gridLayoutWidget_6.raise_()
        self.gridLayoutWidget_7.raise_()
        self.gridLayoutWidget_8.raise_()
        self.gridLayoutWidget_9.raise_()
        self.verticalLayoutWidget.raise_()
        MainWindow.setCentralWidget(self.MainWindow_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku with Python"))
        self.label.setText(_translate("MainWindow", "----------------------------------------------------------------------"))
        self.label_2.setText(_translate("MainWindow", "----------------------------------------------------------------------"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p>|</p><p><br/></p></body></html>"))
        self.checkbutton.setText(_translate("MainWindow", "Check"))
        self.savebutton.setText(_translate("MainWindow", "Save"))
        self.Load.setText(_translate("MainWindow", "Load"))
        self.Exit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
