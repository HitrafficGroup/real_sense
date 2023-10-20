# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowBSMbdU.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(915, 439)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(726, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(236, 240, 241);\n"
"border-radius:10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.camera = QLabel(self.frame_4)
        self.camera.setObjectName(u"camera")

        self.verticalLayout_4.addWidget(self.camera)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnStart = QPushButton(self.frame_3)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setMinimumSize(QSize(0, 40))
        self.btnStart.setMaximumSize(QSize(16777215, 40))
        self.btnStart.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(46, 204, 113 );\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(171, 235, 198);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(46, 204, 113 );\n"
"border-radius:3px;\n"
"color:white\n"
"}")

        self.verticalLayout_2.addWidget(self.btnStart)

        self.btnStop = QPushButton(self.frame_3)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setMinimumSize(QSize(0, 40))
        self.btnStop.setMaximumSize(QSize(16777215, 40))
        self.btnStop.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(205, 97, 85);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(241, 148, 138);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"	background-color: rgb(205, 97, 85);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.btnStop)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.camera.setText("")
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"DETENER", None))
    # retranslateUi

