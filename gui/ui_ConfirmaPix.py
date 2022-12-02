# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfirmaPix.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_Confirma_Pix(object):
    def setupUi(self, Dialog_Confirma_Pix):
        if not Dialog_Confirma_Pix.objectName():
            Dialog_Confirma_Pix.setObjectName(u"Dialog_Confirma_Pix")
        Dialog_Confirma_Pix.resize(647, 450)
        self.frame = QFrame(Dialog_Confirma_Pix)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 30, 581, 361))
        self.frame.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(248, 248, 252);\n"
"	font: 16pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(248, 248, 242);\n"
"	background-color: rgb(35,35,35);\n"
"	background-color: rgb(29, 30, 40);\n"
"	border: 0px solid;\n"
"	padding: 6px 9px;\n"
"	text-align:center;\n"
"	border-radius:5px;\n"
"	font: 16pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(35,35,35);\n"
"	background-color: rgb(98, 114, 164);\n"
"	text-align:center;\n"
"	padding: 6px 9px;\n"
"	border-radius:5px;\n"
"	font: 16pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(25,26,33);\n"
"	background-color: rgb(180, 140, 237);\n"
"	text-align:center;\n"
"	padding: 5px 7px;\n"
"	border-radius:5px;\n"
"	font: 15pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QFrame {\n"
"border-radius: 20px;\n"
"background-color: rgb(40, 42, 54);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.forma_4 = QLabel(self.frame)
        self.forma_4.setObjectName(u"forma_4")
        self.forma_4.setGeometry(QRect(-40, 0, 231, 361))
        self.forma_4.setStyleSheet(u"font: 400pt \"Wingdings 3\";\n"
"color: rgba(248, 248, 248, 10);\n"
"background: transparent;\n"
"")
        self.forma_1 = QLabel(self.frame)
        self.forma_1.setObjectName(u"forma_1")
        self.forma_1.setGeometry(QRect(0, 0, 581, 351))
        self.forma_1.setStyleSheet(u"font: 57 200pt \"Marlett\";\n"
"color: rgba(248, 248, 248, 3);")
        self.btn_cancela_libera = QPushButton(self.frame)
        self.btn_cancela_libera.setObjectName(u"btn_cancela_libera")
        self.btn_cancela_libera.setGeometry(QRect(420, 290, 131, 41))
        font = QFont()
        font.setPointSize(16)
        self.btn_cancela_libera.setFont(font)
        self.btn_cancela_libera.setStyleSheet(u"")
        self.btn_confirma_libera = QPushButton(self.frame)
        self.btn_confirma_libera.setObjectName(u"btn_confirma_libera")
        self.btn_confirma_libera.setGeometry(QRect(30, 290, 211, 41))
        self.btn_confirma_libera.setFont(font)
        self.btn_confirma_libera.setStyleSheet(u"")
        self.label_id_pix = QLabel(self.frame)
        self.label_id_pix.setObjectName(u"label_id_pix")
        self.label_id_pix.setGeometry(QRect(100, 80, 181, 31))
        self.label_id_pix.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_titulo = QLabel(self.frame)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(0, 0, 581, 71))
        self.label_titulo.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline\n"
"")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_nome = QLabel(self.frame)
        self.label_nome.setObjectName(u"label_nome")
        self.label_nome.setGeometry(QRect(10, 120, 561, 41))
        self.label_nome.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_nome.setAlignment(Qt.AlignCenter)
        self.label_valor = QLabel(self.frame)
        self.label_valor.setObjectName(u"label_valor")
        self.label_valor.setGeometry(QRect(10, 170, 561, 41))
        self.label_valor.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_valor.setAlignment(Qt.AlignCenter)
        self.label_caixa = QLabel(self.frame)
        self.label_caixa.setObjectName(u"label_caixa")
        self.label_caixa.setGeometry(QRect(350, 80, 131, 31))
        self.label_caixa.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.campo_senha_libera = QLineEdit(self.frame)
        self.campo_senha_libera.setObjectName(u"campo_senha_libera")
        self.campo_senha_libera.setGeometry(QRect(30, 230, 231, 40))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.campo_senha_libera.setFont(font1)
        self.campo_senha_libera.setFocusPolicy(Qt.StrongFocus)
        self.campo_senha_libera.setAutoFillBackground(False)
        self.campo_senha_libera.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.campo_senha_libera.setMaxLength(16)
        self.campo_senha_libera.setEchoMode(QLineEdit.Password)
        self.campo_senha_libera.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_incorrect_user = QLabel(self.frame)
        self.label_incorrect_user.setObjectName(u"label_incorrect_user")
        self.label_incorrect_user.setGeometry(QRect(310, 240, 261, 31))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_incorrect_user.setFont(font2)
        self.label_incorrect_user.setStyleSheet(u"color:rgb(230,230,230);\n"
"background:transparent;")
        self.label_incorrect_user.setAlignment(Qt.AlignCenter)
        self.forma_1.raise_()
        self.forma_4.raise_()
        self.btn_cancela_libera.raise_()
        self.btn_confirma_libera.raise_()
        self.label_id_pix.raise_()
        self.label_titulo.raise_()
        self.label_nome.raise_()
        self.label_valor.raise_()
        self.label_caixa.raise_()
        self.campo_senha_libera.raise_()
        self.label_incorrect_user.raise_()
        self.frame_2 = QFrame(Dialog_Confirma_Pix)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(28, 28, 585, 365))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"border-radius: 21px;\n"
"border: 2px solid rgb(189, 147, 249);\n"
"background: transparent;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(Dialog_Confirma_Pix)

        QMetaObject.connectSlotsByName(Dialog_Confirma_Pix)
    # setupUi

    def retranslateUi(self, Dialog_Confirma_Pix):
        Dialog_Confirma_Pix.setWindowTitle(QCoreApplication.translate("Dialog_Confirma_Pix", u"Dialog", None))
        self.forma_4.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"z", None))
        self.forma_1.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"y", None))
        self.btn_cancela_libera.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"Cancelar", None))
        self.btn_confirma_libera.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"Confirma Libera\u00e7\u00e3o", None))
        self.label_id_pix.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"ID Pix:", None))
        self.label_titulo.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"Confirma a libera\u00e7\u00e3o do pix selecionado?", None))
        self.label_nome.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"Nome:", None))
        self.label_valor.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"Valor:", None))
        self.label_caixa.setText(QCoreApplication.translate("Dialog_Confirma_Pix", u"Caixa: ADM", None))
        self.campo_senha_libera.setPlaceholderText(QCoreApplication.translate("Dialog_Confirma_Pix", u"senha", None))
        self.label_incorrect_user.setText("")
    # retranslateUi

