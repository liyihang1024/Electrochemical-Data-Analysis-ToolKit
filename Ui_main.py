# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainZwEJKW.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/images/images/images/DataPilot_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/\u6587\u4ef6\u5939-\u5f00_folder-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Open.setIcon(icon1)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/\u9000\u51fa_logout.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Exit.setIcon(icon2)
        self.action_CV = QAction(MainWindow)
        self.action_CV.setObjectName(u"action_CV")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/\u6b63\u5f26\u66f2\u7ebf_sinusoid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_CV.setIcon(icon3)
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/\u4fe1\u606f_info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_About.setIcon(icon4)
        self.action_LSV = QAction(MainWindow)
        self.action_LSV.setObjectName(u"action_LSV")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/\u66f2\u7ebf\u8c03\u6574_curve-adjustment.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_LSV.setIcon(icon5)
        self.action_Tafel = QAction(MainWindow)
        self.action_Tafel.setObjectName(u"action_Tafel")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/\u6298\u7ebf\u56fe_chart-line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Tafel.setIcon(icon6)
        self.action_Cdl = QAction(MainWindow)
        self.action_Cdl.setObjectName(u"action_Cdl")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/\u8111\u7535\u56fe_eeg.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Cdl.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout.addWidget(self.mdiArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Electrochemistry = QMenu(self.menubar)
        self.menu_Electrochemistry.setObjectName(u"menu_Electrochemistry")
        self.menu_About = QMenu(self.menubar)
        self.menu_About.setObjectName(u"menu_About")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Electrochemistry.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Electrochemistry.addAction(self.action_CV)
        self.menu_Electrochemistry.addAction(self.action_LSV)
        self.menu_Electrochemistry.addAction(self.action_Tafel)
        self.menu_Electrochemistry.addAction(self.action_Cdl)
        self.menu_About.addAction(self.action_About)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7535\u5316\u5b66\u6570\u636e\u53ef\u89c6\u5316\u5206\u6790\u767e\u5b9d\u7bb1", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.action_CV.setText(QCoreApplication.translate("MainWindow", u"CV", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_LSV.setText(QCoreApplication.translate("MainWindow", u"LSV", None))
        self.action_Tafel.setText(QCoreApplication.translate("MainWindow", u"Tafel", None))
        self.action_Cdl.setText(QCoreApplication.translate("MainWindow", u"Cdl", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_Electrochemistry.setTitle(QCoreApplication.translate("MainWindow", u"\u7535\u5316\u5b66\u6a21\u5757", None))
        self.menu_About.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

