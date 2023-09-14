# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1360, 618)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ula = QLabel(self.centralwidget)
        self.ula.setObjectName(u"ula")
        self.ula.setGeometry(QRect(190, 12, 1061, 551))
        self.ula.setPixmap(QPixmap(u"ula.png"))
        self.zxSpin = QSpinBox(self.centralwidget)
        self.zxSpin.setObjectName(u"zxSpin")
        self.zxSpin.setGeometry(QRect(380, 52, 61, 41))
        self.zxSpin.setMaximum(1)
        self.nxSpin = QSpinBox(self.centralwidget)
        self.nxSpin.setObjectName(u"nxSpin")
        self.nxSpin.setGeometry(QRect(510, 53, 61, 41))
        self.nxSpin.setMaximum(1)
        self.zySpin = QSpinBox(self.centralwidget)
        self.zySpin.setObjectName(u"zySpin")
        self.zySpin.setGeometry(QRect(380, 482, 61, 41))
        self.zySpin.setMaximum(1)
        self.nySpin = QSpinBox(self.centralwidget)
        self.nySpin.setObjectName(u"nySpin")
        self.nySpin.setGeometry(QRect(510, 482, 61, 41))
        self.nySpin.setMaximum(1)
        self.fSpin = QSpinBox(self.centralwidget)
        self.fSpin.setObjectName(u"fSpin")
        self.fSpin.setGeometry(QRect(760, 142, 61, 41))
        self.fSpin.setMaximum(1)
        self.noSpin = QSpinBox(self.centralwidget)
        self.noSpin.setObjectName(u"noSpin")
        self.noSpin.setGeometry(QRect(870, 142, 61, 41))
        self.noSpin.setMaximum(1)
        self.zrLabel = QLabel(self.centralwidget)
        self.zrLabel.setObjectName(u"zrLabel")
        self.zrLabel.setGeometry(QRect(910, 482, 51, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        # font.setWeight(75)
        self.zrLabel.setFont(font)
        self.ngLabel = QLabel(self.centralwidget)
        self.ngLabel.setObjectName(u"ngLabel")
        self.ngLabel.setGeometry(QRect(1000, 482, 51, 20))
        self.ngLabel.setFont(font)
        self.outLabel = QLabel(self.centralwidget)
        self.outLabel.setObjectName(u"outLabel")
        self.outLabel.setGeometry(QRect(1110, 261, 241, 31))
        self.outLabel.setFont(font)
        self.xEdit = QLineEdit(self.centralwidget)
        self.xEdit.setObjectName(u"xEdit")
        self.xEdit.setGeometry(QRect(40, 160, 261, 50))
        self.xEdit.setMaxLength(16)
        self.yEdit = QLineEdit(self.centralwidget)
        self.yEdit.setObjectName(u"yEdit")
        self.yEdit.setGeometry(QRect(40, 362, 261, 51))
        self.yEdit.setMaxLength(16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1360, 26))
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

