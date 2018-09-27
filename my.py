# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 424)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/res/icon/a.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoRepeatInterval(98)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_2.addLayout(self.verticalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 23))
        self.menubar.setObjectName("menubar")
        self.menuOk = QtWidgets.QMenu(self.menubar)
        self.menuOk.setObjectName("menuOk")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOk.addAction(self.actionExit)
        self.menubar.addAction(self.menuOk.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.menubar.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.menuOk.setTitle(_translate("MainWindow", "ok"))
        self.actionExit.setText(_translate("MainWindow", "exit"))

import myres_rc
