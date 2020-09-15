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
        MainWindow.resize(1150, 612)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ula = QLabel(self.centralwidget)
        self.ula.setObjectName(u"ula")
        self.ula.setGeometry(QRect(10, 10, 1150, 551))
        self.ula.setPixmap(QPixmap(u"ula.png"))
        self.zxSpin = QSpinBox(self.centralwidget)
        self.zxSpin.setObjectName(u"zxSpin")
        self.zxSpin.setGeometry(QRect(200, 50, 61, 41))
        self.zxSpin.setMaximum(1)
        self.nxSpin = QSpinBox(self.centralwidget)
        self.nxSpin.setObjectName(u"nxSpin")
        self.nxSpin.setGeometry(QRect(330, 51, 61, 41))
        self.nxSpin.setMaximum(1)
        self.zySpin = QSpinBox(self.centralwidget)
        self.zySpin.setObjectName(u"zySpin")
        self.zySpin.setGeometry(QRect(200, 480, 61, 41))
        self.zySpin.setMaximum(1)
        self.nySpin = QSpinBox(self.centralwidget)
        self.nySpin.setObjectName(u"nySpin")
        self.nySpin.setGeometry(QRect(330, 480, 61, 41))
        self.nySpin.setMaximum(1)
        self.fSpin = QSpinBox(self.centralwidget)
        self.fSpin.setObjectName(u"fSpin")
        self.fSpin.setGeometry(QRect(580, 140, 61, 41))
        self.fSpin.setMaximum(1)
        self.noSpin = QSpinBox(self.centralwidget)
        self.noSpin.setObjectName(u"noSpin")
        self.noSpin.setGeometry(QRect(690, 140, 61, 41))
        self.noSpin.setMaximum(1)
        self.zrLabel = QLabel(self.centralwidget)
        self.zrLabel.setObjectName(u"zrLabel")
        self.zrLabel.setGeometry(QRect(730, 480, 51, 20))
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
        self.outLabel.setGeometry(QRect(930, 259, 200, 31))
        self.outLabel.setFont(font)
        self.xEdit = QLineEdit(self.centralwidget)
        self.xEdit.setObjectName(u"xEdit")
        self.xEdit.setGeometry(QRect(10, 159, 111, 50))
        self.xEdit.setMaxLength(16)
        self.yEdit = QLineEdit(self.centralwidget)
        self.yEdit.setObjectName(u"yEdit")
        self.yEdit.setGeometry(QRect(10, 360, 111, 50))
        self.yEdit.setMaxLength(16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1069, 26))
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

