# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InsereProtocolo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_Protocolo(object):
    def setupUi(self, Dialog_Protocolo):
        if not Dialog_Protocolo.objectName():
            Dialog_Protocolo.setObjectName(u"Dialog_Protocolo")
        Dialog_Protocolo.resize(647, 450)
        self.frame = QFrame(Dialog_Protocolo)
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
        self.forma_4_protocolo = QLabel(self.frame)
        self.forma_4_protocolo.setObjectName(u"forma_4_protocolo")
        self.forma_4_protocolo.setGeometry(QRect(-40, 0, 231, 361))
        self.forma_4_protocolo.setStyleSheet(u"font: 400pt \"Wingdings 3\";\n"
"color: rgba(248, 248, 248, 10);\n"
"background: transparent;\n"
"")
        self.forma_1_protocolo = QLabel(self.frame)
        self.forma_1_protocolo.setObjectName(u"forma_1_protocolo")
        self.forma_1_protocolo.setGeometry(QRect(0, 0, 581, 351))
        self.forma_1_protocolo.setStyleSheet(u"font: 57 200pt \"Marlett\";\n"
"color: rgba(248, 248, 248, 3);")
        self.btn_cancelar_protocolo = QPushButton(self.frame)
        self.btn_cancelar_protocolo.setObjectName(u"btn_cancelar_protocolo")
        self.btn_cancelar_protocolo.setGeometry(QRect(360, 290, 131, 41))
        font = QFont()
        font.setPointSize(16)
        self.btn_cancelar_protocolo.setFont(font)
        self.btn_cancelar_protocolo.setStyleSheet(u"")
        self.btn_gravar_protocolo = QPushButton(self.frame)
        self.btn_gravar_protocolo.setObjectName(u"btn_gravar_protocolo")
        self.btn_gravar_protocolo.setGeometry(QRect(80, 290, 131, 41))
        self.btn_gravar_protocolo.setFont(font)
        self.btn_gravar_protocolo.setStyleSheet(u"")
        self.label_id_pix_protocolo = QLabel(self.frame)
        self.label_id_pix_protocolo.setObjectName(u"label_id_pix_protocolo")
        self.label_id_pix_protocolo.setGeometry(QRect(100, 80, 181, 31))
        self.label_id_pix_protocolo.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_titulo_protocolo = QLabel(self.frame)
        self.label_titulo_protocolo.setObjectName(u"label_titulo_protocolo")
        self.label_titulo_protocolo.setGeometry(QRect(0, 0, 581, 71))
        self.label_titulo_protocolo.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline\n"
"")
        self.label_titulo_protocolo.setAlignment(Qt.AlignCenter)
        self.label_nome_protocolo = QLabel(self.frame)
        self.label_nome_protocolo.setObjectName(u"label_nome_protocolo")
        self.label_nome_protocolo.setGeometry(QRect(10, 120, 561, 41))
        self.label_nome_protocolo.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_nome_protocolo.setAlignment(Qt.AlignCenter)
        self.label_valor_protocolo = QLabel(self.frame)
        self.label_valor_protocolo.setObjectName(u"label_valor_protocolo")
        self.label_valor_protocolo.setGeometry(QRect(10, 170, 561, 41))
        self.label_valor_protocolo.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_valor_protocolo.setAlignment(Qt.AlignCenter)
        self.label_caixa_protocolo = QLabel(self.frame)
        self.label_caixa_protocolo.setObjectName(u"label_caixa_protocolo")
        self.label_caixa_protocolo.setGeometry(QRect(350, 80, 131, 31))
        self.label_caixa_protocolo.setStyleSheet(u"background: transparent;\n"
"color: rgb(248, 248, 252);\n"
"border: transparent;\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.campo_protocolo = QLineEdit(self.frame)
        self.campo_protocolo.setObjectName(u"campo_protocolo")
        self.campo_protocolo.setGeometry(QRect(30, 230, 521, 40))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.campo_protocolo.setFont(font1)
        self.campo_protocolo.setFocusPolicy(Qt.StrongFocus)
        self.campo_protocolo.setAutoFillBackground(False)
        self.campo_protocolo.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.campo_protocolo.setMaxLength(64)
        self.campo_protocolo.setEchoMode(QLineEdit.Normal)
        self.campo_protocolo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.forma_1_protocolo.raise_()
        self.forma_4_protocolo.raise_()
        self.btn_cancelar_protocolo.raise_()
        self.btn_gravar_protocolo.raise_()
        self.label_id_pix_protocolo.raise_()
        self.label_titulo_protocolo.raise_()
        self.label_nome_protocolo.raise_()
        self.label_valor_protocolo.raise_()
        self.label_caixa_protocolo.raise_()
        self.campo_protocolo.raise_()
        self.frame_2 = QFrame(Dialog_Protocolo)
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

        self.retranslateUi(Dialog_Protocolo)

        QMetaObject.connectSlotsByName(Dialog_Protocolo)
    # setupUi

    def retranslateUi(self, Dialog_Protocolo):
        Dialog_Protocolo.setWindowTitle(QCoreApplication.translate("Dialog_Protocolo", u"Dialog", None))
        self.forma_4_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"z", None))
        self.forma_1_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"y", None))
        self.btn_cancelar_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"Cancelar", None))
        self.btn_gravar_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"Gravar", None))
        self.label_id_pix_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"ID Pix:", None))
        self.label_titulo_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"Inserir o protocolo/certid\u00e3o", None))
        self.label_nome_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"Nome:", None))
        self.label_valor_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"Valor:", None))
        self.label_caixa_protocolo.setText(QCoreApplication.translate("Dialog_Protocolo", u"Caixa: ADM", None))
        self.campo_protocolo.setPlaceholderText(QCoreApplication.translate("Dialog_Protocolo", u"protocolo/certid\u00e3o n\u00bas", None))
    # retranslateUi

