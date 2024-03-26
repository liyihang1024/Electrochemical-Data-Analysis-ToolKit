# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FunctionWindowPhkyWc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(623, 697)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 586, 712))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_electrode_area = QLabel(self.frame)
        self.label_electrode_area.setObjectName(u"label_electrode_area")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_electrode_area.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_electrode_area)

        self.lineEdit_electrode_area = QLineEdit(self.frame)
        self.lineEdit_electrode_area.setObjectName(u"lineEdit_electrode_area")

        self.horizontalLayout_8.addWidget(self.lineEdit_electrode_area)

        self.label_electrode_area_unit = QLabel(self.frame)
        self.label_electrode_area_unit.setObjectName(u"label_electrode_area_unit")

        self.horizontalLayout_8.addWidget(self.label_electrode_area_unit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_potential_shift = QLabel(self.frame)
        self.label_potential_shift.setObjectName(u"label_potential_shift")
        self.label_potential_shift.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_potential_shift)

        self.lineEdit_potential_shift = QLineEdit(self.frame)
        self.lineEdit_potential_shift.setObjectName(u"lineEdit_potential_shift")

        self.horizontalLayout_8.addWidget(self.lineEdit_potential_shift)

        self.label_potential_shift_unit = QLabel(self.frame)
        self.label_potential_shift_unit.setObjectName(u"label_potential_shift_unit")

        self.horizontalLayout_8.addWidget(self.label_potential_shift_unit)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_CV = QFrame(self.scrollAreaWidgetContents)
        self.frame_CV.setObjectName(u"frame_CV")
        self.frame_CV.setStyleSheet(u"")
        self.frame_CV.setFrameShape(QFrame.StyledPanel)
        self.frame_CV.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_CV)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_CV = QLabel(self.frame_CV)
        self.label_CV.setObjectName(u"label_CV")
        self.label_CV.setFont(font)

        self.verticalLayout.addWidget(self.label_CV)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.plainTextEdit_CV_Data = QPlainTextEdit(self.frame_CV)
        self.plainTextEdit_CV_Data.setObjectName(u"plainTextEdit_CV_Data")
        self.plainTextEdit_CV_Data.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_CV_Data.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_CV_Data.setSizePolicy(sizePolicy)
        self.plainTextEdit_CV_Data.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.plainTextEdit_CV_Data)

        self.plainTextEdit_CV_Label = QPlainTextEdit(self.frame_CV)
        self.plainTextEdit_CV_Label.setObjectName(u"plainTextEdit_CV_Label")

        self.horizontalLayout_5.addWidget(self.plainTextEdit_CV_Label)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_addData_CV = QPushButton(self.frame_CV)
        self.btn_addData_CV.setObjectName(u"btn_addData_CV")

        self.horizontalLayout.addWidget(self.btn_addData_CV)

        self.btn_importData_CV = QPushButton(self.frame_CV)
        self.btn_importData_CV.setObjectName(u"btn_importData_CV")

        self.horizontalLayout.addWidget(self.btn_importData_CV)

        self.btn_Plot_CV = QPushButton(self.frame_CV)
        self.btn_Plot_CV.setObjectName(u"btn_Plot_CV")

        self.horizontalLayout.addWidget(self.btn_Plot_CV)

        self.btn_saveData_CV = QPushButton(self.frame_CV)
        self.btn_saveData_CV.setObjectName(u"btn_saveData_CV")

        self.horizontalLayout.addWidget(self.btn_saveData_CV)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.frame_CV)

        self.frame_LSV = QFrame(self.scrollAreaWidgetContents)
        self.frame_LSV.setObjectName(u"frame_LSV")
        self.frame_LSV.setFrameShape(QFrame.StyledPanel)
        self.frame_LSV.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_LSV)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_LSV = QLabel(self.frame_LSV)
        self.label_LSV.setObjectName(u"label_LSV")
        self.label_LSV.setFont(font)

        self.verticalLayout_2.addWidget(self.label_LSV)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.plainTextEdit_LSV_Data = QPlainTextEdit(self.frame_LSV)
        self.plainTextEdit_LSV_Data.setObjectName(u"plainTextEdit_LSV_Data")

        self.horizontalLayout_9.addWidget(self.plainTextEdit_LSV_Data)

        self.plainTextEdit_LSV_Label = QPlainTextEdit(self.frame_LSV)
        self.plainTextEdit_LSV_Label.setObjectName(u"plainTextEdit_LSV_Label")

        self.horizontalLayout_9.addWidget(self.plainTextEdit_LSV_Label)

        self.horizontalLayout_9.setStretch(0, 4)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_addData_LSV = QPushButton(self.frame_LSV)
        self.btn_addData_LSV.setObjectName(u"btn_addData_LSV")

        self.horizontalLayout_2.addWidget(self.btn_addData_LSV)

        self.btn_importData_LSV = QPushButton(self.frame_LSV)
        self.btn_importData_LSV.setObjectName(u"btn_importData_LSV")

        self.horizontalLayout_2.addWidget(self.btn_importData_LSV)

        self.btn_Plot_LSV = QPushButton(self.frame_LSV)
        self.btn_Plot_LSV.setObjectName(u"btn_Plot_LSV")

        self.horizontalLayout_2.addWidget(self.btn_Plot_LSV)

        self.btn_saveData_LSV = QPushButton(self.frame_LSV)
        self.btn_saveData_LSV.setObjectName(u"btn_saveData_LSV")

        self.horizontalLayout_2.addWidget(self.btn_saveData_LSV)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.frame_LSV)

        self.frame_Cdl = QFrame(self.scrollAreaWidgetContents)
        self.frame_Cdl.setObjectName(u"frame_Cdl")
        self.frame_Cdl.setFrameShape(QFrame.StyledPanel)
        self.frame_Cdl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_Cdl)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_Cdl = QLabel(self.frame_Cdl)
        self.label_Cdl.setObjectName(u"label_Cdl")
        self.label_Cdl.setFont(font)

        self.verticalLayout_3.addWidget(self.label_Cdl)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.plainTextEdit_Cdl_Data = QPlainTextEdit(self.frame_Cdl)
        self.plainTextEdit_Cdl_Data.setObjectName(u"plainTextEdit_Cdl_Data")

        self.horizontalLayout_10.addWidget(self.plainTextEdit_Cdl_Data)

        self.plainTextEdit_Cdl_Label = QPlainTextEdit(self.frame_Cdl)
        self.plainTextEdit_Cdl_Label.setObjectName(u"plainTextEdit_Cdl_Label")

        self.horizontalLayout_10.addWidget(self.plainTextEdit_Cdl_Label)

        self.horizontalLayout_10.setStretch(0, 4)
        self.horizontalLayout_10.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_addData_Cdl = QPushButton(self.frame_Cdl)
        self.btn_addData_Cdl.setObjectName(u"btn_addData_Cdl")

        self.horizontalLayout_3.addWidget(self.btn_addData_Cdl)

        self.btn_importData_Cdl = QPushButton(self.frame_Cdl)
        self.btn_importData_Cdl.setObjectName(u"btn_importData_Cdl")

        self.horizontalLayout_3.addWidget(self.btn_importData_Cdl)

        self.btn_Plot_Cdl = QPushButton(self.frame_Cdl)
        self.btn_Plot_Cdl.setObjectName(u"btn_Plot_Cdl")

        self.horizontalLayout_3.addWidget(self.btn_Plot_Cdl)

        self.btn_saveData_Cdl = QPushButton(self.frame_Cdl)
        self.btn_saveData_Cdl.setObjectName(u"btn_saveData_Cdl")

        self.horizontalLayout_3.addWidget(self.btn_saveData_Cdl)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.frame_Cdl)

        self.frame_Tafel = QFrame(self.scrollAreaWidgetContents)
        self.frame_Tafel.setObjectName(u"frame_Tafel")
        self.frame_Tafel.setFrameShape(QFrame.StyledPanel)
        self.frame_Tafel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_Tafel)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_Tafel = QLabel(self.frame_Tafel)
        self.label_Tafel.setObjectName(u"label_Tafel")
        self.label_Tafel.setFont(font)

        self.verticalLayout_4.addWidget(self.label_Tafel)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit_Tafel_Data = QPlainTextEdit(self.frame_Tafel)
        self.plainTextEdit_Tafel_Data.setObjectName(u"plainTextEdit_Tafel_Data")

        self.horizontalLayout_11.addWidget(self.plainTextEdit_Tafel_Data)

        self.plainTextEdit_Tafel_Label = QPlainTextEdit(self.frame_Tafel)
        self.plainTextEdit_Tafel_Label.setObjectName(u"plainTextEdit_Tafel_Label")

        self.horizontalLayout_11.addWidget(self.plainTextEdit_Tafel_Label)

        self.horizontalLayout_11.setStretch(0, 4)
        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.frame_TafelSlope = QFrame(self.frame_Tafel)
        self.frame_TafelSlope.setObjectName(u"frame_TafelSlope")
        self.frame_TafelSlope.setFrameShape(QFrame.StyledPanel)
        self.frame_TafelSlope.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_TafelSlope)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_addData_Tafel = QPushButton(self.frame_Tafel)
        self.btn_addData_Tafel.setObjectName(u"btn_addData_Tafel")

        self.horizontalLayout_4.addWidget(self.btn_addData_Tafel)

        self.btn_importData_Tafel = QPushButton(self.frame_Tafel)
        self.btn_importData_Tafel.setObjectName(u"btn_importData_Tafel")

        self.horizontalLayout_4.addWidget(self.btn_importData_Tafel)

        self.btn_Plot_Tafel = QPushButton(self.frame_Tafel)
        self.btn_Plot_Tafel.setObjectName(u"btn_Plot_Tafel")

        self.horizontalLayout_4.addWidget(self.btn_Plot_Tafel)

        self.btn_saveData_Tafel = QPushButton(self.frame_Tafel)
        self.btn_saveData_Tafel.setObjectName(u"btn_saveData_Tafel")

        self.horizontalLayout_4.addWidget(self.btn_saveData_Tafel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addWidget(self.frame_Tafel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_electrode_area.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6781\u9762\u79ef", None))
        self.lineEdit_electrode_area.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_electrode_area.setPlaceholderText("")
        self.label_electrode_area_unit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">cm</span><span style=\" font-size:12pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.label_potential_shift.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6781\u8f6c\u79fb\u7535\u52bf", None))
        self.lineEdit_potential_shift.setText(QCoreApplication.translate("MainWindow", u"0.9181", None))
        self.lineEdit_potential_shift.setPlaceholderText("")
        self.label_potential_shift_unit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">V</span></p></body></html>", None))
        self.label_CV.setText(QCoreApplication.translate("MainWindow", u"CV\u6a21\u5757", None))
        self.btn_addData_CV.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_importData_CV.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
        self.btn_Plot_CV.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
        self.btn_saveData_CV.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.label_LSV.setText(QCoreApplication.translate("MainWindow", u"LSV\u6a21\u5757", None))
        self.btn_addData_LSV.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_importData_LSV.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
        self.btn_Plot_LSV.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
        self.btn_saveData_LSV.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.label_Cdl.setText(QCoreApplication.translate("MainWindow", u"Cdl\u6a21\u5757", None))
        self.btn_addData_Cdl.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_importData_Cdl.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
        self.btn_Plot_Cdl.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
        self.btn_saveData_Cdl.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.label_Tafel.setText(QCoreApplication.translate("MainWindow", u"Tafel\u6a21\u5757", None))
        self.btn_addData_Tafel.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_importData_Tafel.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e", None))
        self.btn_Plot_Tafel.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe", None))
        self.btn_saveData_Tafel.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
    # retranslateUi

