# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 557)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ula = QLabel(self.centralwidget)
        self.ula.setObjectName(u"ula")
        self.ula.setGeometry(QRect(10, 10, 1061, 551))
        self.ula.setPixmap(QPixmap(u"ula.png"))
        self.xSpin = QSpinBox(self.centralwidget)
        self.xSpin.setObjectName(u"xSpin")
        self.xSpin.setGeometry(QRect(20, 172, 101, 22))
        self.xSpin.setMinimum(-32768)
        self.xSpin.setMaximum(32767)
        self.ySpin = QSpinBox(self.centralwidget)
        self.ySpin.setObjectName(u"ySpin")
        self.ySpin.setGeometry(QRect(20, 374, 101, 22))
        self.ySpin.setMinimum(-32768)
        self.ySpin.setMaximum(32767)
        self.zxSpin = QSpinBox(self.centralwidget)
        self.zxSpin.setObjectName(u"zxSpin")
        self.zxSpin.setGeometry(QRect(210, 70, 41, 22))
        self.zxSpin.setMaximum(1)
        self.nxSpin = QSpinBox(self.centralwidget)
        self.nxSpin.setObjectName(u"nxSpin")
        self.nxSpin.setGeometry(QRect(330, 70, 41, 22))
        self.nxSpin.setMaximum(1)
        self.zySpin = QSpinBox(self.centralwidget)
        self.zySpin.setObjectName(u"zySpin")
        self.zySpin.setGeometry(QRect(210, 480, 41, 22))
        self.zySpin.setMaximum(1)
        self.nySpin = QSpinBox(self.centralwidget)
        self.nySpin.setObjectName(u"nySpin")
        self.nySpin.setGeometry(QRect(330, 480, 41, 22))
        self.nySpin.setMaximum(1)
        self.fSpin = QSpinBox(self.centralwidget)
        self.fSpin.setObjectName(u"fSpin")
        self.fSpin.setGeometry(QRect(590, 150, 41, 22))
        self.fSpin.setMaximum(1)
        self.noSpin = QSpinBox(self.centralwidget)
        self.noSpin.setObjectName(u"noSpin")
        self.noSpin.setGeometry(QRect(690, 150, 41, 22))
        self.noSpin.setMaximum(1)
        self.zrLabel = QLabel(self.centralwidget)
        self.zrLabel.setObjectName(u"zrLabel")
        self.zrLabel.setGeometry(QRect(734, 480, 51, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.zrLabel.setFont(font)
        self.ngLabel = QLabel(self.centralwidget)
        self.ngLabel.setObjectName(u"ngLabel")
        self.ngLabel.setGeometry(QRect(820, 480, 51, 20))
        self.ngLabel.setFont(font)
        self.outLabel = QLabel(self.centralwidget)
        self.outLabel.setObjectName(u"outLabel")
        self.outLabel.setGeometry(QRect(930, 266, 51, 20))
        self.outLabel.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1026, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ula.setText("")
        self.zrLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ngLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.outLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

