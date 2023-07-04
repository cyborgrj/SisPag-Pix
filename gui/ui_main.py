# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1120, 540))
        MainWindow.setMaximumSize(QSize(1120, 540))
        MainWindow.setIconSize(QSize(25, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(890, 540))
        self.centralwidget.setMaximumSize(QSize(1120, 540))
        self.centralwidget.setFocusPolicy(Qt.StrongFocus)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(1120, 45))
        self.top_frame.setAutoFillBackground(False)
        self.top_frame.setStyleSheet(u"")
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_left_frame = QFrame(self.top_frame)
        self.top_left_frame.setObjectName(u"top_left_frame")
        self.top_left_frame.setMinimumSize(QSize(60, 45))
        self.top_left_frame.setMaximumSize(QSize(60, 45))
        self.top_left_frame.setStyleSheet(u"background-color: rgb(25, 26, 33);")
        self.top_left_frame.setFrameShape(QFrame.StyledPanel)
        self.top_left_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.top_left_frame)

        self.top_center_frame = QFrame(self.top_frame)
        self.top_center_frame.setObjectName(u"top_center_frame")
        self.top_center_frame.setStyleSheet(u"background-color: rgb(25, 26, 33);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(25, 26, 33, 255), stop:1 rgba(40, 42, 54, 255));")
        self.top_center_frame.setFrameShape(QFrame.StyledPanel)
        self.top_center_frame.setFrameShadow(QFrame.Raised)
        self.label_titulo = QLabel(self.top_center_frame)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(-54, -11, 1111, 61))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo.setFont(font)
        self.label_titulo.setAutoFillBackground(False)
        self.label_titulo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"background: transparent;")
        self.label_titulo.setTextFormat(Qt.AutoText)
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.top_center_frame)


        self.verticalLayout.addWidget(self.top_frame)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(1120, 540))
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_left_base = QFrame(self.content)
        self.frame_left_base.setObjectName(u"frame_left_base")
        self.frame_left_base.setMinimumSize(QSize(45, 600))
        self.frame_left_base.setMaximumSize(QSize(45, 680))
        self.frame_left_base.setStyleSheet(u"/*rosa rgb(255, 121, 198); */\n"
"/*lil\u00e1s rgb(189, 147, 249);*/\n"
"\n"
"*{\n"
"	background-color: rgb(25, 26, 33);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton {\n"
"	color: rgb(248,248,242);\n"
"	background-color: rgb(25, 26, 33);\n"
"	border: 0px solid;\n"
"	text-align:left;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(60,60,60);\n"
"	background-color: rgb(40, 42, 54);\n"
"	text-align:left;\n"
"	border-radius:6px;\n"
"}\n"
"QPushButton:pressed {\n"
"	border: 2px solid rgb(189, 147, 249);\n"
"}")
        self.frame_left_base.setFrameShape(QFrame.NoFrame)
        self.frame_left_base.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_base)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_left_base)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setEnabled(True)
        self.frame_left_menu.setMinimumSize(QSize(45, 45))
        self.frame_left_menu.setMaximumSize(QSize(45, 480))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 0, 0, 0)
        self.menu = QPushButton(self.frame_left_menu)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(250, 40))
        self.menu.setMaximumSize(QSize(250, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.menu.setFont(font1)
        self.menu.setFocusPolicy(Qt.NoFocus)
        self.menu.setLayoutDirection(Qt.LeftToRight)
        self.menu.setStyleSheet(u"	padding: 6px 9px;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/icons/icons/arrow-left.svg", QSize(), QIcon.Selected, QIcon.On)
        self.menu.setIcon(icon)
        self.menu.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.menu)

        self.gerar_qr_code = QPushButton(self.frame_left_menu)
        self.gerar_qr_code.setObjectName(u"gerar_qr_code")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gerar_qr_code.sizePolicy().hasHeightForWidth())
        self.gerar_qr_code.setSizePolicy(sizePolicy1)
        self.gerar_qr_code.setMinimumSize(QSize(250, 40))
        self.gerar_qr_code.setMaximumSize(QSize(250, 40))
        self.gerar_qr_code.setFont(font1)
        self.gerar_qr_code.setFocusPolicy(Qt.NoFocus)
        self.gerar_qr_code.setLayoutDirection(Qt.LeftToRight)
        self.gerar_qr_code.setStyleSheet(u"	padding: 6px 9px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gerar_qr_code.setIcon(icon1)
        self.gerar_qr_code.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.gerar_qr_code)

        self.imprimir = QPushButton(self.frame_left_menu)
        self.imprimir.setObjectName(u"imprimir")
        self.imprimir.setMinimumSize(QSize(250, 40))
        self.imprimir.setMaximumSize(QSize(250, 40))
        self.imprimir.setFont(font1)
        self.imprimir.setFocusPolicy(Qt.NoFocus)
        self.imprimir.setStyleSheet(u"	padding: 6px 9px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imprimir.setIcon(icon2)
        self.imprimir.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.imprimir)

        self.consulta_pgto = QPushButton(self.frame_left_menu)
        self.consulta_pgto.setObjectName(u"consulta_pgto")
        self.consulta_pgto.setMinimumSize(QSize(250, 40))
        self.consulta_pgto.setMaximumSize(QSize(250, 40))
        self.consulta_pgto.setFont(font1)
        self.consulta_pgto.setFocusPolicy(Qt.NoFocus)
        self.consulta_pgto.setStyleSheet(u"	padding: 6px 9px;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/refresh-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.consulta_pgto.setIcon(icon3)
        self.consulta_pgto.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.consulta_pgto)

        self.cadastrar_usuario = QPushButton(self.frame_left_menu)
        self.cadastrar_usuario.setObjectName(u"cadastrar_usuario")
        self.cadastrar_usuario.setMinimumSize(QSize(250, 40))
        self.cadastrar_usuario.setMaximumSize(QSize(250, 40))
        self.cadastrar_usuario.setFont(font1)
        self.cadastrar_usuario.setFocusPolicy(Qt.NoFocus)
        self.cadastrar_usuario.setStyleSheet(u"padding: 6px 10px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cadastrar_usuario.setIcon(icon4)
        self.cadastrar_usuario.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.cadastrar_usuario)

        self.autorizar_pix = QPushButton(self.frame_left_menu)
        self.autorizar_pix.setObjectName(u"autorizar_pix")
        self.autorizar_pix.setMinimumSize(QSize(250, 40))
        self.autorizar_pix.setMaximumSize(QSize(250, 40))
        self.autorizar_pix.setFont(font1)
        self.autorizar_pix.setFocusPolicy(Qt.NoFocus)
        self.autorizar_pix.setStyleSheet(u"padding: 6px 7px;")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.autorizar_pix.setIcon(icon5)
        self.autorizar_pix.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.autorizar_pix)

        self.vertical_spacer = QSpacerItem(20, 240, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.vertical_spacer)

        self.settings = QPushButton(self.frame_left_menu)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(250, 40))
        self.settings.setMaximumSize(QSize(250, 40))
        self.settings.setFont(font1)
        self.settings.setFocusPolicy(Qt.TabFocus)
        self.settings.setStyleSheet(u"	padding: 6px 9px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon6)
        self.settings.setIconSize(QSize(25, 25))
        self.settings.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.settings)

        self.sair = QPushButton(self.frame_left_menu)
        self.sair.setObjectName(u"sair")
        self.sair.setMinimumSize(QSize(250, 40))
        self.sair.setMaximumSize(QSize(250, 40))
        self.sair.setFont(font1)
        self.sair.setFocusPolicy(Qt.TabFocus)
        self.sair.setStyleSheet(u"	padding: 6px 9px;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sair.setIcon(icon7)
        self.sair.setIconSize(QSize(25, 25))
        self.sair.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.sair)


        self.verticalLayout_2.addWidget(self.frame_left_menu, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_left_base)

        self.right_panel = QFrame(self.content)
        self.right_panel.setObjectName(u"right_panel")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.right_panel.sizePolicy().hasHeightForWidth())
        self.right_panel.setSizePolicy(sizePolicy2)
        self.right_panel.setMinimumSize(QSize(600, 0))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.right_panel.setFont(font2)
        self.right_panel.setAutoFillBackground(False)
        self.right_panel.setStyleSheet(u"*{\n"
"background-color: rgb(40, 42, 54);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QDateEdit {\n"
"border: 2px solid rgb(189, 147, 249);\n"
"color: rgb(248, 248, 242);\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"padding: 5px;\n"
"border-radius: 5px\n"
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
"	border: 2px solid rgb(248,248,252);\n"
"	color: rgb(25,26,33);\n"
"	background-color: rgb(180, 140, 237);\n"
"	text-align:center;\n"
"	padding: 5px 7px;\n"
"	border-radius:5px;\n"
"	font: 15pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QLineEdit{\n"
"backgroun"
                        "d: transparent;\n"
"border: none;\n"
"border-bottom:3px solid rgba(248,248,252,150);\n"
"padding: 5px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(248, 248, 252);\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(248, 248, 252);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(248,248,242);\n"
"background-color: rgb(25, 26, 33);\n"
"alternate-background-color: rgb(40, 42, 54);\n"
"}\n"
"\n"
"QComboBox{\n"
"border: 2px solid rgb(189, 147, 249);\n"
"color: rgb(248, 248, 242);\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"padding: 5px;\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QComboBox:drop-down {\n"
"border: 0px	\n"
"}\n"
"\n"
"QComboBox:down-arrow {\n"
"image: url(:/icons/icons/chevron-down.svg);\n"
"margin-right:10\n"
"}\n"
"\n"
"QComboBox:on {\n"
"border: 2px solid rgb(248, 248, 242);\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"color: rgb(248, 248, 242);\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"border: 1px solid rgba(0,0,0,10%);\n"
"padding: 5px;\n"
"background-colo"
                        "r: rgb(40, 42, 54);\n"
"}\n"
"\n"
"QComboBox QListView:item{\n"
"padding-left: 10px;\n"
"background-color: rgb(40, 42, 54);\n"
"}\n"
"\n"
"QComboBox QListView:item:hover{\n"
"background-color: rgb(29, 30, 40);\n"
"}\n"
"\n"
"QComboBox QListView:item:selected{\n"
"background-color: rgb(29, 30, 40);\n"
"}")
        self.right_panel.setFrameShape(QFrame.NoFrame)
        self.right_panel.setFrameShadow(QFrame.Raised)
        self.right_panel.setLineWidth(0)
        self.stackedWidget = QStackedWidget(self.right_panel)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-10, 10, 1081, 470))
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setStyleSheet(u"")
        self.page_gerar = QWidget()
        self.page_gerar.setObjectName(u"page_gerar")
        self.page_gerar.setStyleSheet(u"")
        self.campo_apresentante = QLineEdit(self.page_gerar)
        self.campo_apresentante.setObjectName(u"campo_apresentante")
        self.campo_apresentante.setGeometry(QRect(210, 140, 641, 41))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.campo_apresentante.setFont(font3)
        self.campo_apresentante.setStyleSheet(u"padding: 5px;")
        self.campo_apresentante.setMaxLength(45)
        self.campo_apresentante.setClearButtonEnabled(True)
        self.campo_valor = QLineEdit(self.page_gerar)
        self.campo_valor.setObjectName(u"campo_valor")
        self.campo_valor.setGeometry(QRect(250, 208, 301, 41))
        self.campo_valor.setFont(font3)
        self.campo_valor.setStyleSheet(u"padding: 5px;")
        self.campo_valor.setMaxLength(20)
        self.campo_valor.setClearButtonEnabled(True)
        self.txt_id_pix = QLabel(self.page_gerar)
        self.txt_id_pix.setObjectName(u"txt_id_pix")
        self.txt_id_pix.setGeometry(QRect(201, 280, 251, 43))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.txt_id_pix.setFont(font4)
        self.txt_id_pix.setStyleSheet(u"background-color: transparent;\n"
"padding: 5px;")
        self.txt_moeda = QLabel(self.page_gerar)
        self.txt_moeda.setObjectName(u"txt_moeda")
        self.txt_moeda.setGeometry(QRect(201, 210, 55, 43))
        self.txt_moeda.setFont(font4)
        self.txt_moeda.setStyleSheet(u"background-color: transparent;\n"
"padding: 5px;")
        self.btn_gerar_qrcode = QPushButton(self.page_gerar)
        self.btn_gerar_qrcode.setObjectName(u"btn_gerar_qrcode")
        self.btn_gerar_qrcode.setGeometry(QRect(170, 360, 161, 41))
        font5 = QFont()
        font5.setPointSize(16)
        self.btn_gerar_qrcode.setFont(font5)
        self.btn_gerar_qrcode.setStyleSheet(u"")
        self.btn_limpar_campos = QPushButton(self.page_gerar)
        self.btn_limpar_campos.setObjectName(u"btn_limpar_campos")
        self.btn_limpar_campos.setGeometry(QRect(380, 360, 161, 41))
        self.btn_limpar_campos.setFont(font5)
        self.btn_limpar_campos.setStyleSheet(u"")
        self.campo_usuario_atual = QLabel(self.page_gerar)
        self.campo_usuario_atual.setObjectName(u"campo_usuario_atual")
        self.campo_usuario_atual.setGeometry(QRect(30, 10, 531, 31))
        self.campo_usuario_atual.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"background: transparent;")
        self.forma_3 = QLabel(self.page_gerar)
        self.forma_3.setObjectName(u"forma_3")
        self.forma_3.setGeometry(QRect(400, -80, 671, 541))
        self.forma_3.setStyleSheet(u"font: 600pt \"Wingdings 3\";\n"
"color: rgba(248, 248, 248, 10);\n"
"background: transparent;\n"
"")
        self.forma_4 = QLabel(self.page_gerar)
        self.forma_4.setObjectName(u"forma_4")
        self.forma_4.setGeometry(QRect(-60, -10, 611, 471))
        self.forma_4.setStyleSheet(u"font: 700pt \"Wingdings 3\";\n"
"color: rgba(248, 248, 248, 10);\n"
"background: transparent;\n"
"")
        self.forma_1 = QLabel(self.page_gerar)
        self.forma_1.setObjectName(u"forma_1")
        self.forma_1.setGeometry(QRect(19, 0, 971, 541))
        self.forma_1.setStyleSheet(u"font: 57 300pt \"Marlett\";\n"
"color: rgba(248, 248, 248, 3);")
        self.forma_2 = QLabel(self.page_gerar)
        self.forma_2.setObjectName(u"forma_2")
        self.forma_2.setGeometry(QRect(410, -170, 501, 411))
        self.forma_2.setStyleSheet(u"font: 57 500pt \"Marlett\";\n"
"color: rgba(248, 248, 248, 3);\n"
"background: transparent;")
        self.campo_cpf_apresentante = QLineEdit(self.page_gerar)
        self.campo_cpf_apresentante.setObjectName(u"campo_cpf_apresentante")
        self.campo_cpf_apresentante.setGeometry(QRect(210, 80, 241, 41))
        self.campo_cpf_apresentante.setFont(font3)
        self.campo_cpf_apresentante.setAutoFillBackground(False)
        self.campo_cpf_apresentante.setStyleSheet(u"padding: 5px;")
        self.campo_cpf_apresentante.setMaxLength(14)
        self.campo_cpf_apresentante.setClearButtonEnabled(True)
        self.somente_numeros = QLabel(self.page_gerar)
        self.somente_numeros.setObjectName(u"somente_numeros")
        self.somente_numeros.setGeometry(QRect(480, 80, 201, 43))
        self.somente_numeros.setFont(font4)
        self.somente_numeros.setStyleSheet(u"background-color: transparent;\n"
"padding: 5px;")
        self.btn_cadastrar_solicitante = QPushButton(self.page_gerar)
        self.btn_cadastrar_solicitante.setObjectName(u"btn_cadastrar_solicitante")
        self.btn_cadastrar_solicitante.setGeometry(QRect(690, 80, 161, 41))
        self.btn_cadastrar_solicitante.setFont(font5)
        self.btn_cadastrar_solicitante.setStyleSheet(u"")
        self.btn_enviar_email = QPushButton(self.page_gerar)
        self.btn_enviar_email.setObjectName(u"btn_enviar_email")
        self.btn_enviar_email.setGeometry(QRect(670, 360, 161, 41))
        self.btn_enviar_email.setFont(font5)
        self.btn_enviar_email.setStyleSheet(u"")
        self.campo_email_solicitante = QLineEdit(self.page_gerar)
        self.campo_email_solicitante.setObjectName(u"campo_email_solicitante")
        self.campo_email_solicitante.setGeometry(QRect(510, 290, 481, 41))
        self.campo_email_solicitante.setFont(font3)
        self.campo_email_solicitante.setStyleSheet(u"padding: 5px;")
        self.campo_email_solicitante.setMaxLength(50)
        self.campo_email_solicitante.setAlignment(Qt.AlignCenter)
        self.campo_email_solicitante.setClearButtonEnabled(True)
        self.stackedWidget.addWidget(self.page_gerar)
        self.forma_1.raise_()
        self.forma_4.raise_()
        self.forma_3.raise_()
        self.txt_id_pix.raise_()
        self.btn_limpar_campos.raise_()
        self.campo_usuario_atual.raise_()
        self.btn_gerar_qrcode.raise_()
        self.txt_moeda.raise_()
        self.forma_2.raise_()
        self.campo_valor.raise_()
        self.campo_apresentante.raise_()
        self.campo_cpf_apresentante.raise_()
        self.somente_numeros.raise_()
        self.btn_cadastrar_solicitante.raise_()
        self.btn_enviar_email.raise_()
        self.campo_email_solicitante.raise_()
        self.page_imprimir = QWidget()
        self.page_imprimir.setObjectName(u"page_imprimir")
        self.frame_10 = QFrame(self.page_imprimir)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, -10, 1071, 471))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.btn_buscar_imprimir = QPushButton(self.frame_10)
        self.btn_buscar_imprimir.setObjectName(u"btn_buscar_imprimir")
        self.btn_buscar_imprimir.setGeometry(QRect(540, 270, 191, 41))
        self.btn_buscar_imprimir.setFont(font5)
        self.btn_buscar_imprimir.setStyleSheet(u"")
        self.txt_buscar = QLabel(self.frame_10)
        self.txt_buscar.setObjectName(u"txt_buscar")
        self.txt_buscar.setGeometry(QRect(210, 210, 261, 43))
        self.txt_buscar.setFont(font4)
        self.txt_buscar.setStyleSheet(u"padding: 5px;\n"
"background:transparent;")
        self.txt_obs = QLabel(self.frame_10)
        self.txt_obs.setObjectName(u"txt_obs")
        self.txt_obs.setGeometry(QRect(210, 320, 391, 43))
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.txt_obs.setFont(font6)
        self.txt_obs.setStyleSheet(u"padding: 5px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background:transparent;")
        self.campo_txt_id_imprimir_pix = QLineEdit(self.frame_10)
        self.campo_txt_id_imprimir_pix.setObjectName(u"campo_txt_id_imprimir_pix")
        self.campo_txt_id_imprimir_pix.setGeometry(QRect(220, 260, 301, 47))
        self.campo_txt_id_imprimir_pix.setFont(font3)
        self.campo_txt_id_imprimir_pix.setStyleSheet(u"")
        self.campo_txt_id_imprimir_pix.setMaxLength(45)
        self.campo_txt_id_imprimir_pix.setClearButtonEnabled(True)
        self.btn_imprimir = QPushButton(self.frame_10)
        self.btn_imprimir.setObjectName(u"btn_imprimir")
        self.btn_imprimir.setGeometry(QRect(220, 100, 191, 41))
        self.btn_imprimir.setFont(font5)
        self.btn_imprimir.setStyleSheet(u"")
        self.txt_obs_2 = QLabel(self.frame_10)
        self.txt_obs_2.setObjectName(u"txt_obs_2")
        self.txt_obs_2.setGeometry(QRect(420, 100, 391, 43))
        self.txt_obs_2.setFont(font6)
        self.txt_obs_2.setStyleSheet(u"padding: 5px;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background:transparent;")
        self.forma_5 = QLabel(self.frame_10)
        self.forma_5.setObjectName(u"forma_5")
        self.forma_5.setGeometry(QRect(-70, 0, 611, 471))
        self.forma_5.setStyleSheet(u"font: 700pt \"Wingdings 3\";\n"
"color: rgba(248, 248, 248, 10);\n"
"background: transparent;\n"
"")
        self.forma_6 = QLabel(self.frame_10)
        self.forma_6.setObjectName(u"forma_6")
        self.forma_6.setGeometry(QRect(10, 10, 971, 541))
        self.forma_6.setStyleSheet(u"font: 57 300pt \"Marlett\";\n"
"color: rgba(248, 248, 248, 3);\n"
"background:transparent;")
        self.forma_7 = QLabel(self.frame_10)
        self.forma_7.setObjectName(u"forma_7")
        self.forma_7.setGeometry(QRect(390, -70, 671, 541))
        self.forma_7.setStyleSheet(u"font: 600pt \"Wingdings 3\";\n"
"color: rgba(248, 248, 248, 10);\n"
"background: transparent;\n"
"")
        self.forma_8 = QLabel(self.frame_10)
        self.forma_8.setObjectName(u"forma_8")
        self.forma_8.setGeometry(QRect(400, -160, 501, 411))
        self.forma_8.setStyleSheet(u"font: 57 500pt \"Marlett\";\n"
"color: rgba(248, 248, 248, 3);\n"
"background: transparent;")
        self.forma_7.raise_()
        self.forma_8.raise_()
        self.forma_5.raise_()
        self.forma_6.raise_()
        self.txt_buscar.raise_()
        self.btn_buscar_imprimir.raise_()
        self.campo_txt_id_imprimir_pix.raise_()
        self.txt_obs.raise_()
        self.txt_obs_2.raise_()
        self.btn_imprimir.raise_()
        self.stackedWidget.addWidget(self.page_imprimir)
        self.page_consultar = QWidget()
        self.page_consultar.setObjectName(u"page_consultar")
        self.table_consulta_pix = QTableWidget(self.page_consultar)
        if (self.table_consulta_pix.columnCount() < 8):
            self.table_consulta_pix.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.table_consulta_pix.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.table_consulta_pix.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.table_consulta_pix.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.table_consulta_pix.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.table_consulta_pix.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.table_consulta_pix.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_consulta_pix.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_consulta_pix.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.table_consulta_pix.setObjectName(u"table_consulta_pix")
        self.table_consulta_pix.setGeometry(QRect(30, 40, 1001, 371))
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(11)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.table_consulta_pix.setFont(font7)
        self.table_consulta_pix.setStyleSheet(u"")
        self.table_consulta_pix.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.table_consulta_pix.setTabKeyNavigation(False)
        self.table_consulta_pix.setProperty("showDropIndicator", False)
        self.table_consulta_pix.setDragDropOverwriteMode(False)
        self.table_consulta_pix.setAlternatingRowColors(True)
        self.table_consulta_pix.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_consulta_pix.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.btn_inser_num_interno_consulta_pix = QPushButton(self.page_consultar)
        self.btn_inser_num_interno_consulta_pix.setObjectName(u"btn_inser_num_interno_consulta_pix")
        self.btn_inser_num_interno_consulta_pix.setGeometry(QRect(40, 417, 231, 41))
        self.combo_limite_consultapix = QComboBox(self.page_consultar)
        self.combo_limite_consultapix.addItem("")
        self.combo_limite_consultapix.addItem("")
        self.combo_limite_consultapix.addItem("")
        self.combo_limite_consultapix.addItem("")
        self.combo_limite_consultapix.setObjectName(u"combo_limite_consultapix")
        self.combo_limite_consultapix.setGeometry(QRect(670, 0, 105, 33))
        self.combo_limite_consultapix.setStyleSheet(u"")
        self.combo_filtro_consultapix = QComboBox(self.page_consultar)
        self.combo_filtro_consultapix.addItem("")
        self.combo_filtro_consultapix.addItem("")
        self.combo_filtro_consultapix.addItem("")
        self.combo_filtro_consultapix.setObjectName(u"combo_filtro_consultapix")
        self.combo_filtro_consultapix.setGeometry(QRect(540, 0, 121, 33))
        self.combo_filtro_consultapix.setStyleSheet(u"")
        self.resultado_busca_consultapix = QLabel(self.page_consultar)
        self.resultado_busca_consultapix.setObjectName(u"resultado_busca_consultapix")
        self.resultado_busca_consultapix.setGeometry(QRect(400, 420, 371, 31))
        self.resultado_busca_consultapix.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.btn_set_small_font_consulta = QPushButton(self.page_consultar)
        self.btn_set_small_font_consulta.setObjectName(u"btn_set_small_font_consulta")
        self.btn_set_small_font_consulta.setGeometry(QRect(860, 419, 31, 31))
        self.btn_set_small_font_consulta.setFocusPolicy(Qt.NoFocus)
        self.btn_set_small_font_consulta.setStyleSheet(u"background: transparent;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.btn_set_big_font_consulta = QPushButton(self.page_consultar)
        self.btn_set_big_font_consulta.setObjectName(u"btn_set_big_font_consulta")
        self.btn_set_big_font_consulta.setGeometry(QRect(866, 410, 51, 41))
        font8 = QFont()
        font8.setFamily(u"MS Shell Dlg 2")
        font8.setPointSize(18)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setWeight(50)
        self.btn_set_big_font_consulta.setFont(font8)
        self.btn_set_big_font_consulta.setFocusPolicy(Qt.NoFocus)
        self.btn_set_big_font_consulta.setStyleSheet(u"background: transparent;\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.combo_filtro_data_consultapix = QComboBox(self.page_consultar)
        self.combo_filtro_data_consultapix.addItem("")
        self.combo_filtro_data_consultapix.addItem("")
        self.combo_filtro_data_consultapix.setObjectName(u"combo_filtro_data_consultapix")
        self.combo_filtro_data_consultapix.setGeometry(QRect(800, 0, 81, 33))
        self.combo_filtro_data_consultapix.setStyleSheet(u"")
        self.btn_buscar_consulta_pix = QPushButton(self.page_consultar)
        self.btn_buscar_consulta_pix.setObjectName(u"btn_buscar_consulta_pix")
        self.btn_buscar_consulta_pix.setGeometry(QRect(439, 0, 91, 33))
        self.btn_buscar_consulta_pix.setFont(font5)
        self.btn_buscar_consulta_pix.setFocusPolicy(Qt.NoFocus)
        self.btn_buscar_consulta_pix.setStyleSheet(u"")
        self.campo_buscar_id_consulta_pix = QLineEdit(self.page_consultar)
        self.campo_buscar_id_consulta_pix.setObjectName(u"campo_buscar_id_consulta_pix")
        self.campo_buscar_id_consulta_pix.setGeometry(QRect(40, -8, 121, 41))
        self.campo_buscar_id_consulta_pix.setFont(font3)
        self.campo_buscar_id_consulta_pix.setStyleSheet(u"")
        self.campo_buscar_id_consulta_pix.setMaxLength(8)
        self.campo_buscar_id_consulta_pix.setClearButtonEnabled(True)
        self.campo_buscar_apresentante_consulta_pix = QLineEdit(self.page_consultar)
        self.campo_buscar_apresentante_consulta_pix.setObjectName(u"campo_buscar_apresentante_consulta_pix")
        self.campo_buscar_apresentante_consulta_pix.setGeometry(QRect(170, -8, 251, 41))
        self.campo_buscar_apresentante_consulta_pix.setFont(font3)
        self.campo_buscar_apresentante_consulta_pix.setStyleSheet(u"")
        self.campo_buscar_apresentante_consulta_pix.setMaxLength(25)
        self.campo_buscar_apresentante_consulta_pix.setClearButtonEnabled(True)
        self.filtro_data_consultapix = QDateEdit(self.page_consultar)
        self.filtro_data_consultapix.setObjectName(u"filtro_data_consultapix")
        self.filtro_data_consultapix.setGeometry(QRect(890, 0, 131, 33))
        self.filtro_data_consultapix.setFrame(True)
        self.filtro_data_consultapix.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.filtro_data_consultapix.setProperty("showGroupSeparator", False)
        self.filtro_data_consultapix.setCalendarPopup(True)
        self.filtro_data_consultapix.setDate(QDate(2000, 1, 1))
        self.stackedWidget.addWidget(self.page_consultar)
        self.page_cadastrar = QWidget()
        self.page_cadastrar.setObjectName(u"page_cadastrar")
        self.frame = QFrame(self.page_cadastrar)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 96, 509, 281))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.campo_repetir_senha = QLineEdit(self.frame)
        self.campo_repetir_senha.setObjectName(u"campo_repetir_senha")
        self.campo_repetir_senha.setGeometry(QRect(10, 190, 261, 39))
        self.campo_repetir_senha.setFont(font3)
        self.campo_repetir_senha.setStyleSheet(u"")
        self.campo_repetir_senha.setMaxLength(12)
        self.campo_repetir_senha.setEchoMode(QLineEdit.Password)
        self.campo_repetir_senha.setClearButtonEnabled(True)
        self.campo_nome_completo = QLineEdit(self.frame)
        self.campo_nome_completo.setObjectName(u"campo_nome_completo")
        self.campo_nome_completo.setGeometry(QRect(10, 70, 471, 39))
        self.campo_nome_completo.setFont(font3)
        self.campo_nome_completo.setStyleSheet(u"")
        self.campo_nome_completo.setMaxLength(45)
        self.campo_nome_completo.setClearButtonEnabled(True)
        self.campo_senha = QLineEdit(self.frame)
        self.campo_senha.setObjectName(u"campo_senha")
        self.campo_senha.setGeometry(QRect(10, 130, 261, 39))
        self.campo_senha.setFont(font3)
        self.campo_senha.setStyleSheet(u"")
        self.campo_senha.setMaxLength(12)
        self.campo_senha.setEchoMode(QLineEdit.Password)
        self.campo_senha.setClearButtonEnabled(True)
        self.campo_usuario = QLineEdit(self.frame)
        self.campo_usuario.setObjectName(u"campo_usuario")
        self.campo_usuario.setGeometry(QRect(10, 10, 186, 39))
        self.campo_usuario.setFont(font3)
        self.campo_usuario.setStyleSheet(u"")
        self.campo_usuario.setMaxLength(3)
        self.campo_usuario.setClearButtonEnabled(True)
        self.frame_2 = QFrame(self.page_cadastrar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(230, 20, 511, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.combo_tipo_usuario = QComboBox(self.frame_2)
        self.combo_tipo_usuario.addItem("")
        self.combo_tipo_usuario.addItem("")
        self.combo_tipo_usuario.addItem("")
        self.combo_tipo_usuario.setObjectName(u"combo_tipo_usuario")
        self.combo_tipo_usuario.setGeometry(QRect(180, 12, 147, 27))
        font9 = QFont()
        font9.setFamily(u"MS Shell Dlg 2")
        font9.setPointSize(13)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setWeight(50)
        self.combo_tipo_usuario.setFont(font9)
        self.combo_tipo_usuario.setStyleSheet(u"font: 13pt \"MS Shell Dlg 2\";")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(12, 12, 154, 25))
        self.label.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\"")
        self.frame_3 = QFrame(self.page_cadastrar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 379, 391, 57))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_cadastrar = QPushButton(self.frame_3)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btn_cadastrar)

        self.btn_cancelar = QPushButton(self.frame_3)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.horizontalLayout_3.addWidget(self.btn_cancelar)

        self.stackedWidget.addWidget(self.page_cadastrar)
        self.page_autorizar = QWidget()
        self.page_autorizar.setObjectName(u"page_autorizar")
        self.page_autorizar.setStyleSheet(u"")
        self.frame_8 = QFrame(self.page_autorizar)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, -10, 1071, 471))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(16, 20, 1031, 41))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.campo_buscar_id = QLineEdit(self.frame_7)
        self.campo_buscar_id.setObjectName(u"campo_buscar_id")
        self.campo_buscar_id.setGeometry(QRect(10, 0, 121, 41))
        self.campo_buscar_id.setFont(font3)
        self.campo_buscar_id.setStyleSheet(u"")
        self.campo_buscar_id.setMaxLength(8)
        self.campo_buscar_id.setClearButtonEnabled(True)
        self.btn_buscar_alteraPix = QPushButton(self.frame_7)
        self.btn_buscar_alteraPix.setObjectName(u"btn_buscar_alteraPix")
        self.btn_buscar_alteraPix.setGeometry(QRect(409, 8, 91, 33))
        self.btn_buscar_alteraPix.setFont(font5)
        self.btn_buscar_alteraPix.setFocusPolicy(Qt.NoFocus)
        self.btn_buscar_alteraPix.setStyleSheet(u"")
        self.campo_buscar_apresentante = QLineEdit(self.frame_7)
        self.campo_buscar_apresentante.setObjectName(u"campo_buscar_apresentante")
        self.campo_buscar_apresentante.setGeometry(QRect(140, 0, 251, 41))
        self.campo_buscar_apresentante.setFont(font3)
        self.campo_buscar_apresentante.setStyleSheet(u"")
        self.campo_buscar_apresentante.setMaxLength(25)
        self.campo_buscar_apresentante.setClearButtonEnabled(True)
        self.combo_limite_altera = QComboBox(self.frame_7)
        self.combo_limite_altera.addItem("")
        self.combo_limite_altera.addItem("")
        self.combo_limite_altera.addItem("")
        self.combo_limite_altera.addItem("")
        self.combo_limite_altera.setObjectName(u"combo_limite_altera")
        self.combo_limite_altera.setGeometry(QRect(640, 8, 111, 33))
        self.combo_limite_altera.setStyleSheet(u"")
        self.combo_filtro_alterapix = QComboBox(self.frame_7)
        self.combo_filtro_alterapix.addItem("")
        self.combo_filtro_alterapix.addItem("")
        self.combo_filtro_alterapix.addItem("")
        self.combo_filtro_alterapix.setObjectName(u"combo_filtro_alterapix")
        self.combo_filtro_alterapix.setGeometry(QRect(510, 8, 121, 33))
        self.combo_filtro_alterapix.setStyleSheet(u"")
        self.filtro_dia_alterapix = QDateEdit(self.frame_7)
        self.filtro_dia_alterapix.setObjectName(u"filtro_dia_alterapix")
        self.filtro_dia_alterapix.setGeometry(QRect(870, 8, 131, 33))
        self.filtro_dia_alterapix.setFrame(True)
        self.filtro_dia_alterapix.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.filtro_dia_alterapix.setProperty("showGroupSeparator", False)
        self.filtro_dia_alterapix.setCalendarPopup(True)
        self.filtro_dia_alterapix.setDate(QDate(2000, 1, 1))
        self.combo_filtro_data_alterapix = QComboBox(self.frame_7)
        self.combo_filtro_data_alterapix.addItem("")
        self.combo_filtro_data_alterapix.addItem("")
        self.combo_filtro_data_alterapix.setObjectName(u"combo_filtro_data_alterapix")
        self.combo_filtro_data_alterapix.setGeometry(QRect(780, 8, 81, 33))
        self.combo_filtro_data_alterapix.setStyleSheet(u"")
        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 90, 153, 152))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_8)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 71, 1061, 401))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.btn_liberar_pix = QPushButton(self.frame_4)
        self.btn_liberar_pix.setObjectName(u"btn_liberar_pix")
        self.btn_liberar_pix.setGeometry(QRect(20, 350, 160, 35))
        self.btn_liberar_pix.setFont(font5)
        self.btn_liberar_pix.setFocusPolicy(Qt.NoFocus)
        self.btn_liberar_pix.setStyleSheet(u"")
        self.btn_cancelar_altera_pix = QPushButton(self.frame_4)
        self.btn_cancelar_altera_pix.setObjectName(u"btn_cancelar_altera_pix")
        self.btn_cancelar_altera_pix.setGeometry(QRect(190, 350, 160, 35))
        self.btn_cancelar_altera_pix.setFont(font5)
        self.btn_cancelar_altera_pix.setFocusPolicy(Qt.NoFocus)
        self.btn_cancelar_altera_pix.setStyleSheet(u"")
        self.table_busca_e_autoriza_pix = QTableWidget(self.frame_4)
        if (self.table_busca_e_autoriza_pix.columnCount() < 10):
            self.table_busca_e_autoriza_pix.setColumnCount(10)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.table_busca_e_autoriza_pix.setHorizontalHeaderItem(9, __qtablewidgetitem17)
        self.table_busca_e_autoriza_pix.setObjectName(u"table_busca_e_autoriza_pix")
        self.table_busca_e_autoriza_pix.setGeometry(QRect(20, 0, 1001, 341))
        self.table_busca_e_autoriza_pix.setFont(font7)
        self.table_busca_e_autoriza_pix.setStyleSheet(u"")
        self.table_busca_e_autoriza_pix.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_busca_e_autoriza_pix.setProperty("showDropIndicator", False)
        self.table_busca_e_autoriza_pix.setDragDropOverwriteMode(False)
        self.table_busca_e_autoriza_pix.setDefaultDropAction(Qt.IgnoreAction)
        self.table_busca_e_autoriza_pix.setAlternatingRowColors(True)
        self.table_busca_e_autoriza_pix.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_busca_e_autoriza_pix.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_busca_e_autoriza_pix.setSortingEnabled(True)
        self.table_busca_e_autoriza_pix.setCornerButtonEnabled(True)
        self.resultado_busca_autoriza = QLabel(self.frame_4)
        self.resultado_busca_autoriza.setObjectName(u"resultado_busca_autoriza")
        self.resultado_busca_autoriza.setGeometry(QRect(380, 350, 371, 31))
        self.resultado_busca_autoriza.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.btn_set_small_font = QPushButton(self.frame_4)
        self.btn_set_small_font.setObjectName(u"btn_set_small_font")
        self.btn_set_small_font.setGeometry(QRect(774, 379, 31, 31))
        self.btn_set_small_font.setFocusPolicy(Qt.NoFocus)
        self.btn_set_small_font.setStyleSheet(u"background: transparent;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.btn_set_big_font = QPushButton(self.frame_4)
        self.btn_set_big_font.setObjectName(u"btn_set_big_font")
        self.btn_set_big_font.setGeometry(QRect(780, 370, 51, 41))
        self.btn_set_big_font.setFont(font8)
        self.btn_set_big_font.setFocusPolicy(Qt.NoFocus)
        self.btn_set_big_font.setStyleSheet(u"background: transparent;\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.page_autorizar)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.frame_5 = QFrame(self.page_settings)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(110, 10, 831, 201))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.combo_tema = QComboBox(self.frame_5)
        self.combo_tema.addItem("")
        self.combo_tema.addItem("")
        self.combo_tema.addItem("")
        self.combo_tema.addItem("")
        self.combo_tema.addItem("")
        self.combo_tema.setObjectName(u"combo_tema")
        self.combo_tema.setGeometry(QRect(190, 80, 161, 33))
        self.combo_tema.setStyleSheet(u"")
        self.btn_aplicar_tema = QPushButton(self.frame_5)
        self.btn_aplicar_tema.setObjectName(u"btn_aplicar_tema")
        self.btn_aplicar_tema.setGeometry(QRect(370, 78, 171, 37))
        self.btn_aplicar_tema.setStyleSheet(u"")
        self.btn_aplicar_tema_2 = QPushButton(self.frame_5)
        self.btn_aplicar_tema_2.setObjectName(u"btn_aplicar_tema_2")
        self.btn_aplicar_tema_2.setGeometry(QRect(280, 139, 171, 37))
        self.btn_aplicar_tema_2.setStyleSheet(u"")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 171, 51))
        self.aparencia_bg = QPushButton(self.frame_5)
        self.aparencia_bg.setObjectName(u"aparencia_bg")
        self.aparencia_bg.setEnabled(False)
        self.aparencia_bg.setGeometry(QRect(0, 0, 821, 61))
        self.aparencia_bg.setFocusPolicy(Qt.NoFocus)
        self.aparencia_bg.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 130, 251, 51))
        self.label_aparencia = QLabel(self.frame_5)
        self.label_aparencia.setObjectName(u"label_aparencia")
        self.label_aparencia.setGeometry(QRect(-2, 0, 821, 51))
        self.label_aparencia.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"background:transparent")
        self.label_aparencia.setAlignment(Qt.AlignCenter)
        self.frame_9 = QFrame(self.page_settings)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(110, 230, 831, 201))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_gera_relatorio = QLabel(self.frame_9)
        self.label_gera_relatorio.setObjectName(u"label_gera_relatorio")
        self.label_gera_relatorio.setGeometry(QRect(10, 70, 451, 51))
        self.label_gera_relatorio.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.general_settings_bg = QPushButton(self.frame_9)
        self.general_settings_bg.setObjectName(u"general_settings_bg")
        self.general_settings_bg.setEnabled(False)
        self.general_settings_bg.setGeometry(QRect(0, 0, 821, 61))
        self.general_settings_bg.setFocusPolicy(Qt.NoFocus)
        self.general_settings_bg.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_status = QLabel(self.frame_9)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(10, 130, 451, 51))
        self.label_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_configuracoes = QLabel(self.frame_9)
        self.label_configuracoes.setObjectName(u"label_configuracoes")
        self.label_configuracoes.setGeometry(QRect(-3, 1, 821, 51))
        self.label_configuracoes.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"background:transparent")
        self.label_configuracoes.setAlignment(Qt.AlignCenter)
        self.btn_gera_excel = QPushButton(self.frame_9)
        self.btn_gera_excel.setObjectName(u"btn_gera_excel")
        self.btn_gera_excel.setGeometry(QRect(630, 110, 151, 41))
        self.filtro_dia_gera_excel = QDateEdit(self.frame_9)
        self.filtro_dia_gera_excel.setObjectName(u"filtro_dia_gera_excel")
        self.filtro_dia_gera_excel.setGeometry(QRect(480, 80, 131, 33))
        self.filtro_dia_gera_excel.setFrame(True)
        self.filtro_dia_gera_excel.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.filtro_dia_gera_excel.setProperty("showGroupSeparator", False)
        self.filtro_dia_gera_excel.setCalendarPopup(True)
        self.filtro_dia_gera_excel.setDate(QDate(2000, 1, 1))
        self.combo_filtro_gera_excel = QComboBox(self.frame_9)
        self.combo_filtro_gera_excel.addItem("")
        self.combo_filtro_gera_excel.addItem("")
        self.combo_filtro_gera_excel.addItem("")
        self.combo_filtro_gera_excel.setObjectName(u"combo_filtro_gera_excel")
        self.combo_filtro_gera_excel.setGeometry(QRect(480, 140, 121, 33))
        self.combo_filtro_gera_excel.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.page_settings)
        self.label_creditos = QLabel(self.right_panel)
        self.label_creditos.setObjectName(u"label_creditos")
        self.label_creditos.setGeometry(QRect(10, 470, 441, 20))
        font10 = QFont()
        font10.setPointSize(10)
        self.label_creditos.setFont(font10)
        self.label_creditos.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout.addWidget(self.right_panel)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.campo_apresentante, self.campo_cpf_apresentante)
        QWidget.setTabOrder(self.campo_cpf_apresentante, self.campo_valor)
        QWidget.setTabOrder(self.campo_valor, self.btn_gerar_qrcode)
        QWidget.setTabOrder(self.btn_gerar_qrcode, self.btn_limpar_campos)
        QWidget.setTabOrder(self.btn_limpar_campos, self.settings)
        QWidget.setTabOrder(self.settings, self.sair)
        QWidget.setTabOrder(self.sair, self.btn_imprimir)
        QWidget.setTabOrder(self.btn_imprimir, self.campo_txt_id_imprimir_pix)
        QWidget.setTabOrder(self.campo_txt_id_imprimir_pix, self.btn_buscar_imprimir)
        QWidget.setTabOrder(self.btn_buscar_imprimir, self.campo_buscar_id_consulta_pix)
        QWidget.setTabOrder(self.campo_buscar_id_consulta_pix, self.campo_buscar_apresentante_consulta_pix)
        QWidget.setTabOrder(self.campo_buscar_apresentante_consulta_pix, self.combo_filtro_consultapix)
        QWidget.setTabOrder(self.combo_filtro_consultapix, self.combo_limite_consultapix)
        QWidget.setTabOrder(self.combo_limite_consultapix, self.combo_filtro_data_consultapix)
        QWidget.setTabOrder(self.combo_filtro_data_consultapix, self.filtro_data_consultapix)
        QWidget.setTabOrder(self.filtro_data_consultapix, self.table_consulta_pix)
        QWidget.setTabOrder(self.table_consulta_pix, self.btn_inser_num_interno_consulta_pix)
        QWidget.setTabOrder(self.btn_inser_num_interno_consulta_pix, self.combo_tipo_usuario)
        QWidget.setTabOrder(self.combo_tipo_usuario, self.campo_usuario)
        QWidget.setTabOrder(self.campo_usuario, self.campo_nome_completo)
        QWidget.setTabOrder(self.campo_nome_completo, self.campo_senha)
        QWidget.setTabOrder(self.campo_senha, self.campo_repetir_senha)
        QWidget.setTabOrder(self.campo_repetir_senha, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.btn_cancelar)
        QWidget.setTabOrder(self.btn_cancelar, self.campo_buscar_id)
        QWidget.setTabOrder(self.campo_buscar_id, self.campo_buscar_apresentante)
        QWidget.setTabOrder(self.campo_buscar_apresentante, self.combo_filtro_alterapix)
        QWidget.setTabOrder(self.combo_filtro_alterapix, self.combo_limite_altera)
        QWidget.setTabOrder(self.combo_limite_altera, self.combo_filtro_data_alterapix)
        QWidget.setTabOrder(self.combo_filtro_data_alterapix, self.filtro_dia_alterapix)
        QWidget.setTabOrder(self.filtro_dia_alterapix, self.table_busca_e_autoriza_pix)
        QWidget.setTabOrder(self.table_busca_e_autoriza_pix, self.combo_tema)
        QWidget.setTabOrder(self.combo_tema, self.btn_aplicar_tema)
        QWidget.setTabOrder(self.btn_aplicar_tema, self.btn_aplicar_tema_2)

        self.retranslateUi(MainWindow)
        self.sair.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"SisPag PIX - 2\u00ba Cart\u00f3rio de Registro de Im\u00f3veis do Rio de Janeiro", None))
        self.menu.setText(QCoreApplication.translate("MainWindow", u"  Recolher o menu", None))
        self.gerar_qr_code.setText(QCoreApplication.translate("MainWindow", u"  Gerar QrCode", None))
        self.imprimir.setText(QCoreApplication.translate("MainWindow", u"  Imprimir o QrCode", None))
        self.consulta_pgto.setText(QCoreApplication.translate("MainWindow", u"  Consultar Pagamento", None))
        self.cadastrar_usuario.setText(QCoreApplication.translate("MainWindow", u"  Cadastro de Usu\u00e1rios", None))
        self.autorizar_pix.setText(QCoreApplication.translate("MainWindow", u"  Liberar Pix", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"  Configura\u00e7\u00f5es", None))
        self.sair.setText(QCoreApplication.translate("MainWindow", u"  Encerrar", None))
        self.campo_apresentante.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Apresentante", None))
        self.campo_valor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Valor do t\u00edtulo", None))
        self.txt_id_pix.setText(QCoreApplication.translate("MainWindow", u"ID Pix: ", None))
        self.txt_moeda.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.btn_gerar_qrcode.setText(QCoreApplication.translate("MainWindow", u"Gerar QrCode", None))
        self.btn_limpar_campos.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.campo_usuario_atual.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.forma_3.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.forma_4.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.forma_1.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.forma_2.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.campo_cpf_apresentante.setInputMask("")
        self.campo_cpf_apresentante.setText("")
        self.campo_cpf_apresentante.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF ou CNPJ", None))
        self.somente_numeros.setText(QCoreApplication.translate("MainWindow", u"(Somente n\u00fameros)", None))
        self.btn_cadastrar_solicitante.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_enviar_email.setText(QCoreApplication.translate("MainWindow", u"Enviar e-mail", None))
        self.campo_email_solicitante.setPlaceholderText(QCoreApplication.translate("MainWindow", u"       e-mail do solicitante", None))
        self.btn_buscar_imprimir.setText(QCoreApplication.translate("MainWindow", u"Buscar e Imprimir", None))
        self.txt_buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar um QrCode Anterior", None))
        self.txt_obs.setText(QCoreApplication.translate("MainWindow", u"Obs.: Respeitar ma\u00edusculas e min\u00fasculas", None))
        self.campo_txt_id_imprimir_pix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TxT ID: ", None))
        self.btn_imprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir QrCode", None))
        self.txt_obs_2.setText(QCoreApplication.translate("MainWindow", u"(imprime o \u00faltimo QrCode gerado)", None))
        self.forma_5.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.forma_6.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.forma_7.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.forma_8.setText(QCoreApplication.translate("MainWindow", u"a", None))
        ___qtablewidgetitem = self.table_consulta_pix.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Pix", None));
        ___qtablewidgetitem1 = self.table_consulta_pix.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Apresentante", None));
        ___qtablewidgetitem2 = self.table_consulta_pix.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem3 = self.table_consulta_pix.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data/Hora", None));
        ___qtablewidgetitem4 = self.table_consulta_pix.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem5 = self.table_consulta_pix.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Ano", None));
        ___qtablewidgetitem6 = self.table_consulta_pix.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Certid\u00e3o N\u00ba", None));
        ___qtablewidgetitem7 = self.table_consulta_pix.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Protocolo N\u00ba", None));
        self.btn_inser_num_interno_consulta_pix.setText(QCoreApplication.translate("MainWindow", u"Inserir protocolo(s)", None))
        self.combo_limite_consultapix.setItemText(0, QCoreApplication.translate("MainWindow", u"10 items", None))
        self.combo_limite_consultapix.setItemText(1, QCoreApplication.translate("MainWindow", u"30 items", None))
        self.combo_limite_consultapix.setItemText(2, QCoreApplication.translate("MainWindow", u"50 items", None))
        self.combo_limite_consultapix.setItemText(3, QCoreApplication.translate("MainWindow", u"100 items", None))

        self.combo_filtro_consultapix.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.combo_filtro_consultapix.setItemText(1, QCoreApplication.translate("MainWindow", u"Aguardando", None))
        self.combo_filtro_consultapix.setItemText(2, QCoreApplication.translate("MainWindow", u"Pagos", None))

        self.resultado_busca_consultapix.setText("")
        self.btn_set_small_font_consulta.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.btn_set_big_font_consulta.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.combo_filtro_data_consultapix.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.combo_filtro_data_consultapix.setItemText(1, QCoreApplication.translate("MainWindow", u"Data", None))

        self.btn_buscar_consulta_pix.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.campo_buscar_id_consulta_pix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar ID:", None))
        self.campo_buscar_apresentante_consulta_pix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por apresentante", None))
        self.campo_repetir_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repetir Senha", None))
        self.campo_nome_completo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Completo", None))
        self.campo_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.campo_usuario.setInputMask("")
        self.campo_usuario.setText("")
        self.campo_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.combo_tipo_usuario.setItemText(0, QCoreApplication.translate("MainWindow", u"Caixa", None))
        self.combo_tipo_usuario.setItemText(1, QCoreApplication.translate("MainWindow", u"Contabilidade", None))
        self.combo_tipo_usuario.setItemText(2, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Tipo de Usu\u00e1rio:", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.campo_buscar_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar ID:", None))
        self.btn_buscar_alteraPix.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.campo_buscar_apresentante.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por apresentante", None))
        self.combo_limite_altera.setItemText(0, QCoreApplication.translate("MainWindow", u"10 items", None))
        self.combo_limite_altera.setItemText(1, QCoreApplication.translate("MainWindow", u"30 items", None))
        self.combo_limite_altera.setItemText(2, QCoreApplication.translate("MainWindow", u"50 items", None))
        self.combo_limite_altera.setItemText(3, QCoreApplication.translate("MainWindow", u"100 items", None))

        self.combo_filtro_alterapix.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.combo_filtro_alterapix.setItemText(1, QCoreApplication.translate("MainWindow", u"Aguardando", None))
        self.combo_filtro_alterapix.setItemText(2, QCoreApplication.translate("MainWindow", u"Pagos", None))

        self.combo_filtro_data_alterapix.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.combo_filtro_data_alterapix.setItemText(1, QCoreApplication.translate("MainWindow", u"Data", None))

        self.btn_liberar_pix.setText(QCoreApplication.translate("MainWindow", u"Liberar Pix", None))
        self.btn_cancelar_altera_pix.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        ___qtablewidgetitem8 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID Pix", None));
        ___qtablewidgetitem9 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Apresentante", None));
        ___qtablewidgetitem10 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem11 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Caixa", None));
        ___qtablewidgetitem12 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Data/Hora", None));
        ___qtablewidgetitem13 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem14 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Liberado", None));
        ___qtablewidgetitem15 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Ano", None));
        ___qtablewidgetitem16 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Certid\u00e3o N\u00ba", None));
        ___qtablewidgetitem17 = self.table_busca_e_autoriza_pix.horizontalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Protocolo N\u00ba", None));
        self.resultado_busca_autoriza.setText("")
        self.btn_set_small_font.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.btn_set_big_font.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.combo_tema.setItemText(0, QCoreApplication.translate("MainWindow", u"Escolher Tema", None))
        self.combo_tema.setItemText(1, QCoreApplication.translate("MainWindow", u"Drcl Night", None))
        self.combo_tema.setItemText(2, QCoreApplication.translate("MainWindow", u"Drcl Claro", None))
        self.combo_tema.setItemText(3, QCoreApplication.translate("MainWindow", u"Mono Escuro", None))
        self.combo_tema.setItemText(4, QCoreApplication.translate("MainWindow", u"Mono Claro", None))

        self.btn_aplicar_tema.setText(QCoreApplication.translate("MainWindow", u"Aplicar Tema", None))
        self.btn_aplicar_tema_2.setText(QCoreApplication.translate("MainWindow", u"Escolher fonte...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Esquema de cores:", None))
        self.aparencia_bg.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tamanho da fonte (tabelas)", None))
        self.label_aparencia.setText(QCoreApplication.translate("MainWindow", u"Apar\u00eancia", None))
        self.label_gera_relatorio.setText(QCoreApplication.translate("MainWindow", u"Gerar relat\u00f3rio em Excel dos pagamentos por dia", None))
        self.general_settings_bg.setText("")
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_configuracoes.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio em Excel", None))
        self.btn_gera_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.combo_filtro_gera_excel.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))
        self.combo_filtro_gera_excel.setItemText(1, QCoreApplication.translate("MainWindow", u"Aguardando", None))
        self.combo_filtro_gera_excel.setItemText(2, QCoreApplication.translate("MainWindow", u"Pagos", None))

        self.label_creditos.setText(QCoreApplication.translate("MainWindow", u"Sistema de gerenciamento de Pix, desenvolvido por Eduardo Rossini - 2022.", None))
    # retranslateUi

