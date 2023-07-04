# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 574)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 370, 480))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(24, 20, 317, 441))
        self.label_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(10, 10, 10, 100), stop:1 rgba(55, 55, 55, 144));\n"
"border-radius:20px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 49, 284, 401))
        self.label_3.setStyleSheet(u"background-color: rgb(84, 84, 84);\n"
"border-radius: 15px;")
        self.label_login = QLabel(self.widget)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setGeometry(QRect(45, 100, 271, 40))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setMouseTracking(True)
        self.label_login.setStyleSheet(u"color: rgba(255,255,255, 210)")
        self.label_login.setAlignment(Qt.AlignCenter)
        self.campo_usuario = QLineEdit(self.widget)
        self.campo_usuario.setObjectName(u"campo_usuario")
        self.campo_usuario.setGeometry(QRect(80, 180, 200, 40))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.campo_usuario.setFont(font1)
        self.campo_usuario.setFocusPolicy(Qt.StrongFocus)
        self.campo_usuario.setAutoFillBackground(False)
        self.campo_usuario.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.campo_usuario.setMaxLength(3)
        self.campo_usuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.campo_senha = QLineEdit(self.widget)
        self.campo_senha.setObjectName(u"campo_senha")
        self.campo_senha.setGeometry(QRect(80, 240, 200, 40))
        self.campo_senha.setFont(font1)
        self.campo_senha.setFocusPolicy(Qt.StrongFocus)
        self.campo_senha.setAutoFillBackground(False)
        self.campo_senha.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.campo_senha.setEchoMode(QLineEdit.Password)
        self.campo_senha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_nome_usuario = QLabel(self.widget)
        self.label_nome_usuario.setObjectName(u"label_nome_usuario")
        self.label_nome_usuario.setGeometry(QRect(40, 200, 281, 40))
        self.label_nome_usuario.setFont(font)
        self.label_nome_usuario.setMouseTracking(True)
        self.label_nome_usuario.setStyleSheet(u"color: rgba(255,255,255, 210)")
        self.label_nome_usuario.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.widget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(80, 330, 201, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_login.setFont(font2)
        self.btn_login.setFocusPolicy(Qt.NoFocus)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 20, 20, 219), stop:1 rgba(100, 100, 100, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 40, 40, 219), stop:1 rgba(120, 120, 120, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:2px;\n"
"	padding-top:2px;\n"
"	background-color:rgba(120, 120, 120,200);\n"
"}")
        self.label_incorrect_user = QLabel(self.widget)
        self.label_incorrect_user.setObjectName(u"label_incorrect_user")
        self.label_incorrect_user.setGeometry(QRect(80, 380, 201, 31))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_incorrect_user.setFont(font3)
        self.label_incorrect_user.setStyleSheet(u"color:rgb(230,230,230);\n"
"background:transparent;")
        self.label_incorrect_user.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(24, 230, 317, 231))
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.506, y2:0, stop:0.420455 rgba(36, 36, 36, 191), stop:1 rgba(132, 132, 132, 0));\n"
"border-radius: 20px;")
        self.sair = QPushButton(self.widget)
        self.sair.setObjectName(u"sair")
        self.sair.setGeometry(QRect(284, 53, 33, 33))
        self.sair.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"	\n"
"	background-color: rgb(83, 83, 83);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(120, 120, 120,200);\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:2px;\n"
"	padding-top:2px;\n"
"	background-color:rgba(105, 118, 132,200);\n"
"	border-radius:15px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sair.setIcon(icon)
        self.sair.setIconSize(QSize(26, 26))
        self.label_correct_user = QLabel(self.widget)
        self.label_correct_user.setObjectName(u"label_correct_user")
        self.label_correct_user.setGeometry(QRect(80, 380, 201, 31))
        self.label_correct_user.setFont(font3)
        self.label_correct_user.setStyleSheet(u"color:rgb(230,230,230);\n"
"background:transparent;")
        self.label_correct_user.setAlignment(Qt.AlignCenter)
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_login.raise_()
        self.label_nome_usuario.raise_()
        self.label_5.raise_()
        self.label_incorrect_user.raise_()
        self.btn_login.raise_()
        self.campo_senha.raise_()
        self.campo_usuario.raise_()
        self.sair.raise_()
        self.label_correct_user.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.campo_usuario.setPlaceholderText(QCoreApplication.translate("Form", u"usu\u00e1rio", None))
        self.campo_senha.setPlaceholderText(QCoreApplication.translate("Form", u"senha", None))
        self.label_nome_usuario.setText("")
        self.btn_login.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_incorrect_user.setText("")
        self.label_5.setText("")
        self.sair.setText("")
        self.label_correct_user.setText("")
    # retranslateUi

