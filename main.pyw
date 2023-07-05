########################################################################
## IMPORTS
########################################################################
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from datetime import datetime
from fpdf import FPDF
import qrcode
import time
import subprocess
from db.db import *
import locale
import configparser
import re
from xlsx import xlsx
import re 
import email_rgi.mail as mail_rgi
from decimal import Decimal
      
########################################################################
# IMPORTAR ARQUIVOS GUI
from gui import *
########################################################################


########################################################################
# Criar objeto de janela para "system tray" global
window_obj = []
########################################################################



########################################################################
# Carregar configurações do arquivo config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Configurações de aparência
TEMA = config['APARENCIA']['TEMA']
FONTE = config['APARENCIA']['FONTE']

# Configurações do banco de dados Users
DBNAME = config['DATABASE USERS']['DBNAME']

# Configurações do banco de dados Pix
HOSTNAME = config['DATABASE PIX']['HOSTNAME']
DATABASE = config['DATABASE PIX']['DATABASE']
USERNAME = config['DATABASE PIX']['USERNAME']
PWD = config['DATABASE PIX']['PWD']
PORT_ID = config['DATABASE PIX']['PORT_ID']

# Configurações de localização
LOCALE = config['LOCALIZACAO']['LOCALE']

# Configurações de RGI
RGI_NOME = config['RGI']['NOME']
RGI_CHAVE_PIX = config['RGI']['CHAVEPIX']
RGI_CIDADE = config['RGI']['CIDADE']
PERCENTUAL = config['RGI']['PERCENTUAL']
TAXA_MINIMA = config['RGI']['TAXA_MINIMA']
TAXA_MAXIMA = config['RGI']['TAXA_MAXIMA']

# Configurações de Aplicativos Adobe e caminho do PDF
ADOBE_READER = config['ADOBE']['ACROBAT']
ADOBE_PDF_FILE = config['ADOBE']['PDFFILE']
ADOBE_PDF_FILE_EXTRA = config['ADOBE']['PDFFILE_EXTRA']
ADOBE_QRCODE = config['ADOBE']['QRCODE']

########################################################################


class Tema:
    def __init__(self, nome_tema: str):
        self.nome_tema = nome_tema
        self.escolher_tema(nome_tema)

    def escolher_tema(self, novo_tema: str):
        self.nome_tema = novo_tema
        if novo_tema == "Mono Escuro":
            print('Tema escolhido: Mono Dark')
            # Definições do tema:
            self.side_menu_hover_bg_color = (60, 60, 60)
            self.side_menu_bg_color = (35, 35, 35)
            self.side_alt_menu_bg_color = (100, 100, 100)
            self.rightside_menu_bg_color = (70, 70, 70)
            
            # Cores dos botões
            self.btn_text_color = (248, 248, 242)
            self.btn_bg_color = (45, 45, 45)
            self.btn_pressed_color = (170, 170, 170)
            self.btn_bg_color_hover = (120, 120, 120)
            self.btn_pressed_text = (45, 45, 45)

            # Cores das formas
            self.forma_color1 = (248, 248, 248, 3)
            self.forma_color2 = (248, 248, 248, 10)

            # Cores da tabela
            self.table_item_bg_color = (50, 50, 50)
            self.table_item_alt_bg_color = (60, 60, 60)
            self.table_item_text_color = (248, 248, 242)

            # Cores das fontes
            self.left_menu_text_color = (248, 248, 242)
            self.main_text_color = (248, 248, 242)

            # Cores chaves
            self.key_color_1 = (255, 255, 200)
            self.cor_destaque_1 = (170, 170, 170)
            self.cor_destaque_2 = (120, 120, 120)
            self.input_text_bg_color = (255,255,255,150)

            # Stops do gradiente RGBA
            self.stop1 = (36, 36, 36, 255)
            self.stop2 = (80, 80, 80, 255)

        elif novo_tema == "Mono Claro":
            print('Tema escolhido: Mono Light')
            # Definições do tema:
            self.side_menu_hover_bg_color = (90, 90, 90)
            self.side_menu_bg_color = (70, 70, 70)
            self.side_alt_menu_bg_color = (130, 130, 130)
            self.rightside_menu_bg_color = (200, 200, 200)
            
            # Cores dos botões
            self.btn_text_color = (40, 40, 40)
            self.btn_bg_color = (120, 120, 120)
            self.btn_pressed_color = (95, 95, 95)
            self.btn_pressed_text = (230, 230, 230)
            self.btn_bg_color_hover = (70, 70, 70)

            # Cores das formas
            self.forma_color1 = (148, 148, 148, 60)
            self.forma_color2 = (148, 148, 148, 40)

            # Cores da tabela
            self.table_item_bg_color = (230, 230, 230)
            self.table_item_alt_bg_color = (190, 190, 190)
            self.table_item_text_color = (40, 40, 40)

            # Cores das fontes
            self.left_menu_text_color = (248, 248, 248)
            self.main_text_color = (40, 40, 40)

            # Cores chaves
            self.key_color_1 = (255, 255, 255)
            self.cor_destaque_1 = (220, 220, 220)
            self.cor_destaque_2 = (190, 190, 190)
            self.input_text_bg_color = (10, 10, 10, 250)

            # Stops do gradiente RGBA
            self.stop1 = (36, 36, 36, 255)
            self.stop2 = (80, 80, 80, 255)

        elif novo_tema == "Drcl Night":
            print('Tema escolhido: Drácula Night')
            # Definições do tema:
            # Cores de fundo de tela/botões
            self.side_menu_hover_bg_color = (40, 42, 54)
            self.side_menu_bg_color = (25, 26, 33)
            self.side_alt_menu_bg_color = (49, 51, 65)
            self.rightside_menu_bg_color = (40, 42, 54)
            
            # Cores dos botões
            self.btn_text_color = (248, 248, 242)            
            self.btn_bg_color = (29, 30, 40)
            self.btn_pressed_color = (189, 147, 249)
            self.btn_bg_color_hover = (96, 114, 164)
            self.btn_pressed_text = (29, 30, 40)

            # Cores das formas
            self.forma_color1 = (248, 248, 248, 3)
            self.forma_color2 = (248, 248, 248, 10)

            # Cores da tabela
            self.table_item_bg_color = (33, 34, 44)
            self.table_item_alt_bg_color = (40, 42, 54)
            self.table_item_text_color = (248, 248, 242)

            # Cores das fontes
            self.left_menu_text_color = (248, 248, 242)
            self.main_text_color = (248, 248, 242)

            # Cores chaves
            self.key_color_1 = (98, 114, 139)
            
            self.cor_destaque_1 = (189, 147, 249)
            self.cor_destaque_2 = (239, 113, 159)
            self.input_text_bg_color = (255,255,255,150)

            # Stops do gradiente RGBA
            self.stop1 = (25, 26, 33, 255)
            self.stop2 = (40, 42, 54, 255)

        elif novo_tema == "Drcl Claro":
            print('Tema escolhido: Drácula Claro')
            # Definições do tema:
            # Cores de fundo de tela/botões
            self.side_menu_hover_bg_color = (80, 84, 108)
            self.side_menu_bg_color = (50, 52, 66)
            self.side_alt_menu_bg_color = (49, 51, 65)
            self.rightside_menu_bg_color = (248, 248, 242)
            
            # Cores dos botões
            self.btn_text_color = (248, 248, 242)            
            self.btn_bg_color = (98, 114, 164)
            self.btn_pressed_color = (98, 114, 164)
            self.btn_bg_color_hover = (189, 147, 249)
            self.btn_pressed_text = (248, 248, 242)
            
            # Cores da tabela
            self.table_item_bg_color = (248, 248, 242)
            self.table_item_alt_bg_color = (218, 218, 212)
            self.table_item_text_color = (50, 52, 66)

            # Cores das fontes
            self.left_menu_text_color = (248, 248, 242)
            self.main_text_color = (40, 42, 54)

            # Cores das formas
            self.forma_color1 = (148, 148, 148, 60)
            self.forma_color2 = (148, 148, 148, 40)
            
            # Cores chaves
            self.key_color_1 = (98, 114, 139)
            self.cor_destaque_1 = (189, 147, 249)
            self.cor_destaque_2 = (239, 113, 159)
            self.input_text_bg_color = (40, 42, 54, 150)

            # Stops do gradiente RGBA
            self.stop1 = (25, 26, 33, 255)
            self.stop2 = (40, 42, 54, 255)


class Pagamento:
    def __init__(self, id_tx, nome, valor, copia_cola):
        self.valor = valor
        self.id_tx = id_tx
        self.nome = nome
        self.copia_cola = copia_cola
        self.pix_id = ''

    def insert_user(self):
        return 'QrCode Gerado com sucesso!'


def show_tray_message(self, tray: QSystemTrayIcon, notification_title, notification_message):
    icon = QIcon(r'C:\SisPag Pix\gui\icons\pix_icon.png')
    duration = 3 * 1000
    tray.showMessage(notification_title, notification_message, icon, duration)


def verifica_email(email):  
    regex = r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"
    return re.search(regex, email) 


def limpa_cpf_cnpj(cpf_cnpj: str) -> str:
    resultado = ''
    for digit in cpf_cnpj:
        if digit.isdigit():
            resultado += digit
    return resultado


def verifica_cpf(cpf: str):
    cpf_formatado = ''
    erro = True
    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números
    if len(numbers) != 11:
        return erro, ''

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return erro, ''

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return erro, ''

    i = 0
    for n in numbers:
        if i == 2 or i == 5:
            cpf_formatado = cpf_formatado + str(n) + '.'
        elif i == 8:
            cpf_formatado = cpf_formatado + str(n) + '-'
        else:
            cpf_formatado = cpf_formatado + str(n)
        i += 1
    erro = False

    return erro, cpf_formatado


def verifica_cnpj(cnpj: str):
    """
    Efetua a validação do CNPJ somente com relação aos números informados, formatação não é importante.
    """
    cnpj_formatado = ''
    erro = True
    cnpj = ''.join(re.findall('\d', str(cnpj)))

    if (not cnpj) or (len(cnpj) < 14):
        return erro, ''

    # Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam
    digitos = [int(digito) for digito in cnpj if digito.isdigit()]
    novo = digitos[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < 14:
        r = sum([x * y for (x, y) in zip(novo, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        prod.insert(0, 6)

    # Se o número gerado coincidir com o número original, é válido
    if novo == digitos:
        erro = False

    i = 0
    for c in cnpj:
        if i == 1 or i == 4:
            cnpj_formatado = cnpj_formatado + str(c) + '.'
        elif i == 7:
            cnpj_formatado = cnpj_formatado + str(c) + '/'
        elif i == 11:
            cnpj_formatado = cnpj_formatado + str(c) + '-'
        else:
            cnpj_formatado = cnpj_formatado + str(c)
        i += 1
    erro = False

    return erro, cnpj_formatado


def formata_cpf_cnpj(cpf_cnpj):
    if len(cpf_cnpj) == 11:
        cpf_formatado = ''
        for i in range(11):
            if i == 2 or i == 5:
                cpf_formatado += cpf_cnpj[i] + '.'
            elif i == 8:
                cpf_formatado += cpf_cnpj[i] + '-'
            else:
                cpf_formatado += cpf_cnpj[i]
        return cpf_formatado
    if len(cpf_cnpj) == 14:
        cnpj_formatado = ''
        for i in range(14):
            if i == 1 or i == 4:
                cnpj_formatado += cpf_cnpj[i] + '.'
            elif i == 7:
                cnpj_formatado += cpf_cnpj[i] + '/'
            elif i == 11:
                cnpj_formatado += cpf_cnpj[i] + '-'
            else:
                cnpj_formatado += cpf_cnpj[i]
        return cnpj_formatado
    return 'erro'

class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 37)
        self.cell(40, 16,'')
        self.ln()
        self.cell(40, 16, 'Cartório do 2º Ofício de Registro', align='center')
        self.ln()
        self.cell(40, 16, '  de Imóveis do Rio de Janeiro', align='center')
        self.ln()

    def chapter_title(self):
        pass

    def chapter_body(self, apresentante, valor, id, copia_cola):
        # Times 12
        self.set_font('Times', '', 26)
        self.image(ADOBE_QRCODE, 60, 140, 100)
        # Line break
        self.ln()
        self.cell(50, 14, f"Identificador nº: {id}", align='center')
        self.ln()
        self.set_font('Times', '', 20)
        self.cell(20, 14, f"Apresentante: {apresentante}")
        self.ln()
        self.set_font('Times', '', 26)
        self.cell(20, 14, f"Valor: {valor}")
        self.ln()
        self.ln()
        self.cell(80, 14, '                       QRCode para Pagamento', align='center')
        for i in range(0, 8, 1):
            self.ln()
        self.cell(80, 14, f"Pix Copia e Cola:")
        self.ln()
        self.set_font('Times', '', 12)
        # se dividido no pdf o código Pix acaba perdendo sua integridade...
        # pixParte1, pixParte2 = dividePixCopiaCola(copia_cola)
        self.multi_cell(190, 5, f"{copia_cola}")
        self.ln()

    def print_chapter(self, apresentante, valor, id, copia_cola):
        self.add_page()
        self.chapter_title()
        self.chapter_body(apresentante, valor, id, copia_cola)



def dia_corrente():
    data = datetime.today()
    strData = data.strftime('%d/%m/%Y')
    dia, mes, ano = strData.split('/')
    # print(f'Dia: {dia}, mês: {mes}, ano: {ano}')
    return int(ano), int(mes), int(dia)


def carrega_fonte_config():
    nome_fonte = 'MS Shell Dlg 2'
    tamanho_fonte = 11
    try:
        find = re.search(r'(?<=\().*,\d\d', FONTE)
        grupo = find.group().split(',')
    except Exception as error:
        print('Erro ao carregar fonte do arquivo config.ini, carregando fonte padrão...')
        print(error)
        return nome_fonte, tamanho_fonte
    else:
        if grupo != None:
            nome_fonte = str(grupo[0])
            tamanho_fonte = int(grupo[1])
        else:
            return nome_fonte, tamanho_fonte
    finally:
        return nome_fonte, tamanho_fonte


class InsereProtocolo(QDialog):
    def __init__(self, pix_id, nome, valor, caixa):
        self.db_pix = DataBasePix(HOSTNAME, DATABASE, USERNAME, PWD, PORT_ID)
        QDialog.__init__(self)
        self.ui = Ui_Dialog_Protocolo()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.pix_id = pix_id
        self.ui.label_id_pix_protocolo.setText(f'ID Pix: {pix_id}')
        self.ui.label_caixa_protocolo.setText(f'Usuário: {caixa.upper()}')
        self.ui.label_nome_protocolo.setText(f'Nome: {nome}')
        self.ui.label_valor_protocolo.setText(f'Valor: {valor}')
        self.show()
        self.ui.btn_cancelar_protocolo.clicked.connect(lambda: self.sair_insere_protocolo())
        self.ui.btn_gravar_protocolo.clicked.connect(
            lambda: self.confirma_protocolo(self.pix_id, self.ui.campo_ano_certidao.text(),
            self.ui.campo_num_certidao.text(), self.ui.campo_num_protocolo.text()))
        self.ui.campo_num_protocolo.returnPressed.connect(
            lambda: self.confirma_protocolo(self.pix_id, self.ui.campo_num_protocolo.text()))

    
    def sair_insere_protocolo(self):
        self.done(0)
        self.close()

    def confirma_protocolo(self, pix_id, ano, numcert, numprot):
        int_ano = 0
        int_numcert = 0
        int_numprot = 0
        # Converter o texto dos campos em número, 
        if ano == '':
            int_ano = 0
        else:
            try:
                int_ano = int(ano)
            except:
                int_ano = -1
                print('Número inválido')
        
        if numcert == '':
            int_numcert = 0
        else:
            try:
                int_numcert = int(numcert)
            except:
                int_numcert = -1
                print('Número inválido')
        
        if numprot == '':
            int_numprot = 0
        else:
            try:
                int_numprot = int(numprot)
            except:
                int_numprot = -1
        
        try:
            self.db_pix.insertPixNumInterno(pix_id, int_ano, int_numcert, int_numprot)
        except Exception as error:
            print(f'Erro ao gravar protocolo: {error}')
            self.done(0)
            self.close()
        else:
            self.done(1)
            self.close()


class ConfirmaPix(QDialog):
    def __init__(self, pix_id, nome, valor, caixa):
        self.db = DataBaseUsers(DBNAME)
        QDialog.__init__(self)
        self.ui = Ui_Dialog_Confirma_Pix()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_id_pix.setText(f'ID Pix: {pix_id}')
        self.ui.label_caixa.setText(f'Usuário: {caixa.upper()}')
        self.ui.label_nome.setText(f'Nome: {nome}')
        self.ui.label_valor.setText(f'Valor: {valor}')
        self.show()
        self.ui.btn_cancela_libera.clicked.connect(lambda: self.sair_confirma_pix())
        self.ui.btn_confirma_libera.clicked.connect(
            lambda: self.confirma_pix(caixa, self.ui.campo_senha_libera.text()))
        self.ui.campo_senha_libera.returnPressed.connect(
            lambda: self.confirma_pix(caixa, self.ui.campo_senha_libera.text()))

    
    def sair_confirma_pix(self):
        self.done(0)
        self.close()

    def confirma_pix(self, sigla, senha):
        _, acesso = self.db.check_users(sigla.lower(), senha)
        self.ui.label_incorrect_user.clear()
        if acesso == 'incorretas':
            self.ui.label_incorrect_user.setText('Senha incorreta!')
        else:
            print('Senha correta')
            self.done(1)
            self.close()


class LoginWindow(QWidget):
    def __init__(self, parent=None):
        self.db = DataBaseUsers(DBNAME)
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.show()
        self.ui.campo_senha.returnPressed.connect(lambda: self.efetuar_login())
        self.ui.sair.clicked.connect(lambda: self.sair_login())
        self.ui.btn_login.clicked.connect(lambda: self.efetuar_login())
    
    def sair_login(self):
        self.close()
        app.exit()
    
    def efetuar_login(self):       
        usuario = self.ui.campo_usuario.text()
        senha = self.ui.campo_senha.text()
        username, acesso = self.db.check_users(usuario.lower(), senha)
        self.ui.label_incorrect_user.clear()
        if acesso == 'incorretas':
            self.ui.label_incorrect_user.setText('Senha ou usuário incorreto!')
        else:
            self.window = MainWindow(usuario=username, acesso=acesso, sigla=usuario)
            self.window.show()
            self.close()


#  Passar a classe __init__ com self, user
#  Se user for caixa, self.ui.btn_cadastrar.setVisible(False)
class MainWindow(QMainWindow):
    def __init__(self, usuario, acesso, sigla):
        self.db = DataBaseUsers(DBNAME)
        self.db_pix = DataBasePix(HOSTNAME, DATABASE, USERNAME, PWD, PORT_ID)
        self.usuario = usuario
        self.acesso = acesso
        self.sigla = sigla
        pix_icone = QIcon(r'C:\SisPag Pix\gui\icons\pix_icon.png')
        self.tx_id_pix = ''
        self.main_window_id_pix = ''
        locale.setlocale(locale.LC_ALL, LOCALE)
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SisPag PIX - 2RGI")
        self.tema_atual = Tema(TEMA)
        nome_fonte, tamanho_fonte = carrega_fonte_config()
        self.fontTable = QFont(nome_fonte, tamanho_fonte)
        self.setWindowIcon(pix_icone)
        ##########################
        global window_obj
        window_obj = self.ui
        ##########################

        dia = QDate()
        try:
            aa, mm, dd = dia_corrente()
        except Exception as error:
            print(f'Erro ao recuperar dia{error}')
            aa = 2023
            mm = 1
            dd = 1
        finally:
            dia.setDate(aa, mm, dd)
            self.data_pix_padrão = str(dd)+'/'+str(mm)+'/'+str(aa)
        
        # Definir o dia base para ser exibido no filtro de consulta/libera pix
        self.ui.filtro_dia_alterapix.setDate(dia)
        self.ui.filtro_data_consultapix.setDate(dia)
        self.ui.filtro_dia_gera_excel.setDate(dia)

        # Timer que irá verificar recursivamente por pagamentos pix pagos
        self.pix_counter = self.db_pix.search_pix_status(self.sigla, self.data_pix_padrão, 'pago')
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.consulta_novo_pix_pago(self.pix_counter))
        self.timer.start(3000)

        # Clicando na notificação mostra a janela (se estiver oculta) e entra no consulta pix
        tray.messageClicked.connect(lambda: self.showNormal())
        tray.messageClicked.connect(lambda: self.tela_consultar())

        # Verificar o nível de acesso do usuário para definir quais telas serão exibidas.
        self.verifica_acesso()
        
        # Ações de esconder e exibir a janela
        action_hide.triggered.connect(lambda: self.hide())
        action_show.triggered.connect(lambda: self.showNormal())

        # Recolher e expandir menu lateral
        self.ui.menu.clicked.connect(lambda: self.slide_left_menu())
        
        # Exibir usuário logado
        self.ui.campo_usuario_atual.setText(f"Usuário: {self.usuario}")

        # Acesso dos Widgets e suas respectivas páginas
        self.ui.gerar_qr_code.clicked.connect(lambda: self.tela_gerar_qr_code())
        self.ui.imprimir.clicked.connect(lambda: self.tela_imprimir())
        self.ui.consulta_pgto.clicked.connect(lambda: self.tela_consultar())
        self.ui.cadastrar_usuario.clicked.connect(lambda: self.tela_cadastrar_usuario())
        self.ui.autorizar_pix.clicked.connect(lambda: self.tela_autorizar_pix())
        self.ui.settings.clicked.connect(lambda: self.tela_settings())


        # Ações da tela de gerar QrCode
        self.ui.campo_cpf_apresentante.returnPressed.connect(
            lambda: self.busca_solicitante(self.ui.campo_cpf_apresentante.text()))
        self.ui.btn_cadastrar_solicitante.clicked.connect(
            lambda: self.cadastra_solicitante(self.ui.campo_cpf_apresentante.text(),
            self.ui.campo_apresentante.text()))
        self.ui.btn_gerar_qrcode.clicked.connect(
            lambda: self.gera_qr_code(self.ui.campo_apresentante.text(), 
            self.ui.campo_valor.text(), self.ui.campo_cpf_apresentante.text()))
        self.ui.btn_limpar_campos.clicked.connect(lambda: self.limpar_campos_qr_code())
        self.ui.btn_enviar_email.clicked.connect(lambda: self.envia_email_solicitante(
            nome_solicitante=self.ui.campo_apresentante.text(),
            email_solicitante=self.ui.campo_email_solicitante.text()
        ))


        # Ações da tela de imprimir QrCode
        self.ui.btn_buscar_imprimir.clicked.connect(
            lambda: self.buscar_imprimir_pix(self.ui.campo_txt_id_imprimir_pix.text()))
        self.ui.btn_imprimir.clicked.connect(
            lambda: self.imprimir_pix()
        )


        # Ações da tela de cadastro
        self.ui.btn_cadastrar.clicked.connect(lambda: self.cadastra_usuario())
        self.ui.btn_cancelar.clicked.connect(lambda: self.limpar_campos_cadastro())
        self.ui.sair.clicked.connect(lambda: self.sair_sistema())


        # Ações da tela de consulta pix
        self.ui.btn_set_big_font_consulta.clicked.connect(
            lambda: self.muda_fonte_tabela_pix())
        self.ui.btn_buscar_consulta_pix.clicked.connect(
            lambda: self.carregar_consulta(self.sigla))
        self.ui.campo_buscar_apresentante_consulta_pix.returnPressed.connect(
            lambda: self.carregar_consulta(self.sigla))
        self.ui.campo_buscar_id_consulta_pix.returnPressed.connect(
            lambda: self.carregar_consulta(self.sigla))
        self.ui.btn_inser_num_interno_consulta_pix.clicked.connect(
            lambda: self.insere_protocolo_pix_selecionado())
        # Se o usuário escolher uma data, automaticamente muda-se o filtro de data
        # de "Todos" para "Data", pois entende-se que o usuário quer uma data específica.
        self.ui.filtro_data_consultapix.dateChanged.connect(
            lambda: self.ui.combo_filtro_data_consultapix.set_current_index(1))


        # Ações da tela de altera Pix
        self.ui.btn_set_big_font.clicked.connect(
            lambda: self.muda_fonte_tabela_pix())
        self.ui.campo_buscar_apresentante.returnPressed.connect(
            lambda: self.carregar_altera_pix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text()))
        self.ui.campo_buscar_id.returnPressed.connect(
            lambda: self.carregar_altera_pix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text()))        
        self.ui.btn_buscar_alteraPix.clicked.connect(
            lambda: self.carregar_altera_pix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text()))
        self.ui.btn_cancelar_altera_pix.clicked.connect(
            lambda: self.limpa_campos_altera_pix())
        self.ui.btn_liberar_pix.clicked.connect(
            lambda: self.altera_pix_selecionado())
        self.ui.filtro_dia_alterapix.dateChanged.connect(
            lambda: self.ui.combo_filtro_data_alterapix.set_current_index(1))


        # Ações de configurações do sistema (settings)
        self.ui.combo_tema.activated.connect(lambda: 
                self.tema_atual.escolher_tema(self.ui.combo_tema.currentText()))
        self.ui.btn_aplicar_tema.clicked.connect(lambda: self.aplica_tema(self.tema_atual))
        self.ui.btn_gera_excel.clicked.connect(lambda: self.gravar_planilha_excel())
        self.show()

        if TEMA != 'Drcl Night':
            self.tema_atual.escolher_tema(TEMA)
            self.aplica_tema(self.tema_atual)


    def consulta_novo_pix_pago(self, quant_atual):
        quant_pix_pagos = self.db_pix.search_pix_status(self.sigla, self.data_pix_padrão, 'pago')
        if quant_pix_pagos > quant_atual:
            show_tray_message(self, tray, 'Novo Pix pago!', 'Um novo pix foi pago pela parte!')
            self.pix_counter = quant_pix_pagos


    def encerra_sistema(self):
        msg_solicitante = QMessageBox()
        msg_solicitante.setIcon(QMessageBox.Warning)
        msg_solicitante.setWindowTitle('Encerrado por inatividade.')
        msg_solicitante.setText('Será necessário fechar e entrar novamente no sistema.')
        msg_solicitante.exec_()
        sys.exit('Encerrado por inatividade.')


    def envia_email_solicitante(self, nome_solicitante, email_solicitante):
        if nome_solicitante == '' or email_solicitante == '':
            msg_solicitante = QMessageBox()
            msg_solicitante.setIcon(QMessageBox.Warning)
            msg_solicitante.setWindowTitle('Erro ao preparar e-mail')
            msg_solicitante.setText('É necessário informar nome e email do apresentante')
            msg_solicitante.exec_()
        else:
            if verifica_email(email_solicitante):
                copiaECola = self.db_pix.get_copia_cola(self.tx_id_pix)
                
                # Verifica se a conexão do banco foi encerrada por inatividade.
                if copiaECola == 'conexão encerrada':
                    self.encerra_sistema()

                if copiaECola != 'erro':
                    status = mail_rgi.envia_email(
                        nome_dest=nome_solicitante,
                        email_dest=email_solicitante,
                        anexo=ADOBE_PDF_FILE,
                        pix_copia_e_cola=self.db_pix.get_copia_cola(self.tx_id_pix)
                    )
                    if status == 'sucesso':
                        msg_solicitante = QMessageBox()
                        msg_solicitante.setIcon(QMessageBox.Warning)
                        msg_solicitante.setWindowTitle('Sucesso no envio')
                        msg_solicitante.setText(f'E-mail enviado com sucesso para: "{email_solicitante}"')
                        msg_solicitante.exec_()
                        self.limpar_campos_qr_code()
                    else:
                        msg_solicitante = QMessageBox()
                        msg_solicitante.setIcon(QMessageBox.Warning)
                        msg_solicitante.setWindowTitle('Erro ao enviar e-mail')
                        msg_solicitante.setText(f'''
    Houve um erro ao enviar o e-mail para: {email_solicitante}.
    Verificar e tentar novamente!


    Erro: {status}''')
                        msg_solicitante.exec_()
                else:
                    msg_solicitante = QMessageBox()
                    msg_solicitante.setIcon(QMessageBox.Warning)
                    msg_solicitante.setWindowTitle('Erro ao recuperar pix copia e cola')
                    msg_solicitante.setText('É necessário gerar o QrCode antes de enviar o e-mail.')
                    msg_solicitante.exec_()
                    return
            else:
                msg_solicitante = QMessageBox()
                msg_solicitante.setIcon(QMessageBox.Warning)
                msg_solicitante.setWindowTitle('Erro ao preparar e-mail')
                msg_solicitante.setText('O e-mail informado está num formato inválido.')
                msg_solicitante.exec_()


    def cadastra_solicitante(self, cpf_cnpj, nome_solicitante):
        if cpf_cnpj != '' and nome_solicitante != '':
            cpf_cnpj_formatado = formata_cpf_cnpj(cpf_cnpj)
            resultado = self.db_pix.insert_solicitante(cpf_cnpj_formatado, nome_solicitante)
            
            # Verifica se a conexão do banco foi encerrada por inatividade.
            if resultado == 'conexão encerrada':
                    self.encerra_sistema()

            if resultado == 'inserido':
                msg_solicitante = QMessageBox()
                msg_solicitante.setIcon(QMessageBox.Warning)
                msg_solicitante.setWindowTitle('Inserido com sucesso!')
                msg_solicitante.setText('O cadastro foi efetuado com sucesso.')
                msg_solicitante.exec_()
            elif resultado == 'existente':
                solicitante = self.db_pix.busca_solicitante(cpf_cnpj_formatado)
                self.ui.campo_apresentante.setText(solicitante[1])
                msg_solicitante = QMessageBox()
                msg_solicitante.setIcon(QMessageBox.Warning)
                msg_solicitante.setWindowTitle('Solicitante já existente')
                msg_solicitante.setText('Não há necessidade de cadastrar!')
                msg_solicitante.exec_()
            else:
                msg_solicitante = QMessageBox()
                msg_solicitante.setIcon(QMessageBox.Warning)
                msg_solicitante.setWindowTitle('Erro ao cadastrar')
                msg_solicitante.setText(f'Não foi possível cadastrar {resultado}')
                msg_solicitante.exec_()
        else:
            msg_solicitante = QMessageBox()
            msg_solicitante.setIcon(QMessageBox.Warning)
            msg_solicitante.setWindowTitle('Dados incompletos...')
            msg_solicitante.setText('Favor digitar CPF e Nome para cadastrar!')
            msg_solicitante.exec_()


    def busca_solicitante(self, cpf_cnpj):
        if len(cpf_cnpj) == 11:
            erro, _ = verifica_cpf(cpf_cnpj)
            if not erro:
                cpf_cnpj_formatado = formata_cpf_cnpj(cpf_cnpj)
                solicitante = self.db_pix.busca_solicitante(cpf_cnpj_formatado)
                
                # Verifica se a conexão do banco foi encerrada por inatividade.
                if solicitante == 'conexão encerrada':
                    self.encerra_sistema()

                if solicitante != None:
                    self.ui.campo_apresentante.setText(solicitante[1])
                    print(solicitante[1])
                else:
                    msg_solicitante = QMessageBox()
                    msg_solicitante.setIcon(QMessageBox.Warning)
                    msg_solicitante.setWindowTitle('Solicitante não encontrado!')
                    msg_solicitante.setText(f'Informe o nome e clique no botão cadastrar')
                    msg_solicitante.exec_()
                
            else:
                msg_solicitante = QMessageBox()
                msg_solicitante.setIcon(QMessageBox.Warning)
                msg_solicitante.setWindowTitle('CPF inválido')
                msg_solicitante.setText(f'O CPF digitádo é inválido')
                msg_solicitante.exec_()
        elif len(cpf_cnpj) == 14:
            erro, _ = verifica_cpf(cpf_cnpj)
            if not erro:
                cpf_cnpj_formatado = formata_cpf_cnpj(cpf_cnpj)
                solicitante = self.db_pix.busca_solicitante(cpf_cnpj_formatado)
                if solicitante != None:
                    self.ui.campo_apresentante.setText(solicitante[1])
                    print(solicitante[1])
                else:
                    msg_solicitante = QMessageBox()
                    msg_solicitante.setIcon(QMessageBox.Warning)
                    msg_solicitante.setWindowTitle('Solicitante não encontrado!')
                    msg_solicitante.setText(f'Informe o nome e clique no botão cadastrar')
                    msg_solicitante.exec_()
            else:
                msg_solicitante = QMessageBox()
                msg_solicitante.setIcon(QMessageBox.Warning)
                msg_solicitante.setWindowTitle('CNPJ inválido')
                msg_solicitante.setText(f'O CNPJ digitádo é inválido')
                msg_solicitante.exec_()
        else:
            msg_solicitante = QMessageBox()
            msg_solicitante.setIcon(QMessageBox.Warning)
            msg_solicitante.setWindowTitle('CPF/CNPJ inválido')
            msg_solicitante.setText(f'O CPF/CNPJ digitádo é inválido')
            msg_solicitante.exec_()


    def gravar_planilha_excel(self):
        if self.ui.combo_filtro_gera_excel.currentIndex() == 0:
            estado_gera_excel = ''
        elif self.ui.combo_filtro_gera_excel.currentIndex() == 1:
            estado_gera_excel = 'aguardando'
        else:
            estado_gera_excel = 'pago'
        relatorio = self.db_pix.search_pix_by_name( apresentante='', 
                                                limite=100, 
                                                filtro=estado_gera_excel, 
                                                filtro_data='Data',
                                                data=self.ui.filtro_dia_gera_excel.text()
                                                )
        
        # Verifica se a conexão do banco foi encerrada por inatividade.
        if relatorio == 'conexão encerrada':
            self.encerra_sistema()

        colunas = ['PixID', 'Nome', 'Valor', 'Caixa', 'Situação', 'Liberado', 'Ano', 'NumCert', 'NumProt']
        self.planilha = xlsx.Planilha(nomeplanilha='relatorio.xlsx', linhas=(len(relatorio)+2))
        self.planilha.criar_cabecalho(colunas)
        
        if estado_gera_excel == '':
            self.planilha.criar_titulo('Relatório de Pagamentos pix do dia: ' + self.ui.filtro_dia_gera_excel.text() + ' - (Todos)')
        elif estado_gera_excel == 'aguardando':
            self.planilha.criar_titulo('Relatório de Pagamentos pix do dia: ' + self.ui.filtro_dia_gera_excel.text() + ' - (Aguardando)')
        else:
            self.planilha.criar_titulo('Relatório de Pagamentos pix do dia: ' + self.ui.filtro_dia_gera_excel.text() + ' - (Pagos)')
        
        linha_atual = 4
        soma_taxas = Decimal(0)
        for pgto in relatorio:
            self.planilha.escrever(f'A{linha_atual}', pgto[0], False, False)
            self.planilha.escrever(f'B{linha_atual}', pgto[1], False, False)
            self.planilha.escrever(f'C{linha_atual}', pgto[2], False, valor=True)
            self.planilha.escrever(f'D{linha_atual}', pgto[3], False, False)
            self.planilha.escrever(f'E{linha_atual}', pgto[5], False, False)
            self.planilha.escrever(f'F{linha_atual}', pgto[6], False, False)
            self.planilha.escrever(f'G{linha_atual}', pgto[7], False, False)
            self.planilha.escrever(f'H{linha_atual}', pgto[8], False, False)
            self.planilha.escrever(f'I{linha_atual}', pgto[9], False, False)
            if pgto[5] == 'pago':
                valor = Decimal(pgto[2])
                percentual = Decimal(PERCENTUAL)
                tx_minima = Decimal(TAXA_MINIMA)
                tx_maxima = Decimal(TAXA_MAXIMA)
                taxa = valor * percentual # Multiplica pelo percentual definido no arquivo config.ini
                if taxa < tx_minima:
                    taxa = tx_minima # esse é o valor mínimo definido no arquivo config.ini
                elif taxa > tx_maxima:
                    taxa = tx_maxima # esse é o valor máximo definido no arquivo config.ini
                else:
                    # se o valor estiver entre as taxas mínimas e máxima, não fazer nada.
                    pass 
                soma_taxas = soma_taxas + taxa
            linha_atual += 1
        self.planilha.escrever(f'B{linha_atual+1}', 'Total das taxas de serviço PIX', negrito=True, valor=False)
        self.planilha.escrever(f'C{linha_atual+1}', soma_taxas, negrito=True, valor=True)
        try:
            self.planilha.fecha_planilha()
        except Exception as erro:
            msg_solicitante = QMessageBox()
            msg_solicitante.setIcon(QMessageBox.Warning)
            msg_solicitante.setWindowTitle('Erro ao salvar')
            msg_solicitante.setText(f'O relatório Excel deve estar aberto/em uso, fechar e tentar novamente\n{erro}')
            msg_solicitante.exec_()
        else:
            msg_solicitante = QMessageBox()
            msg_solicitante.setIcon(QMessageBox.Warning)
            msg_solicitante.setWindowTitle('Relatório gerado com sucesso')
            msg_solicitante.setText(f'O relatório se encontra na pasta: C:\SysPg Pix')
            msg_solicitante.exec_()

    # # Função para procurar pix aguardando pagamento para verificação manual
    # def send_message(self, message: str):
    #     quant_pix_atual = self.db_pix.search_pix_status(self.sigla, self.data_pix_padrão, 'aguardando')
    #     if self.ui.autorizar_pix.isVisible():
    #         if quant_pix_atual > self.pix_counter:
    #             self.pix_counter = quant_pix_atual
    #             self.timer.stop()
    #             show_tray_message(self, tray, 'Novo Pix!', 'Há um novo Pix aguardando pagamento...' )
    #             self.carregar_altera_pix('','')
    #             self.timer.start(1000)


    def buscar_imprimir_pix(self, id):
        txt_id = self.db_pix.get_txt_id(id)
        copia_e_cola = self.db_pix.get_copia_cola(txt_id)
        if id == '':
            msg_imprimir = QMessageBox()
            msg_imprimir.setIcon(QMessageBox.Warning)
            msg_imprimir.setWindowTitle('Informar ID')
            msg_imprimir.setText(f'Para buscar e imprimir é necessário informar o ID do Pix.')
            msg_imprimir.exec_()
        else:
            pix = self.db_pix.search_pix_by_id(pix_id=id)
            
            # Verifica se a conexão do banco foi encerrada por inatividade.
            if pix == 'conexão encerrada':
                self.encerra_sistema()

            if pix != None:
                nomeApresentante = pix[1]
                valor = pix[2]
                erro_pix = False
                print("Gerar QrCode para impressão")
                pgto = Pagamento(id_tx=str(id),
                            nome=nomeApresentante,
                            valor=valor,
                            copia_cola=copia_e_cola)
                reais = self.converter_float_reais(pgto.valor)
                # Validar dados antes de gerar QRCode/PDF e gravar no banco
                
                if not erro_pix:
                    # Gerar QrCode com os dados preenchidos.
                    qr = qrcode.make(pgto.copia_cola)
                    qr.save(r'C:\SisPag Pix\src\pixqrcode.png')
                    
                    self.ui.txt_id_pix.setText(f"ID Pix: {pgto.id_tx}")

                    # verificar erro
                    # #print(rgi.Nome, pgto.nome, rgi.ChavePix, pgto.valor, rgi.Cidade, pgto.id_tx)
                    # payload = Payload(RGI_NOME, pgto.nome, RGI_CHAVE_PIX, valor_str, RGI_CIDADE, pgto.id_tx)
                    # pixCopiaCola = payload.gerarPayload()
                    # pgto.copia_cola = pixCopiaCola

                    # Gerar Arquivo PDF com os dados + QrCode
                    pdf = PDF()
                    pdf.print_chapter(pgto.nome, reais, pgto.id_tx, pgto.copia_cola)
                    # Caso o PDF de impressão do QRCode já esteja aberto (ex. O usuário esqueceu de fechar
                    # na geração anterior, o sistema não conseguirá gravar o arquivo pois o windows gera erro
                    # de permissão ao criar e gravar novo arquivo com um de mesmo nome e local já aberto
                    # para evitar um precoce fim do processo de geração, utilizo um arquivo "extra" que nada
                    # mais é do que o mesmo arquivo, com nome diferente no mesmo local, para seguir com a impressão.
                    try:
                        pdf.output(ADOBE_PDF_FILE, 'F')
                    except Exception as error:
                        msg_erro = QMessageBox()
                        msg_erro.setIcon(QMessageBox.Warning)
                        msg_erro.setWindowTitle('Erro ao gerar arquivo PDF')
                        msg_erro.setText(f'Após imprimir, sempre feche todas as abas e PDFs abertos, para evitar erros.\n{error}')
                        msg_erro.exec_()
                        try:
                            pdf.output(ADOBE_PDF_FILE_EXTRA, 'F')
                        except Exception as error:
                            msg_erro = QMessageBox()
                            msg_erro.setIcon(QMessageBox.Warning)
                            msg_erro.setWindowTitle('Falha geral na criação do PDF')
                            msg_erro.setText(f'Fechar o Adobe e todas as suas abas e gerar novo QRCode.\n{error}')
                            msg_erro.exec_()
                        else:
                            # Abrir arquivo PDF de backup com nome diferente pois já tem um com nome igual aberto.
                            cmd = '"{}" "{}"'.format(ADOBE_READER, ADOBE_PDF_FILE_EXTRA)
                            subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    else:
                        # No caso de nenhum erro na criação, abrir arquivo PDF para conferência dos dados
                        cmd = '"{}" "{}"'.format(ADOBE_READER, ADOBE_PDF_FILE)
                        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                self.erro_dados_pix('O Código IDPix informado, não foi encontrado.')


    def imprimir_pix(self):
        # Abrir qrquivo PDF para conferência dos dados
        cmd = '"{}" /p "{}"'.format(ADOBE_READER, ADOBE_PDF_FILE)
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def verifica_prot_cert_pix(self, pagamentoPix):
        if pagamentoPix[6] == None or pagamentoPix[6] == '':
            if pagamentoPix[7] == None or pagamentoPix[7] == '':
                if pagamentoPix[8] == None or pagamentoPix[8] == '':
                    return False
        return True

    def insere_protocolo_pix_selecionado(self):
        coluna_id = self.ui.table_consulta_pix.selectedIndexes()[0]
        coluna_nome = self.ui.table_consulta_pix.selectedIndexes()[1]
        coluna_valor = self.ui.table_consulta_pix.selectedIndexes()[2]
        coluna_status = self.ui.table_consulta_pix.selectedIndexes()[4]

        id = self.ui.table_consulta_pix.model().data(coluna_id)
        apresentante = self.ui.table_consulta_pix.model().data(coluna_nome)
        valor = self.ui.table_consulta_pix.model().data(coluna_valor)
        status = self.ui.table_consulta_pix.model().data(coluna_status)

        pix_selecionado = self.db_pix.search_pix_by_id(id)
        
        # Verifica se a conexão do banco foi encerrada por inatividade.
        if pix_selecionado == 'conexão encerrada':
            self.encerra_sistema()
        
        if self.verifica_prot_cert_pix(pix_selecionado):
            msg_pix = QMessageBox()
            msg_pix.setWindowTitle(f'Protocolo/Certidão já informado: {pix_selecionado[0]}')
            msg_pix.setText(f'Atenção o Pix já tem nº de certidão e/ou protocolo informados, confirmar o pix selecionado!')
            msg_pix.exec_()

        if status == 'pago':
            self.dialog = InsereProtocolo(pix_id=id, nome=apresentante, valor=valor, caixa=self.sigla)
            confirma_protocolo = self.dialog.exec_()
            self.dialog.close()
            if confirma_protocolo == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Cadastrado com sucesso!')
                msg.setText(f'O nº de Protocolo/Certidão foi inserido com sucesso!')
                msg.exec_()
                self.carregar_consulta(self.sigla)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Pix não está pago')
            msg.setText(f'Só é possível inserir protocolo em pix com status pago!')
            msg.exec_()


    def altera_pix_selecionado(self):
        coluna_id = self.ui.table_busca_e_autoriza_pix.selectedIndexes()[0]
        coluna_nome = self.ui.table_busca_e_autoriza_pix.selectedIndexes()[1]
        coluna_valor = self.ui.table_busca_e_autoriza_pix.selectedIndexes()[2]

        id = self.ui.table_busca_e_autoriza_pix.model().data(coluna_id)
        apresentante = self.ui.table_busca_e_autoriza_pix.model().data(coluna_nome)
        valor = self.ui.table_busca_e_autoriza_pix.model().data(coluna_valor)
        pix_selecionado = self.db_pix.search_pix_by_id(id)

        # Verifica se a conexão do banco foi encerrada por inatividade.
        if pix_selecionado == 'conexão encerrada':
            self.encerra_sistema()

        if pix_selecionado[5] == 'pago':
            msg_pix = QMessageBox()
            msg_pix.setWindowTitle(f'Pix selecionado: {pix_selecionado[0]}')
            msg_pix.setText('O pix informado já está pago!')
            msg_pix.exec_()
        else:         
            self.dialog = ConfirmaPix(pix_id=id, nome=apresentante, valor=valor, caixa=self.sigla)
            senhaAutorizaPixOk = self.dialog.exec_()
            self.dialog.close()
            if senhaAutorizaPixOk == 1:
                try:
                    self.db_pix.update_pix(pix_id=id, updated_by=self.sigla, status='pago')
                except Exception as error:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle('Erro ao liberar o Pix')
                    msg.setText(f'O Pix de ID: {id} não foi liberado!')
                    print(error)
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle('Pix Liberado!')
                    msg.setText(f'O Pix de ID: {id} foi liberado com sucesso!')
                    msg.exec_()
                    self.carregar_altera_pix('','')
        

    def limpa_campos_altera_pix(self):
        self.ui.campo_buscar_id.setText('')
        self.ui.campo_buscar_apresentante.setText('')
        self.ui.table_busca_e_autoriza_pix.setRowCount(0)
        self.ui.table_busca_e_autoriza_pix.clearContents()
        self.ui.table_busca_e_autoriza_pix.clearSpans()
        self.ui.resultado_busca_autoriza.clear()
        self.ui.table_busca_e_autoriza_pix.setSortingEnabled(False)


    def verifica_acesso(self):
        if self.acesso.lower() == 'administrador':
            # Inicializar a MainWindow do App na tela de autorizar pix.
            self.ui.cadastrar_usuario.setVisible(True)
            self.tela_cadastrar_usuario()
            # Na fase de desenvolvimento o usuário administrador terá acesso à todas as telas
            # self.ui.autorizar_pix.setVisible(False)
            # self.ui.gerar_qr_code.setVisible(False)
            # self.ui.consulta_pgto.setVisible(False)
            # self.ui.imprimir.setVisible(False)

        elif self.acesso.lower() == 'contabilidade':
            # Inicializar a MainWindow do App na tela de autorizar pix.
            self.ui.autorizar_pix.setVisible(True)
            self.tela_autorizar_pix()
            self.ui.cadastrar_usuario.setVisible(False)
            self.ui.gerar_qr_code.setVisible(False)
            self.ui.consulta_pgto.setVisible(False)
            self.ui.imprimir.setVisible(False)

        else:
            # Inicializar a MainWindow do App na tela de geração de Qr Code.
            self.tela_gerar_qr_code()
            self.ui.campo_usuario_atual.setText(f"Usuário: {self.usuario}")
            self.ui.cadastrar_usuario.setVisible(False)
            self.ui.autorizar_pix.setVisible(False)
            self.ui.filtro_dia_gera_excel.setVisible(False)
            self.ui.combo_filtro_gera_excel.setVisible(False)
            self.ui.label_gera_relatorio.setText('Função desabilitada para o usuário.')
            self.ui.btn_gera_excel.setVisible(False)
            self.ui.label_status.setVisible(False)


    def aplica_tema(self, tema_atual: Tema):
    
        self.ui.right_panel.setStyleSheet('''*{
        background-color: rgb'''+f'{(tema_atual.rightside_menu_bg_color)}'+''';
        font: 14pt "MS Shell Dlg 2";
        }

        QDateEdit {
            border: 2px solid rgb'''+f'{(tema_atual.cor_destaque_1)}'+''';
            color: rgb'''+f'{(tema_atual.main_text_color)}'+''';
            font: 13pt "MS Shell Dlg 2";
            padding: 5px;
            border-radius: 5px
        }

        QPushButton {
            color: rgb'''+f'{(tema_atual.btn_text_color)}'+''';
            background-color: rgb'''+f'{(tema_atual.btn_bg_color)}'+''';
            border: 0px solid;
            padding: 6px 9px;
            text-align:center;
            border-radius:5px;
            font: 16pt "MS Shell Dlg 2"
        }

        QPushButton:hover {
            color: rgb'''+f'{(tema_atual.left_menu_text_color)}'+''';
            background-color: rgb'''+f'{(tema_atual.btn_bg_color_hover)}'+''';
            text-align:center;
            padding: 6px 9px;
            border-radius:5px;
            font: 16pt "MS Shell Dlg 2"
        }

        QPushButton:pressed {
            border: 2px solid rgb'''+f'{(tema_atual.rightside_menu_bg_color)}'+''';
            background-color: rgb'''+f'{(tema_atual.btn_pressed_color)}'+''';
            color: rgb'''+f'{(tema_atual.btn_pressed_text)}'+''';
            text-align:center;
            padding: 5px 7px;
            border-radius:5px;
            font: 15pt "MS Shell Dlg 2"
        }

        QLineEdit{
            background: transparent;
            border: none;
            border-bottom:3px solid rgba'''+f'{(tema_atual.input_text_bg_color)}'+''';
            padding: 5px;
            font: 16pt "MS Shell Dlg 2";
            color: rgb'''+f'{(tema_atual.main_text_color)}'+''';
        }

        QLabel{
            color: rgb'''+f'{(tema_atual.main_text_color)}'+''';
            font: 15pt "MS Shell Dlg 2";
        }
        
        QTableWidget{
            font: 11pt "MS Shell Dlg 2";
            background-color: rgb'''+f'{(tema_atual.table_item_bg_color)}'+''';
            alternate-background-color: rgb'''+f'{(tema_atual.table_item_alt_bg_color)}'+''';
            color: rgb'''+f'{(tema_atual.table_item_text_color)}'+''';
        }

        QComboBox{
            border: 2px solid rgb'''+f'{(tema_atual.cor_destaque_1)}'+''';
            color: rgb'''+f'{(tema_atual.main_text_color)}'+''';
            font: 13pt "MS Shell Dlg 2";
            padding: 5px;
            border-radius: 5px
        }

        QComboBox:drop-down {
            border: 0px	
        }

        QComboBox:down-arrow {
            image: url(:/icons/icons/chevron-down.svg);
            margin-right:10
        }

        QComboBox:on {
            border: 2px solid rgb'''+f'{(tema_atual.main_text_color)}'+''';
        }

        QComboBox QListView {
            color: rgb'''+f'{(tema_atual.main_text_color)}'+''';
            font: 13pt "MS Shell Dlg 2";
            border: 1px solid rgba(0,0,0,10%);
            padding: 5px;
            background-color: rgb'''+f'{(tema_atual.side_menu_hover_bg_color)}'+''';
        }

        QComboBox QListView:item{
            padding-left: 10px;
            background-color: rgb'''+f'{(tema_atual.side_menu_hover_bg_color)}'+''';
        }

        QComboBox QListView:item:hover{
            background-color: rgb'''+f'{(tema_atual.btn_bg_color)}'+''';
        }

        QComboBox QListView:item:selected{
            background-color: rgb'''+f'{(tema_atual.btn_bg_color)}'+''';
        }
        ''')

        self.ui.label_aparencia.setStyleSheet('''
            color: rgb'''+f'{(tema_atual.btn_text_color)}'+''';
            font: 18pt "MS Shell Dlg 2";
            text-decoration: underline;
            background:transparent
        ''')

        self.ui.label_configuracoes.setStyleSheet('''
            color: rgb'''+f'{(tema_atual.btn_text_color)}'+''';
            font: 18pt "MS Shell Dlg 2";
            text-decoration: underline;
            background:transparent  
        ''')

        self.ui.frame_left_base.setStyleSheet('''*{
            background-color: rgb'''+f'{(tema_atual.side_menu_bg_color)}'+''';
            border: 0px solid;
        }
        QPushButton {
            color: rgb'''+f'{(tema_atual.left_menu_text_color)}'+''';
            background-color: rgb'''+f'{(tema_atual.side_menu_bg_color)}'+''';
            border: 0px solid;
            padding: 6px 9px;
            text-align:left;
        }
        QPushButton:hover {
            background-color: rgb'''+f'{(tema_atual.side_menu_hover_bg_color)}'+''';
            text-align:left;
            padding: 6px 9px;
            border-radius:6px;
            border: 2px solid rgb'''+f'{(tema_atual.cor_destaque_1)}'+''';
        }''')

        self.ui.top_center_frame.setStyleSheet('''
            background-color: rgb'''+f'{(tema_atual.side_menu_bg_color)}'+''';
        ''')

        self.ui.label_titulo.setStyleSheet('''
            color: rgb'''+f'{(tema_atual.left_menu_text_color)}'+''';
        ''')
        self.ui.forma_1.setStyleSheet('''
            font: 57 300pt "Marlett";
            color: rgba'''+f'{(tema_atual.forma_color1)}'+''';
        ''')

        self.ui.forma_2.setStyleSheet('''
            font: 57 500pt "Marlett";
            color: rgba'''+f'{(tema_atual.forma_color1)}'+''';
            background: transparent;
        ''')

        self.ui.forma_3.setStyleSheet('''
            font: 600pt "Wingdings 3";
            color: rgba'''+f'{(tema_atual.forma_color2)}'+''';
            background: transparent;
        ''')

        self.ui.forma_4.setStyleSheet('''
            font: 700pt "Wingdings 3";
            color: rgba'''+f'{(tema_atual.forma_color2)}'+''';
            background: transparent;
        ''')

        self.ui.forma_5.setStyleSheet('''
            font: 700pt "Wingdings 3";
            color: rgba'''+f'{(tema_atual.forma_color2)}'+''';
            background: transparent;
        ''')

        self.ui.forma_6.setStyleSheet('''
            font: 57 300pt "Marlett";
            color: rgba'''+f'{(tema_atual.forma_color1)}'+''';
            background: transparent;
        ''')

        self.ui.forma_7.setStyleSheet('''
            font: 600pt "Wingdings 3";
            color: rgba'''+f'{(tema_atual.forma_color2)}'+''';
            background: transparent;
        ''')

        self.ui.forma_8.setStyleSheet('''
            font: 57 500pt "Marlett";
            color: rgba'''+f'{(tema_atual.forma_color1)}'+''';
            background: transparent;
        ''')

        self.ui.top_left_frame.setStyleSheet('''
            background-color: rgb'''+f'{(tema_atual.side_menu_bg_color)}'+''';
        ''')

        self.ui.label_creditos.setStyleSheet('''
            color: rgb'''+f'{(tema_atual.main_text_color)}'+''';
            font: 10pt "MS Shell Dlg 2";
        ''')
        
        config['APARENCIA']['TEMA'] = tema_atual.nome_tema
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        self.tela_settings()
                                           

    def sair_sistema(self):
        self.db.close_users()
        self.db_pix.close_db()
        self.close()
        app.exit()


    def tela_autorizar_pix(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_autorizar)

        # Definir largura das colunas
        self.ui.table_busca_e_autoriza_pix.setColumnWidth(0, 130)
        self.ui.table_busca_e_autoriza_pix.setColumnWidth(1, 270)
        self.ui.table_busca_e_autoriza_pix.setColumnWidth(2, 155)
        self.ui.table_busca_e_autoriza_pix.setColumnWidth(3, 90)
        self.ui.table_busca_e_autoriza_pix.setColumnWidth(4, 157)
        self.ui.table_busca_e_autoriza_pix.setColumnWidth(5, 107)
        self.ui.table_busca_e_autoriza_pix.setColumnWidth(6, 100)

        # Carregar últimos registros após preparar tabela
        self.carregar_altera_pix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text())

        # Destacar o menu selecionado no momento
        self.ui.autorizar_pix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            border: 2px solid rgb'''+f'{(self.tema_atual.cor_destaque_1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.gerar_qr_code.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')                                
        self.ui.imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.consulta_pgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.cadastrar_usuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def tela_gerar_qr_code(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_gerar)

        # Destacar o menu selecionado no momento
        self.ui.gerar_qr_code.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            border: 2px solid rgb'''+f'{(self.tema_atual.cor_destaque_1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.consulta_pgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.cadastrar_usuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.autorizar_pix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def tela_imprimir(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_imprimir)

        # Destacar o menu selecionado no momento
        self.ui.imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            border: 2px solid rgb'''+f'{(self.tema_atual.cor_destaque_1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.gerar_qr_code.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.consulta_pgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.cadastrar_usuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.autorizar_pix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def tela_consultar(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_consultar)
        self.ui.table_consulta_pix.setColumnWidth(0, 90)
        self.ui.table_consulta_pix.setColumnWidth(1, 310)
        self.ui.table_consulta_pix.setColumnWidth(2, 140)
        self.ui.table_consulta_pix.setColumnWidth(3, 115)
        self.ui.table_consulta_pix.setColumnWidth(4, 210)      
        self.carregar_consulta(self.sigla)
        # Destacar o menu selecionado no momento
        self.ui.consulta_pgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            border: 2px solid rgb'''+f'{(self.tema_atual.cor_destaque_1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.gerar_qr_code.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.cadastrar_usuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.autorizar_pix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def tela_settings(self):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)

            # Destacar o menu selecionado no momento
            self.ui.settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
                                                background-color: rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                                border: 2px solid rgb'''+f'{(self.tema_atual.cor_destaque_1)}'+''';
                                                padding: 6px 9px;
                                                text-align:left;
                                                border-radius:6px;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
                                                background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                                border: 0px solid;
                                                padding: 6px 9px;
                                                text-align:left;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.consulta_pgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
                                                background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                                border: 0px solid;
                                                padding: 6px 9px;
                                                text-align:left;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.cadastrar_usuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
                                                background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                                border: 0px solid;
                                                padding: 6px 9px;
                                                text-align:left;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.autorizar_pix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
                                                background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                                border: 0px solid;
                                                padding: 6px 9px;
                                                text-align:left;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.gerar_qr_code.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def converter_float_reais(self, valor) -> str:
        valor_formatado = locale.currency(valor, grouping=True)
        return str(valor_formatado)


    def converterDiaHora(self, diaHora) -> str:
        hora_formatada = diaHora.strftime("%d-%m-%Y %H:%M")
        return hora_formatada


    def muda_fonte_tabela_pix(self):
        ok, self.fontTable = QFontDialog.getFont(self.ui.table_busca_e_autoriza_pix)
        if ok:
            self.ui.table_busca_e_autoriza_pix.setFont(self.fontTable)
            self.ui.table_consulta_pix.setFont(self.fontTable)
            self.ui.table_busca_e_autoriza_pix.resizeColumnsToContents()
            self.ui.table_busca_e_autoriza_pix.resizeRowsToContents()
            self.ui.table_consulta_pix.setFont(self.fontTable)
            self.ui.table_consulta_pix.resizeColumnsToContents()
            self.ui.table_consulta_pix.resizeRowsToContents()
        self.carregar_consulta(self.sigla)
        self.carregar_altera_pix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text())

        config['APARENCIA']['FONTE'] = str(self.fontTable)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


    def carregar_altera_pix(self, name, id):
        # Inicializa limpando a tabela
        print('Carrega altera pix')
        self.ui.table_busca_e_autoriza_pix.setRowCount(0)
        self.ui.resultado_busca_autoriza.clear()
        self.ui.table_busca_e_autoriza_pix.setSortingEnabled(False)
        
        idPix = self.ui.campo_buscar_id.text()
        apresentante = self.ui.campo_buscar_apresentante.text()
        # Verificar o estado do filtro status dos pagamentos
        if self.ui.combo_filtro_alterapix.currentIndex() == 0:
            filtro = ''
        elif self.ui.combo_filtro_alterapix.currentIndex() == 1:
            filtro = 'aguardando'
        else:
            filtro = 'pago'

        # Verificar o estado do filtro limite de registros
        if self.ui.combo_limite_altera.currentIndex() == 0:
            limite = 10
        elif self.ui.combo_limite_altera.currentIndex() == 1:
            limite = 30
        elif self.ui.combo_limite_altera.currentIndex() == 2:
            limite = 50
        else:
            limite = 100 


        # Verificar o estado do filtro de data
        if self.ui.combo_filtro_data_alterapix.currentIndex() == 0:
            filtro_data = ''
        else:
            filtro_data = 'Data'

        # Repassa a data escolhida na caixa de seleção de data em formato texto.
        dataBusca = self.ui.filtro_dia_alterapix.text()

        if idPix != '' and apresentante != '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Dados inválidos')
            msg.setText('Informar somente o nome ou somente o ID Pix.')
            msg.exec_()
            self.ui.resultado_busca_consultapix.clear()
            self.ui.resultado_busca_consultapix.setText('Resultado da busca: nenhum registro encontrado')
            return

        if idPix == '':
            pagamentos = self.db_pix.search_pix_by_name( 
                limite=limite,
                filtro=filtro,
                filtro_data=filtro_data,
                apresentante=apresentante,
                data=dataBusca
            )
        else:
            pagamentos = self.db_pix.search_pix_by_id(
                pix_id=idPix,
            )

        # Verifica se a conexão do banco foi encerrada por inatividade. 
        if pagamentos == 'conexão encerrada': 
            self.encerra_sistema() 

        if pagamentos == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Não encontrado')
            msg.setText('Nenhum registro com o nome e/ou filtro informado. Verificar!')
            msg.exec_()
            self.ui.resultado_busca_autoriza.clear()
            self.ui.resultado_busca_autoriza.setText('Resultado da busca: nenhum registro encontrado')
        elif len(pagamentos) < 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Não encontrado')
            msg.setText('Nenhum registro com o nome e/ou filtro informado. Verificar!')
            msg.exec_()
            self.ui.resultado_busca_consultapix.clear()
            self.ui.resultado_busca_consultapix.setText('Resultado da busca: nenhum registro encontrado')
        else:
            linha = 0
            self.ui.table_busca_e_autoriza_pix.setRowCount(len(pagamentos))
            self.ui.table_busca_e_autoriza_pix.setSortingEnabled(False)
            if idPix  == '':
                for pagamento in pagamentos:
                    reais = self.converter_float_reais(pagamento[2])
                    diaHora = self.converterDiaHora(pagamento[4])
                    for coluna in range(0,9,1):
                        if coluna == 0 or coluna == 1 or coluna == 3:
                            item_atual = QTableWidgetItem(str(pagamento[coluna]))
                            item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                                self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.table_busca_e_autoriza_pix.setItem(linha, 
                                coluna, item_atual)
                            item_atual.setFont(self.fontTable)
                        elif coluna == 2:
                            item_atual = QTableWidgetItem(reais)
                            item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                                self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.table_busca_e_autoriza_pix.setItem(linha, 
                                coluna, item_atual)
                        elif coluna == 4:
                            item_atual = QTableWidgetItem(diaHora)
                            item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                                self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.table_busca_e_autoriza_pix.setItem(linha, 
                                coluna, item_atual)
                            item_atual.setFont(self.fontTable)
                        else:
                            # Se for a última coluna, verifica se o valor é none pra retornar ''
                            # Se não for none, aplica a sigla do usuário em maiúsculas
                            if str(pagamento[coluna]) == 'None':
                                pgtoColuna = ''
                            else:
                                pgtoColuna = str(pagamento[coluna])   
                            item_atual = QTableWidgetItem(pgtoColuna)
                            item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                                self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.table_busca_e_autoriza_pix.setItem(linha, 
                                coluna, item_atual)
                            item_atual.setFont(self.fontTable)
                    linha += 1
                    self.ui.table_busca_e_autoriza_pix.resizeColumnsToContents()
                    self.ui.table_busca_e_autoriza_pix.resizeRowsToContents()
            else:
                reais = self.converter_float_reais(pagamentos[2])
                diaHora = self.converterDiaHora(pagamentos[4])
                for coluna in range(0,9,1):
                    if coluna == 0 or coluna == 1 or coluna == 3:
                        item_atual = QTableWidgetItem(str(pagamentos[coluna]))
                        item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                            self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                        item_atual.setFont(self.fontTable)
                        self.ui.table_busca_e_autoriza_pix.setItem(linha, 
                            coluna, item_atual)
                    elif coluna == 2:
                        item_atual = QTableWidgetItem(reais)
                        item_atual.setFont(self.fontTable)
                        self.ui.table_busca_e_autoriza_pix.setItem(linha, 
                            coluna, item_atual)
                        item_atual.setFont(self.fontTable)
                    elif coluna == 4:
                        item_atual.setFont(self.fontTable)
                        item_atual = QTableWidgetItem(diaHora)
                        item_atual.setFont(self.fontTable)
                        self.ui.table_busca_e_autoriza_pix.setItem(linha, 
                            coluna, item_atual)
                    else:
                        # Se for a última coluna, verifica se o valor é none pra retornar ''
                        # Se não for none, aplica a sigla do usuário em maiúsculas
                        if str(pagamentos[coluna]) == 'None':
                            pgtoColuna = ''
                        else:
                            pgtoColuna = str(pagamentos[coluna])   
                        item_atual = QTableWidgetItem(pgtoColuna)
                        item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                            self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                        item_atual.setFont(self.fontTable)
                        self.ui.table_busca_e_autoriza_pix.setItem(linha, 
                            coluna, item_atual)
                        item_atual.setFont(self.fontTable)
                self.ui.table_busca_e_autoriza_pix.resizeColumnsToContents()
                self.ui.table_busca_e_autoriza_pix.resizeRowsToContents()
        self.ui.table_busca_e_autoriza_pix.setSortingEnabled(True)


    def carregar_consulta(self, caixa):
        # Inicializa limpando a tabela
        print('Carrega consulta pix')  
        self.ui.table_consulta_pix.setRowCount(0)
        self.ui.resultado_busca_autoriza.clear()
        idPix = self.ui.campo_buscar_id_consulta_pix.text()
        apresentante = self.ui.campo_buscar_apresentante_consulta_pix.text()
        # Verificar o estado do filtro status dos pagamentos
        if self.ui.combo_filtro_consultapix.currentIndex() == 0:
            filtro = ''
        elif self.ui.combo_filtro_consultapix.currentIndex() == 1:
            filtro = 'aguardando'
        else:
            filtro = 'pago'

        # Verificar o estado do filtro limite de registros
        if self.ui.combo_limite_consultapix.currentIndex() == 0:
            limite = 10
        elif self.ui.combo_limite_consultapix.currentIndex() == 1:
            limite = 30
        elif self.ui.combo_limite_consultapix.currentIndex() == 2:
            limite = 50
        else:
            limite = 100 


        # Verificar o estado do filtro de data
        if self.ui.combo_filtro_data_consultapix.currentIndex() == 0:
            filtro_data = ''
        else:
            filtro_data = 'Data'

        # Repassa a data escolhida na caixa de seleção de data em formato texto.
        dataBusca = self.ui.filtro_data_consultapix.text()

        if idPix != '' and apresentante != '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Dados inválidos')
            msg.setText('Informar somente o nome ou somente o ID Pix.')
            msg.exec_()
            self.ui.resultado_busca_consultapix.clear()
            self.ui.resultado_busca_consultapix.setText('Resultado da busca: nenhum registro encontrado')
            return

        if idPix == '':
            pagamentos = self.db_pix.search_pix_by_caixa(
                caixa=caixa, 
                limite=limite,
                filtro=filtro,
                filtro_data=filtro_data,
                apresentante=apresentante,
                data=dataBusca
            )
        else:
            pagamentos = self.db_pix.search_pix_by_id_caixa(
                pix_id=idPix,
                caixa=caixa
            )

        # Verifica se a conexão do banco foi encerrada por inatividade.
        if pagamentos == 'conexão encerrada':
            self.encerra_sistema()

        if pagamentos == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Não encontrado')
            msg.setText('Nenhum registro com o nome e/ou filtro informado. Verificar!')
            msg.exec_()
            self.ui.resultado_busca_consultapix.clear()
            self.ui.resultado_busca_consultapix.setText('Resultado da busca: nenhum registro encontrado')
        elif len(pagamentos) < 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Não encontrado')
            msg.setText('Nenhum registro com o nome e/ou filtro informado. Verificar!')
            msg.exec_()
            self.ui.resultado_busca_consultapix.clear()
            self.ui.resultado_busca_consultapix.setText('Resultado da busca: nenhum registro encontrado')
        else:
            linha = 0
            self.ui.table_consulta_pix.setSortingEnabled(False)
            if idPix == '':
                self.ui.table_consulta_pix.setRowCount(len(pagamentos))
                for pagamento in pagamentos:
                    reais = self.converter_float_reais(pagamento[2])
                    diaHora = self.converterDiaHora(pagamento[3])
                    for coluna in range(0,9,1):
                        if coluna == 0 or coluna == 1:
                            item_atual = QTableWidgetItem(str(pagamento[coluna]))
                            item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                                self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.table_consulta_pix.setItem(linha, 
                                coluna, item_atual)
                        elif coluna == 2:
                            item_atual = QTableWidgetItem(reais)
                            item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                                self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.table_consulta_pix.setItem(linha, 
                                coluna, item_atual)
                        elif coluna == 3:
                            item_atual = QTableWidgetItem(diaHora)
                            item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                                self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.table_consulta_pix.setItem(linha, 
                                coluna, item_atual)
                            item_atual.setFont(self.fontTable)
                        elif coluna == 4:
                            # se for a coluna 4 "createdby" não é necessário exibir
                            # pois nessa tela todos os pagamentos são do próprio caixa
                            continue
                        else:
                            # Se for a última coluna, verifica se o valor é none pra retornar ''
                                # Se não for none, aplica a sigla do usuário em maiúsculas
                            if str(pagamento[coluna]) == 'None':
                                pgtoColuna = ''
                            else:
                                pgtoColuna = str(pagamento[coluna])   
                            item_atual = QTableWidgetItem(pgtoColuna)
                            item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                                self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.table_consulta_pix.setItem(linha, 
                                coluna-1, item_atual)
                    linha += 1
                    self.ui.table_consulta_pix.resizeColumnsToContents()
                    self.ui.table_consulta_pix.resizeRowsToContents()
            else:
                self.ui.table_consulta_pix.setRowCount(1)
                reais = self.converter_float_reais(pagamentos[2])
                diaHora = self.converterDiaHora(pagamentos[3])
                for coluna in range(0,9,1):
                    if coluna == 0 or coluna == 1:
                        item_atual = QTableWidgetItem(str(pagamentos[coluna]))
                        item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                            self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                        item_atual.setFont(self.fontTable)
                        self.ui.table_consulta_pix.setItem(linha, 
                            coluna, item_atual)
                        item_atual.setFont(self.fontTable)
                    elif coluna == 2:
                        item_atual = QTableWidgetItem(reais)
                        item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                            self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                        item_atual.setFont(self.fontTable)
                        self.ui.table_consulta_pix.setItem(linha, 
                            coluna, item_atual)
                    elif coluna == 3:
                        item_atual = QTableWidgetItem(diaHora)
                        item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                            self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                        item_atual.setFont(self.fontTable)
                        self.ui.table_consulta_pix.setItem(linha, 
                            coluna, item_atual)
                        item_atual.setFont(self.fontTable)
                    elif coluna == 4:
                        # se for a coluna 4 "createdby" não é necessário exibir
                        # pois nessa tela todos os pagamentos são do próprio caixa
                        continue
                    else:
                        if str(pagamentos[coluna]) == 'None':
                            pgtoColuna = ''
                        else:
                            pgtoColuna = str(pagamentos[coluna])   
                        item_atual = QTableWidgetItem(pgtoColuna)
                        item_atual.setTextColor(QColor(self.tema_atual.main_text_color[0],
                            self.tema_atual.main_text_color[1],self.tema_atual.main_text_color[2]))
                        item_atual.setFont(self.fontTable)
                        self.ui.table_consulta_pix.setItem(linha, 
                            coluna-1, item_atual)
                        item_atual.setFont(self.fontTable)
                self.ui.table_consulta_pix.resizeColumnsToContents()
                self.ui.table_consulta_pix.resizeRowsToContents()
        self.ui.table_consulta_pix.setSortingEnabled(True)


    def tela_cadastrar_usuario(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_cadastrar)
        self.ui.cadastrar_usuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            border: 2px solid rgb'''+f'{(self.tema_atual.cor_destaque_1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.gerar_qr_code.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.consulta_pgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.autorizar_pix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.tema_atual.left_menu_text_color)}'+''';
	                                        background-color: rgb'''+f'{(self.tema_atual.side_menu_bg_color)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.tema_atual.side_menu_hover_bg_color)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def cadastra_usuario(self):
        if self.ui.campo_senha.text() != self.ui.campo_repetir_senha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Senhas não conferem')
            msg.setText('As senhas informadas são divergentes!')
            msg.exec_()
            return None

        user = self.ui.campo_usuario.text()
        nome = self.ui.campo_nome_completo.text()
        senha = self.ui.campo_senha.text()
        acesso = self.ui.combo_tipo_usuario.currentText()
        
        cadastro = self.db.insertUsers(user.lower(), senha, acesso.lower(), nome)
        if cadastro == 'sucesso':
            msg_sucesso = QMessageBox()
            msg_sucesso.setIcon(QMessageBox.Warning)
            msg_sucesso.setWindowTitle('Usuário cadastrado.')
            msg_sucesso.setText('O usuário foi cadastrado com sucesso!')
            msg_sucesso.exec_()
        else:
            msg_erro = QMessageBox()
            msg_erro.setIcon(QMessageBox.Warning)
            msg_erro.setWindowTitle('Erro!')
            msg_erro.setText('O usuário informado já está cadastrado!')
            msg_erro.exec_()
        return None


    def limpar_campos_qr_code(self):
        print("Limpar campos")
        self.ui.campo_apresentante.setText('')
        self.ui.campo_cpf_apresentante.setText('')
        self.ui.campo_valor.setText('')
        self.ui.txt_id_pix.setText('ID Pix: ')
        self.ui.campo_email_solicitante.setText('')


    def limpar_campos_cadastro(self):
        print("Limpar campos")
        self.ui.combo_tipo_usuario.set_current_index(0)
        self.ui.campo_usuario.setText('')
        self.ui.campo_nome_completo.setText('')
        self.ui.campo_senha.setText('')
        self.ui.campo_repetir_senha.setText('')


    def gera_qr_code(self, apresentante, valor, cpf_cnpj):
        cpf_cnpj_formatado = formata_cpf_cnpj(cpf_cnpj)
        solicitante = self.db_pix.busca_solicitante(cpf_cnpj_formatado)

        # Verifica se a conexão do banco foi encerrada por inatividade.
        if solicitante == 'conexão encerrada':
            self.encerra_sistema()

        if solicitante == None or solicitante == 'erro':
            msg_erro = QMessageBox()
            msg_erro.setIcon(QMessageBox.Warning)
            msg_erro.setWindowTitle('Erro!')
            msg_erro.setText('O solicitante não está cadastrado, verificar e tentar novamente.')
            msg_erro.exec_()
            return
        else:
            erro_pix = False
            print("Gerar QrCode")
            txt_id = gen_txt_id()
            pgto = Pagamento(id_tx=txt_id,
                        nome=apresentante,
                        valor=valor,
                        copia_cola='')

            deposito_inicial = pgto.valor
            valor_decimal = deposito_inicial.replace('.', '')
            valor_decimal = valor_decimal.replace(',', '.')

            cpf_cnpj_informado = cpf_cnpj
            digitos_cpf_cnpj = limpa_cpf_cnpj(cpf_cnpj_informado)
            
            if len(digitos_cpf_cnpj) == 11:
                err, cpf_cnpj_verificado = verifica_cpf(cpf_cnpj_informado)
            else:
                err, cpf_cnpj_verificado = verifica_cnpj(cpf_cnpj_informado)

            if err:
                erro_pix = True
                self.erro_dados_pix('O CPF/CNPJ informado está incorreto.')

            try:
                valor_pix = Decimal(valor_decimal)
            except Exception as error:
                erro_pix = True
                self.erro_dados_pix('Formato de valor inválido, verificar. (ex.: 24.145,00)')
                return
            else:        
                reais = self.converter_float_reais(valor_pix)

            if not erro_pix:
                # Gravar pix no banco de dados PostgreSQL
                try:
                    self.db_pix.insert_pix(txt_id=pgto.id_tx, valor=valor_pix, created_by=self.sigla,
                                status='aguardando', cpf_cnpj=cpf_cnpj_verificado)
                except Exception as error:
                    self.erro_dados_pix(error)
                pgto.pix_id = self.db_pix.get_pix_id(txt_id=pgto.id_tx)

                # Gerar QrCode com os dados preenchidos.
                pixRegistrado = False
                tentativas = 0
                
                # Gerar QrCode com os dados preenchidos.
                while not pixRegistrado:
                    time.sleep(2)
                    pgto.copia_cola = self.db_pix.get_copia_cola(txt_id=pgto.id_tx)
                    tentativas += 1
                    if pgto.copia_cola != None and pgto.copia_cola != '':
                        pixRegistrado = True
                    if tentativas >= 5:
                        msg_erro = QMessageBox()
                        msg_erro.setIcon(QMessageBox.Warning)
                        msg_erro.setWindowTitle('Erro ao gerar arquivo QrCode')
                        msg_erro.setText(f'Solicitar ao TI que verifique o status do Servidor de API "(\\vmauto)".')
                        msg_erro.exec_()
                        return
                
                qr = qrcode.make(pgto.copia_cola)
                qr.save(r'C:\SisPag Pix\src\pixqrcode.png')

                self.ui.txt_id_pix.setText(f"ID Pix: {pgto.pix_id}")
                # Gerar Arquivo PDF com os dados + QrCode

                # Fechar o arquivo PDF, caso esteja aberto
                
                pdf = PDF()
                pdf.print_chapter(pgto.nome, reais, pgto.pix_id, pgto.copia_cola)
                # Caso o PDF de impressão do QRCode já esteja aberto (ex. O usuário esqueceu de fechar
                # na geração anterior, o sistema não conseguirá gravar o arquivo pois o windows gera erro
                # de permissão ao criar e gravar novo arquivo com um de mesmo nome e local já aberto
                # para evitar um precoce fim do processo de geração, utilizo um arquivo "extra" que nada
                # mais é do que o mesmo arquivo, com nome diferente no mesmo local, para seguir com a impressão.
                try:
                    pdf.output(ADOBE_PDF_FILE, 'F')
                except Exception as error:
                    msg_erro = QMessageBox()
                    msg_erro.setIcon(QMessageBox.Warning)
                    msg_erro.setWindowTitle('Erro ao gerar arquivo PDF')
                    msg_erro.setText('Já há um arquivo PDF de QrCode aberto, será gerado um arquivo backup.')
                    msg_erro.setInformativeText('Após imprimir, sempre feche todas as abas e PDFs abertos, para evitar erros.')
                    msg_erro.setDetailedText(f'Descrição do erro: {error}')
                    msg_erro.exec_()
                    try:
                        pdf.output(ADOBE_PDF_FILE_EXTRA, 'F')
                    except Exception as error:
                        msg_erro = QMessageBox()
                        msg_erro.setIcon(QMessageBox.Warning)
                        msg_erro.setWindowTitle('Falha geral na criação do PDF')
                        msg_erro.setText('Não foi possível gerar o PDF para impressão do Pix informado')
                        msg_erro.setInformativeText("Fechar o Adobe e todas as suas abas e gerar novo QRCode...")
                        msg_erro.setDetailedText(f'Descrição do erro: {error}')
                        msg_erro.exec_()
                    else:
                        # Abrir arquivo PDF de backup com nome diferente pois já tem um com nome igual aberto.
                        cmd = '"{}" "{}"'.format(ADOBE_READER, ADOBE_PDF_FILE_EXTRA)
                        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    # No caso de nenhum erro na criação, abrir arquivo PDF para conferência dos dados
                    cmd = '"{}" "{}"'.format(ADOBE_READER, ADOBE_PDF_FILE)
                    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.tx_id_pix = txt_id

    def erro_dados_pix(self, texto):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Erro ao gerar o Pix')
        msg.setText(f'Erro! {texto}')
        msg.exec_()


    def slide_left_menu(self):
        width = self.ui.frame_left_base.width()

        if width == 45:
            newWidth = 235
            self.ui.menu.setStyleSheet('''icon: url(:/icons/icons/chevron-left.svg);
                                        padding: 6px 9px;''')
        else:
            newWidth = 45
            self.ui.menu.setStyleSheet('''icon: url(:/icons/icons/menu.svg);
                                        padding: 6px 9px;''')
        
        self.animation1 = QPropertyAnimation(self.ui.frame_left_base, b"maximumWidth")
        self.animation2 = QPropertyAnimation(self.ui.frame_left_menu, b"maximumWidth")
        self.animation1.setDuration(250)
        self.animation2.setDuration(250)
        self.animation1.setStartValue(width)
        self.animation2.setStartValue(width)
        self.animation1.setEndValue(newWidth)
        self.animation2.setEndValue(newWidth)
        self.animation1.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation2.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation1.start()
        self.animation2.start()

def show_message(mensagem, titulo):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowIcon(QIcon(r'C:\SisPag Pix\gui\icons\info.svg'))

    msg.setWindowTitle(titulo)
    msg.setText(mensagem)

    msg.setInformativeText("Informações adicionais podem ser inseridas aqui...")
    msg.setDetailedText("Ainda mais detalhes nessa parte")
    msg.exec_()

if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    # Verificar se o sistema permite uso de notificações
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "System Tray", "System tray was not detected!")
        sys.exit(1)

    app.setWindowIcon(QIcon(r'C:\SisPag Pix\gui\icons\pix_icon.png'))

    # Em vez de fechar o app minimizar para a system tray
    app.setQuitOnLastWindowClosed(False)

    # Criar o ícone do app e exibir na "system tray"
    tray = QSystemTrayIcon(QIcon(r'C:\SisPag Pix\gui\icons\pix_icon.png'), app)
    tray.show()

    # # Criar o menu da system tray
    menu = QMenu()

    # Somente para teste de funcionamento das notificações
    # action_message_box = QAction("Mostrar caixa de mensagem")
    # action_message_box.triggered.connect(lambda: show_message('Teste de Mensagem ao clicar no Tray','Caixa de Mensagem'))
    # menu.addAction(action_message_box)
    
    # # Mostrar uma notificação no sistema
    # Somente para teste de funcionamento das notificações
    # action_tray_message = QAction("Mostrar notificação")
    # action_tray_message.triggered.connect(lambda: show_tray_message(window_obj, tray, 'Teste', 'Mensagem de teste'))
    # menu.addAction(action_tray_message)
    
    # Esconder a janela para a system tray
    action_hide = QAction("Ocultar a janela principal")
    menu.addAction(action_hide)
    

    # Mostrar a janela para a system tray
    action_show = QAction("Exibir a janela principal")
    menu.addAction(action_show)


    # Mostrar a janela a partir da system tray
    action_exit = QAction("Sair")
    action_exit.triggered.connect(app.exit)
    menu.addAction(action_exit)

    # Adicionar o menu ao contexto da system tray
    tray.setContextMenu(menu)

    login_form = LoginWindow()
    login_form.show()
    sys.exit(app.exec_())
