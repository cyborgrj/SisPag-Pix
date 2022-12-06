########################################################################
## IMPORTS
########################################################################
import sys
from PySide2 import *
from datetime import datetime
from random import randint
from pixqrcodegen import Payload
from fpdf import FPDF
import uuid
import subprocess
from db.db import *
import locale
import configparser
import re

########################################################################
# IMPORT GUI FILE
from gui.ui_main import *
from gui.ui_LoginUI import *
from gui.ui_ConfirmaPix import *
from gui.ui_InsereProtocolo import *
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

# Configurações de Aplicativos Adobe e caminho do PDF
ADOBE_READER = config['ADOBE']['ACROBAT']
ADOBE_PDF_FILE = config['ADOBE']['PDFFILE']
ADOBE_QRCODE = config['ADOBE']['QRCODE']

########################################################################


class Tema:
    def __init__(self, nomeTema: str):
        self.nomeTema = nomeTema
        self.escolherTema(nomeTema)

    def escolherTema(self, novoTema: str):
        self.nomeTema = novoTema
        if novoTema == "Mono Escuro":
            print('Tema escolhido: Mono Dark')
            # Definições do tema:
            self.sideMenuHoverBgColor = (60, 60, 60)
            self.sideMenuBgColor = (35, 35, 35)
            self.sideAltMenurBgColor = (100, 100, 100)
            self.rightSideMenuBgColor = (70, 70, 70)
            self.tableItemBgColor = (50, 50, 50)
            self.btnBgColor = (45, 45, 45)

            # Cores das fontes
            self.leftMenuTextColor = (248, 248, 242)
            self.mainTextColor = (255, 255, 255)
            self.keyColor1 = (255, 255, 200)
            self.keyColor2 = (120, 120, 120)
            self.corDestaque1 = (170, 170, 170)
            self.corDestaque2 = (120, 120, 120)
            self.inputTextBgColor = (255,255,255,150)

            # Stops do gradiente RGBA
            self.stop1 = (36, 36, 36, 255)
            self.stop2 = (80, 80, 80, 255)

        elif novoTema == "Mono Claro":
            print('Tema escolhido: Mono Light')
            # Definições do tema:
            self.sideMenuHoverBgColor = (90, 90, 90)
            self.sideMenuBgColor = (70, 70, 70)
            self.sideAltMenurBgColor = (130, 130, 130)
            self.rightSideMenuBgColor = (200, 200, 200)
            self.tableItemBgColor = (50, 50, 50)
            self.btnBgColor = (70, 70, 70)

            # Cores das fontes
            self.leftMenuTextColor = (248, 248, 242)
            self.mainTextColor = (10, 10, 10)
            self.keyColor1 = (255, 255, 200)
            self.keyColor2 = (120, 120, 120)
            self.corDestaque1 = (170, 170, 170)
            self.corDestaque2 = (120, 120, 120)
            self.inputTextBgColor = (10, 10, 10, 250)

            # Stops do gradiente RGBA
            self.stop1 = (36, 36, 36, 255)
            self.stop2 = (80, 80, 80, 255)

        elif novoTema == "Drcl Night":
            print('Tema escolhido: Drácula Night')
            # Definições do tema:
            # Cores de fundo de tela/botões
            self.sideMenuHoverBgColor = (40, 42, 54)
            self.sideMenuBgColor = (25, 26, 33)
            self.sideAltMenurBgColor = (49, 51, 65)
            self.rightSideMenuBgColor = (40, 42, 54)
            self.tableItemBgColor = (33, 34, 44)
            self.btnBgColor = (29, 30, 40)

            # Cores das fontes
            self.leftMenuTextColor = (248, 248, 242)
            self.mainTextColor = (248, 248, 242)
            self.keyColor1 = (98, 114, 139)
            self.keyColor2 = (96, 114, 164)
            self.corDestaque1 = (189, 147, 249)
            self.corDestaque2 = (239, 113, 159)
            self.inputTextBgColor = (255,255,255,150)

            # Stops do gradiente RGBA
            self.stop1 = (25, 26, 33, 255)
            self.stop2 = (40, 42, 54, 255)

        elif novoTema == "Drcl Claro":
            print('Tema escolhido: Drácula Claro')
            # Definições do tema:
            # Cores de fundo de tela/botões
            self.sideMenuHoverBgColor = (80, 84, 108)
            self.sideMenuBgColor = (50, 52, 66)
            self.sideAltMenurBgColor = (49, 51, 65)
            self.rightSideMenuBgColor = (248, 248, 242)
            self.tableItemBgColor = (66, 68, 88)
            self.btnBgColor = (58, 60, 80)

            # Cores das fontes
            self.leftMenuTextColor = (248, 248, 242)
            self.mainTextColor = (40, 42, 54)
            self.keyColor1 = (98, 114, 139)
            self.keyColor2 = (96, 114, 164)
            self.corDestaque1 = (189, 147, 249)
            self.corDestaque2 = (239, 113, 159)
            self.inputTextBgColor = (40, 42, 54, 150)

            # Stops do gradiente RGBA
            self.stop1 = (25, 26, 33, 255)
            self.stop2 = (40, 42, 54, 255)


class Pagamento:
    def __init__(self, idTx, nome, valor, copiaCola):
        self.valor = valor
        self.idTx = idTx
        self.nome = nome
        self.copiaCola = copiaCola

    def insertUser(self):
        return 'QrCode Gerado com sucesso!'


def dividePixCopiaCola(copiaCola):
    parte1, parte2 = copiaCola.split('5802BR')
    parte2 = '5802BR' + parte2
    return parte1, parte2


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

    def chapter_body(self, apresentante, valor, id, copiaCola):
        # Times 12
        self.set_font('Times', '', 26)
        self.image(ADOBE_QRCODE, 60, 140, 100)
        # Line break
        self.ln()
        self.cell(50, 14, f"Identificador nº: {id}", align='center')
        self.ln()
        self.cell(20, 14, f"Apresentante: {apresentante}")
        self.ln()
        self.cell(20, 14, f"Valor: {valor}")
        self.ln()
        self.ln()
        self.cell(80, 14, '                       QRCode para Pagamento', align='center')
        for i in range(0, 8, 1):
            self.ln()
        self.cell(80, 14, f"Pix Copia e Cola:")
        self.ln()
        self.set_font('Times', '', 5)
        # se dividido no pdf o código Pix acaba perdendo sua integridade...
        # pixParte1, pixParte2 = dividePixCopiaCola(copiaCola)
        self.cell(120, 5, f"{copiaCola}")
        self.ln()

    def print_chapter(self, apresentante, valor, id, copiaCola):
        self.add_page()
        self.chapter_title()
        self.chapter_body(apresentante, valor, id, copiaCola)


def geradorID(stringId: str) -> str:
    ''' 
    Utilizar somente os 8 primeiros dídigos do UUID e colocar minúsculas ou maíusculas aleatoriamente.
    Isso é feito para diminuir ainda mais as chances de gerar um código repedito já que há um limite
    na quantidade de caracteres do identificador no Pix, assim sendo não podemos utilizar o UUID completo.
    '''

    # array para evitar sequencias de números, ex: ae234367.
    num =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    x = 0
    identificador = ''
    for s in stringId:
        # se o x estiver na posição 4 ou 7 e for número.
        if x == 4 or x == 5:
            if s in num:
                if stringId[x+5] not in num:
                    s = stringId[x]
                else:
                    s = 'u'

        i = randint(0,1)
        if i == 0:
            identificador = identificador + s.upper()
        else:
            identificador = identificador + s
        if x >= 7:
            break
        x += 1
    return identificador


def diaCorrente():
    data = datetime.today()
    strData = data.strftime('%d/%m/%Y')
    dia, mes, ano = strData.split('/')
    # print(f'Dia: {dia}, mês: {mes}, ano: {ano}')
    return int(ano), int(mes), int(dia)


def carregaFonteConfig():
    nomeFonte = 'MS Shell Dlg 2'
    tamFonte = 11
    try:
        find = re.search(r'(?<=\().*,\d\d', FONTE)
        grupo = find.group().split(',')
    except Exception as error:
        print('Erro ao carregar fonte do arquivo config.ini, carregando fonte padrão...')
        return nomeFonte, tamFonte
    else:
        if grupo != None:
            nomeFonte = str(grupo[0])
            tamFonte = int(grupo[1])
        else:
            return nomeFonte, tamFonte
    finally:
        return nomeFonte, tamFonte


class InsereProtocolo(QDialog):
    def __init__(self, pixID, nome, valor, caixa):
        self.dbPix = DataBasePix(HOSTNAME, DATABASE, USERNAME, PWD, PORT_ID)
        QDialog.__init__(self)
        self.ui = Ui_Dialog_Protocolo()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.pixID = pixID
        self.ui.label_id_pix_protocolo.setText(f'ID Pix: {pixID}')
        self.ui.label_caixa_protocolo.setText(f'Usuário: {caixa.upper()}')
        self.ui.label_nome_protocolo.setText(f'Nome: {nome}')
        self.ui.label_valor_protocolo.setText(f'Valor: {valor}')
        self.show()
        self.ui.btn_cancelar_protocolo.clicked.connect(lambda: self.sair_insere_protocolo())
        self.ui.btn_gravar_protocolo.clicked.connect(
            lambda: self.confirma_protocolo(self.pixID, self.ui.campo_protocolo.text()))
        self.ui.campo_protocolo.returnPressed.connect(
            lambda: self.confirma_protocolo(self.pixID, self.ui.campo_protocolo.text()))

    
    def sair_insere_protocolo(self):
        self.done(0)
        self.close()

    def confirma_protocolo(self, txtID, protocolo):
        try:
            self.dbPix.updatePixNumInterno(txtID, protocolo)
        except Exception as error:
            print(f'Erro ao gravar protocolo: {error}')
            self.done(0)
            self.close()
        else:
            self.done(1)
            self.close()


class ConfirmaPix(QDialog):
    def __init__(self, pixID, nome, valor, caixa):
        self.db = DataBaseUsers(DBNAME)
        QDialog.__init__(self)
        self.ui = Ui_Dialog_Confirma_Pix()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.label_id_pix.setText(f'ID Pix: {pixID}')
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
        username, acesso = self.db.checkUsers(sigla.lower(), senha)
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
        self.ui.Sair.clicked.connect(lambda: self.sair_login())
        self.ui.btn_login.clicked.connect(lambda: self.efetuar_login())
    
    def sair_login(self):
        self.close()
    
    def efetuar_login(self):       
        usuario = self.ui.campo_usuario.text()
        senha = self.ui.campo_senha.text()
        username, acesso = self.db.checkUsers(usuario.lower(), senha)
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
        self.dbPix = DataBasePix(HOSTNAME, DATABASE, USERNAME, PWD, PORT_ID)
        self.usuario = usuario
        self.acesso = acesso
        self.sigla = sigla
        locale.setlocale(locale.LC_ALL, LOCALE)
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("SisPag PIX - 2RGI")
        self.temaAtual = Tema(TEMA)
        nomeFonte, tamFonte = carregaFonteConfig()
        self.fontTable = QFont(nomeFonte, tamFonte)
        
        dia = QDate()
        try:
            aa, mm, dd = diaCorrente()
        except Exception as error:
            print(f'Erro ao recuperar dia{error}')
            aa = 2023
            mm = 1
            dd = 1
        finally:
            dia.setDate(aa, mm, dd)
        
        # Definir o dia base para ser exibido no filtro de consulta/libera pix
        self.ui.filtro_dia_alterapix.setDate(dia)
        self.ui.filtro_data_consultapix.setDate(dia)
        
        # Verificar o nível de acesso do usuário para definir quais telas serão exibidas.
        self.verificaAcesso()
        
        # Recolher e expandir menu lateral
        self.ui.Menu.clicked.connect(lambda: self.slideLeftMenu())
        
        # Exibir usuário logado
        self.ui.campo_usuario_atual.setText(f"Usuário: {self.usuario}")

        # Acesso dos Widgets e suas respectivas páginas
        self.ui.GerarQrCode.clicked.connect(lambda: self.telaGerarQrCode())
        self.ui.Imprimir.clicked.connect(lambda: self.telaImprimir())
        self.ui.ConsultaPgto.clicked.connect(lambda: self.telaConsultar())
        self.ui.CadastrarUsuario.clicked.connect(lambda: self.telaCadastrarUsuario())
        self.ui.AutorizarPix.clicked.connect(lambda: self.telaAutorizarPix())
        self.ui.Settings.clicked.connect(lambda: self.telaSettings())

        # Ações da tela de gerar QrCode
        self.ui.btn_gerar_qrcode.clicked.connect(
            lambda: self.geraQrCode(self.ui.campo_apresentante.text(), 
            self.ui.campo_valor.text(), self.ui.campo_cpf_apresentante.text()))
        self.ui.btn_limpar_campos.clicked.connect(lambda: self.limparCamposQrCode())

        # Ações da tela de imprimir QrCode
        self.ui.btn_buscar_imprimir.clicked.connect(
            lambda: self.buscarImprimirPix(self.ui.campo_txt_id_imprimir_pix.text()))
        self.ui.btn_imprimir.clicked.connect(
            lambda: self.imprimirPix()
        )

        # Ações da tela de cadastro
        self.ui.btn_cadastrar.clicked.connect(lambda: self.cadastraUsuario())
        self.ui.btn_cancelar.clicked.connect(lambda: self.limparCamposCadastro())
        self.ui.Sair.clicked.connect(lambda: self.sairSistema())

        # Ações da tela de consulta pix
        self.ui.btn_set_big_font_consulta.clicked.connect(
            lambda: self.mudaFonteTabelaPix())
        self.ui.btn_buscar_consulta_pix.clicked.connect(
            lambda: self.carregarConsulta(self.sigla))
        self.ui.campo_buscar_apresentante_consulta_pix.returnPressed.connect(
            lambda: self.carregarConsulta(self.sigla))
        self.ui.campo_buscar_id_consulta_pix.returnPressed.connect(
            lambda: self.carregarConsulta(self.sigla))
        self.ui.btn_inser_num_interno_consulta_pix.clicked.connect(
            lambda: self.insereProtocoloPixSelecionado())

        # Ações da tela de altera Pix
        self.ui.btn_set_big_font.clicked.connect(
            lambda: self.mudaFonteTabelaPix())
        self.ui.campo_buscar_apresentante.returnPressed.connect(
            lambda: self.carregarAlteraPix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text()))
        self.ui.campo_buscar_id.returnPressed.connect(
            lambda: self.carregarAlteraPix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text()))        
        self.ui.btn_buscar_alteraPix.clicked.connect(
            lambda: self.carregarAlteraPix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text()))
        self.ui.btn_cancelar_altera_pix.clicked.connect(
            lambda: self.limpaCamposAlteraPix())
        self.ui.btn_liberar_pix.clicked.connect(
            lambda: self.alteraPixSelecionado())

        # Ações de configurações do sistema (Settings)
        self.ui.combo_tema.activated.connect(lambda: 
                self.temaAtual.escolherTema(self.ui.combo_tema.currentText()))
        self.ui.btn_aplicar_tema.clicked.connect(lambda: self.aplicaTema(self.temaAtual))

        self.show()

        if TEMA != 'Drcl Night':
            self.temaAtual.escolherTema(TEMA)
            self.aplicaTema(self.temaAtual)


    def buscarImprimirPix(self, txtId):
        pix = self.dbPix.searchPixByID(txtId)
        if pix != None:
            nomeApresentante = pix[1]
            valor = (pix[2])
            erroPix = False
            print("Gerar QrCode para impressão")
            pgto = Pagamento(idTx=txtId,
                        nome=nomeApresentante,
                        valor=valor,
                        copiaCola='')
            valor_str = str(pgto.valor)
            reais = self.converterFloatReais(pgto.valor)
            # Validar dados antes de gerar QRCode/PDF e gravar no banco
            if len(pgto.idTx) < 8:
                erroPix = True
                self.erroDadosPix('Não foi possível gerar o ID do Pix.')
            
            if len(pgto.nome) < 8:
                erroPix = True
                self.erroDadosPix('Informar pelo menos um nome e sobrenome.')
            
            if not erroPix:
                # Gerar QrCode com os dados preenchidos.
                self.ui.txt_id_pix.setText(f"ID Pix: {pgto.idTx}")

                #print(rgi.Nome, pgto.nome, rgi.ChavePix, pgto.valor, rgi.Cidade, pgto.idTx)
                payload = Payload(RGI_NOME, pgto.nome, RGI_CHAVE_PIX, valor_str, RGI_CIDADE, pgto.idTx)
                pixCopiaCola = payload.gerarPayload()
                pgto.copiaCola = pixCopiaCola

                # Gerar Arquivo PDF com os dados + QrCode
                pdf = PDF()
                pdf.print_chapter(pgto.nome, reais, pgto.idTx, pgto.copiaCola)
                pdf.output(ADOBE_PDF_FILE, 'F')

                # Abrir qrquivo PDF para impressão
                cmd = '"{}" /p "{}"'.format(ADOBE_READER, ADOBE_PDF_FILE)
                subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            self.erroDadosPix('O Código IDPix informado, não foi encontrado.')


    def imprimirPix(self):
        # Abrir qrquivo PDF para conferência dos dados
        cmd = '"{}" /p "{}"'.format(ADOBE_READER, ADOBE_PDF_FILE)
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def insereProtocoloPixSelecionado(self):
        colunaId = self.ui.tableConsultaPix.selectedIndexes()[0]
        colunaNome = self.ui.tableConsultaPix.selectedIndexes()[1]
        colunaValor = self.ui.tableConsultaPix.selectedIndexes()[2]
        colunaStatus = self.ui.tableConsultaPix.selectedIndexes()[4]

        id = self.ui.tableConsultaPix.model().data(colunaId)
        apresentante = self.ui.tableConsultaPix.model().data(colunaNome)
        valor = self.ui.tableConsultaPix.model().data(colunaValor)
        status = self.ui.tableConsultaPix.model().data(colunaStatus)

        if status == 'pago':
            self.dialog = InsereProtocolo(pixID=id, nome=apresentante, valor=valor, caixa=self.sigla)
            confirmaProtocolo = self.dialog.exec_()
            self.dialog.close()
            if confirmaProtocolo == 1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Cadastrado com sucesso!')
                msg.setText(f'O nº de Protocolo/Certidão foi inserido com sucesso!')
                msg.exec_()
                self.carregarConsulta(self.sigla)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Pix não está pago')
            msg.setText(f'Só é possível inserir protocolo em pix com status pago!')
            msg.exec_()


    def alteraPixSelecionado(self):
        colunaId = self.ui.tableBuscaEAutorizaPix.selectedIndexes()[0]
        colunaNome = self.ui.tableBuscaEAutorizaPix.selectedIndexes()[1]
        colunaValor = self.ui.tableBuscaEAutorizaPix.selectedIndexes()[2]

        id = self.ui.tableBuscaEAutorizaPix.model().data(colunaId)
        apresentante = self.ui.tableBuscaEAutorizaPix.model().data(colunaNome)
        valor = self.ui.tableBuscaEAutorizaPix.model().data(colunaValor)

        self.dialog = ConfirmaPix(pixID=id, nome=apresentante, valor=valor, caixa=self.sigla)
        senhaAutorizaPixOk = self.dialog.exec_()
        self.dialog.close()
        if senhaAutorizaPixOk == 1:
            try:
                self.dbPix.updatePix(txtID=id, updatedBy=self.sigla, status='pago')
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
                self.carregarAlteraPix('','')
        

    def limpaCamposAlteraPix(self):
        self.ui.campo_buscar_id.setText('')
        self.ui.campo_buscar_apresentante.setText('')
        self.ui.tableBuscaEAutorizaPix.setRowCount(0)
        self.ui.tableBuscaEAutorizaPix.clearContents()
        self.ui.tableBuscaEAutorizaPix.clearSpans()
        self.ui.resultado_busca_autoriza.clear()
        self.ui.tableBuscaEAutorizaPix.setSortingEnabled(False)


    def verificaAcesso(self):
        if self.acesso.lower() == 'administrador':
            # Inicializar a MainWindow do App na tela de autorizar pix.
            self.ui.CadastrarUsuario.setVisible(True)
            self.telaCadastrarUsuario()
            # Na fase de desenvolvimento o usuário administrador terá acesso à todas as telas
            # self.ui.AutorizarPix.setVisible(False)
            # self.ui.GerarQrCode.setVisible(False)
            # self.ui.ConsultaPgto.setVisible(False)
            # self.ui.Imprimir.setVisible(False)

        elif self.acesso.lower() == 'contabilidade':
            # Inicializar a MainWindow do App na tela de autorizar pix.
            self.ui.AutorizarPix.setVisible(True)
            self.telaAutorizarPix()
            self.ui.CadastrarUsuario.setVisible(False)
            self.ui.GerarQrCode.setVisible(False)
            self.ui.ConsultaPgto.setVisible(False)
            self.ui.Imprimir.setVisible(False)

        else:
            # Inicializar a MainWindow do App na tela de geração de Qr Code.
            self.telaGerarQrCode()
            self.ui.campo_usuario_atual.setText(f"Usuário: {self.usuario}")
            self.ui.CadastrarUsuario.setVisible(False)
            self.ui.AutorizarPix.setVisible(False)


    def aplicaTema(self, temaAtual: Tema):
    
        self.ui.right_panel.setStyleSheet('''*{
        background-color: rgb'''+f'{(temaAtual.rightSideMenuBgColor)}'+''';
        font: 14pt "MS Shell Dlg 2";
        }

        QPushButton {
            color: rgb'''+f'{(temaAtual.mainTextColor)}'+''';
            background-color: rgb'''+f'{(temaAtual.btnBgColor)}'+''';
            border: 0px solid;
            padding: 6px 9px;
            text-align:center;
            border-radius:5px;
            font: 16pt "MS Shell Dlg 2"
        }

        QPushButton:hover {
            color: rgb'''+f'{(temaAtual.mainTextColor)}'+''';
            background-color: rgb'''+f'{(temaAtual.keyColor2)}'+''';
            text-align:center;
            padding: 6px 9px;
            border-radius:5px;
            font: 16pt "MS Shell Dlg 2"
        }

        QPushButton:pressed {
            background-color: rgb'''+f'{(temaAtual.corDestaque1)}'+''';
            color: rgb'''+f'{(temaAtual.btnBgColor)}'+''';
            text-align:center;
            padding: 5px 7px;
            border-radius:5px;
            font: 15pt "MS Shell Dlg 2"
        }

        QLineEdit{
            background: transparent;
            border: none;
            border-bottom:3px solid rgba'''+f'{(temaAtual.inputTextBgColor)}'+''';
            padding: 5px;
            font: 16pt "MS Shell Dlg 2";
            color: rgb'''+f'{(temaAtual.mainTextColor)}'+''';
        }

        QLabel{
            color: rgb'''+f'{(temaAtual.mainTextColor)}'+''';
            font: 15pt "MS Shell Dlg 2";
        }
        
        QTableWidget{
        font: 11pt "MS Shell Dlg 2";
        background-color: rgb'''+f'{(temaAtual.tableItemBgColor)}'+''';
        alternate-background-color: rgb'''+f'{(temaAtual.sideMenuHoverBgColor)}'+''';
        }

        QComboBox{
        border: 2px solid rgb'''+f'{(temaAtual.corDestaque1)}'+''';
        color: rgb'''+f'{(temaAtual.mainTextColor)}'+''';
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
        border: 2px solid rgb'''+f'{(temaAtual.mainTextColor)}'+''';
        }

        QComboBox QListView {
        color: rgb'''+f'{(temaAtual.mainTextColor)}'+''';
        font: 13pt "MS Shell Dlg 2";
        border: 1px solid rgba(0,0,0,10%);
        padding: 5px;
        background-color: rgb'''+f'{(temaAtual.sideMenuHoverBgColor)}'+''';
        }

        QComboBox QListView:item{
        padding-left: 10px;
        background-color: rgb'''+f'{(temaAtual.sideMenuHoverBgColor)}'+''';
        }

        QComboBox QListView:item:hover{
        background-color: rgb'''+f'{(temaAtual.btnBgColor)}'+''';
        }

        QComboBox QListView:item:selected{
        background-color: rgb'''+f'{(temaAtual.btnBgColor)}'+''';
        }
        ''')

        self.ui.frame_left_base.setStyleSheet('''*{
            background-color: rgb'''+f'{(temaAtual.sideMenuBgColor)}'+''';
            border: 0px solid;
        }
        QPushButton {
            color: rgb'''+f'{(temaAtual.leftMenuTextColor)}'+''';
            background-color: rgb'''+f'{(temaAtual.sideMenuBgColor)}'+''';
            border: 0px solid;
            padding: 6px 9px;
            text-align:left;
        }
        QPushButton:hover {
            background-color: rgb'''+f'{(temaAtual.sideMenuHoverBgColor)}'+''';
            text-align:left;
            padding: 6px 9px;
            border-radius:6px;
            border: 2px solid rgb'''+f'{(temaAtual.corDestaque1)}'+''';
        }''')

        self.ui.top_center_frame.setStyleSheet('''
        background-color: rgb'''+f'{(temaAtual.sideMenuBgColor)}'+''';
        ''')

        self.ui.label_titulo.setStyleSheet('''
        color: rgb'''+f'{(temaAtual.leftMenuTextColor)}'+''';
        ''')

        self.ui.top_left_frame.setStyleSheet('''
        background-color: rgb'''+f'{(temaAtual.sideMenuBgColor)}'+''';
        ''')

        self.ui.label_creditos.setStyleSheet('''
        color: rgb'''+f'{(temaAtual.mainTextColor)}'+''';
        font: 10pt "MS Shell Dlg 2";
        ''')
        
        config['APARENCIA']['TEMA'] = temaAtual.nomeTema
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        self.telaSettings()
                                           

    def sairSistema(self):
        self.db.closeUsers()
        self.dbPix.closeDB()
        self.close()


    def telaAutorizarPix(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_autorizar)

        # Definir largura das colunas
        self.ui.tableBuscaEAutorizaPix.setColumnWidth(0, 130)
        self.ui.tableBuscaEAutorizaPix.setColumnWidth(1, 270)
        self.ui.tableBuscaEAutorizaPix.setColumnWidth(2, 155)
        self.ui.tableBuscaEAutorizaPix.setColumnWidth(3, 90)
        self.ui.tableBuscaEAutorizaPix.setColumnWidth(4, 157)
        self.ui.tableBuscaEAutorizaPix.setColumnWidth(5, 107)
        self.ui.tableBuscaEAutorizaPix.setColumnWidth(6, 100)

        # Destacar o menu selecionado no momento
        self.ui.AutorizarPix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            border: 2px solid rgb'''+f'{(self.temaAtual.corDestaque1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.GerarQrCode.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')                                
        self.ui.Imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.ConsultaPgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.CadastrarUsuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.Settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def telaGerarQrCode(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_gerar)

        # Destacar o menu selecionado no momento
        self.ui.GerarQrCode.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            border: 2px solid rgb'''+f'{(self.temaAtual.corDestaque1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.Imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.ConsultaPgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.CadastrarUsuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.AutorizarPix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.Settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def telaImprimir(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_imprimir)

        # Destacar o menu selecionado no momento
        self.ui.Imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            border: 2px solid rgb'''+f'{(self.temaAtual.corDestaque1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.GerarQrCode.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.ConsultaPgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.CadastrarUsuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.AutorizarPix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.Settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def telaConsultar(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_consultar)
        self.ui.tableConsultaPix.setColumnWidth(0, 90)
        self.ui.tableConsultaPix.setColumnWidth(1, 310)
        self.ui.tableConsultaPix.setColumnWidth(2, 140)
        self.ui.tableConsultaPix.setColumnWidth(3, 115)
        self.ui.tableConsultaPix.setColumnWidth(4, 210)      
        self.carregarConsulta(self.sigla)
        # Destacar o menu selecionado no momento
        self.ui.ConsultaPgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            border: 2px solid rgb'''+f'{(self.temaAtual.corDestaque1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.GerarQrCode.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.Imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.CadastrarUsuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.AutorizarPix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.Settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def telaSettings(self):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)

            # Destacar o menu selecionado no momento
            self.ui.Settings.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
                                                background-color: rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                                border: 2px solid rgb'''+f'{(self.temaAtual.corDestaque1)}'+''';
                                                padding: 6px 9px;
                                                text-align:left;
                                                border-radius:6px;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.Imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
                                                background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                                border: 0px solid;
                                                padding: 6px 9px;
                                                text-align:left;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.ConsultaPgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
                                                background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                                border: 0px solid;
                                                padding: 6px 9px;
                                                text-align:left;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.CadastrarUsuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
                                                background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                                border: 0px solid;
                                                padding: 6px 9px;
                                                text-align:left;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.AutorizarPix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
                                                background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                                border: 0px solid;
                                                padding: 6px 9px;
                                                text-align:left;
                                            }
                                            QPushButton::hover {
                                                background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                                text-align:left;
                                                padding: 6px 9px;
                                                border-radius:6px;
                                            }
                                            ''')
            self.ui.GerarQrCode.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def converterFloatReais(self, valor) -> str:
        valor_formatado = locale.currency(valor, grouping=True)
        return str(valor_formatado)


    def converterDiaHora(self, diaHora) -> str:
        hora_formatada = diaHora.strftime("%d-%m-%Y %H:%M")
        return hora_formatada


    def mudaFonteTabelaPix(self):
        ok, self.fontTable = QFontDialog.getFont(self.ui.tableBuscaEAutorizaPix)
        if ok:
            self.ui.tableBuscaEAutorizaPix.setFont(self.fontTable)
            self.ui.tableConsultaPix.setFont(self.fontTable)
            self.ui.tableBuscaEAutorizaPix.resizeColumnsToContents()
            self.ui.tableBuscaEAutorizaPix.resizeRowsToContents()
            self.ui.tableConsultaPix.setFont(self.fontTable)
            self.ui.tableConsultaPix.resizeColumnsToContents()
            self.ui.tableConsultaPix.resizeRowsToContents()
        self.carregarConsulta(self.sigla)
        self.carregarAlteraPix(
                self.ui.campo_buscar_apresentante.text(),
                self.ui.campo_buscar_id.text())

        config['APARENCIA']['FONTE'] = str(self.fontTable)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


    def carregarAlteraPix(self,name,id):
        # Inicializa limpando a tabela
        self.ui.tableBuscaEAutorizaPix.setRowCount(0)
        self.ui.resultado_busca_autoriza.clear()
        self.ui.tableBuscaEAutorizaPix.setSortingEnabled(False)
        if id != '' and name == '':
            self.ui.tableBuscaEAutorizaPix.setRowCount(1)
            pagamento = self.dbPix.searchPixByID(id)
            if pagamento == None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Não encontrado')
                msg.setText('Nenhum registro com o ID informado. Verificar!')
                msg.exec_()
                self.ui.resultado_busca_autoriza.clear()
                self.ui.resultado_busca_autoriza.setText('Resultado da busca: nenhum registro encontrado')
            else:
                self.ui.campo_buscar_apresentante.setText('')
                self.ui.resultado_busca_autoriza.setText(
                    f'Resultado da busca: 1 registro encontrado')
                reais = self.converterFloatReais(pagamento[2])
                diaHora = self.converterDiaHora(pagamento[4])
                for coluna in range(0,9,1):
                    if coluna == 2:
                        item_atual = QTableWidgetItem(reais)
                        item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                            self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                        item_atual.setFont(self.fontTable)
                        self.ui.tableBuscaEAutorizaPix.setItem(0, 
                            coluna, item_atual)
                    elif coluna == 4:
                        item_atual = QTableWidgetItem(diaHora)
                        item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                            self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                        item_atual.setFont(self.fontTable)
                        self.ui.tableBuscaEAutorizaPix.setItem(0, 
                            coluna, item_atual)
                    else:
                        if coluna == 6 or coluna == 3:
                            # Se for a última coluna, verifica se o valor é none pra retornar ''
                            # Se não for none, aplica a sigla do usuário em maiúsculas
                            if str(pagamento[coluna]) == 'None':
                                item_atual = QTableWidgetItem('')
                            else:
                                item_atual = QTableWidgetItem(str(pagamento[coluna]).upper())
                        elif coluna == 8:
                            # Se for a última coluna, verifica se o valor é none pra retornar ''
                            # Se não for none, aplica a sigla do usuário em maiúsculas
                            if str(pagamento[coluna]) == 'None':
                                item_atual = QTableWidgetItem('')
                            else:
                                item_atual = QTableWidgetItem(str(pagamento[coluna]))
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                            self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableBuscaEAutorizaPix.setItem(0, 
                                coluna - 1, item_atual)
                            item_atual.setFont(self.fontTable)
                        else:
                            item_atual = QTableWidgetItem(str(pagamento[coluna]))
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableBuscaEAutorizaPix.setItem(0, 
                                coluna, item_atual)
                            item_atual.setFont(self.fontTable)
            self.ui.tableBuscaEAutorizaPix.resizeColumnsToContents()
            self.ui.tableBuscaEAutorizaPix.resizeRowsToContents()
        elif name != '' and id == '':
            # Verificar o estado do filtro limite de registros
            if self.ui.combo_limite_altera.currentIndex() == 0:
                limite = 10
            elif self.ui.combo_limite_altera.currentIndex() == 1:
                limite = 30
            elif self.ui.combo_limite_altera.currentIndex() == 1:
                limite = 50
            else:
                limite = 100 

            # Verificar o estado do filtro status dos pagamentos
            if self.ui.combo_filtro_alterapix.currentIndex() == 0:
                filtro = ''
            elif self.ui.combo_filtro_alterapix.currentIndex() == 1:
                filtro = 'aguardando'
            else:
                filtro = 'pago'

            # Verificar o estado do filtro de data
            if self.ui.combo_filtro_data_alterapix.currentIndex() == 0:
                filtroData = ''
            else:
                filtroData = 'Data'

            # Repassa a data escolhida na caixa de seleção de data em formato texto.
            dataBusca = self.ui.filtro_dia_alterapix.text()

            pagamentos = self.dbPix.searchPixByName(name, limite, filtro, filtroData, dataBusca)
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
                self.ui.resultado_busca_autoriza.clear()
                self.ui.resultado_busca_autoriza.setText('Resultado da busca: nenhum registro encontrado')
            else:
                self.ui.campo_buscar_id.setText('')
                self.ui.resultado_busca_autoriza.clear()
                self.ui.resultado_busca_autoriza.setText(
                    f'Resultado da busca: {len(pagamentos)} registro(s) encontrado(s)')
                linha = 0
                self.ui.tableBuscaEAutorizaPix.setRowCount(len(pagamentos))
                for pagamento in pagamentos:
                    reais = self.converterFloatReais(pagamento[2])
                    diaHora = self.converterDiaHora(pagamento[4])
                    for coluna in range(0,9,1):
                        if coluna == 2:
                            item_atual = QTableWidgetItem(reais)
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                            self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableBuscaEAutorizaPix.setItem(linha, 
                            coluna, item_atual)
                        elif coluna == 4:
                            item_atual = QTableWidgetItem(diaHora)
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                            self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableBuscaEAutorizaPix.setItem(linha, 
                            coluna, item_atual)
                            item_atual.setFont(self.fontTable)
                        else:
                            if coluna == 6 or coluna == 3:
                                # Se for a última coluna, verifica se o valor é none pra retornar ''
                                # Se não for none, aplica a sigla do usuário em maiúsculas
                                if str(pagamento[coluna]) == 'None':
                                    item_atual = QTableWidgetItem('')
                                else:
                                    item_atual = QTableWidgetItem(str(pagamento[coluna]).upper())
                            elif coluna == 8:
                                # Se for a última coluna, verifica se o valor é none pra retornar ''
                                # Se não for none, aplica a sigla do usuário em maiúsculas
                                if str(pagamento[coluna]) == 'None':
                                    item_atual = QTableWidgetItem('')
                                else:
                                    item_atual = QTableWidgetItem(str(pagamento[coluna]))
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableBuscaEAutorizaPix.setItem(linha, 
                                    coluna - 1, item_atual)
                                item_atual.setFont(self.fontTable)
                            else:
                                item_atual = QTableWidgetItem(str(pagamento[coluna]))
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                    self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableBuscaEAutorizaPix.setItem(linha, 
                                    coluna, item_atual)
                                item_atual.setFont(self.fontTable)
                    linha += 1
            self.ui.tableBuscaEAutorizaPix.resizeColumnsToContents()
            self.ui.tableBuscaEAutorizaPix.resizeRowsToContents()
        elif name == '' and id == '':
            # Verificar o estado do filtro limite de registros
            if self.ui.combo_limite_altera.currentIndex() == 0:
                limite = 10
            elif self.ui.combo_limite_altera.currentIndex() == 1:
                limite = 30
            elif self.ui.combo_limite_altera.currentIndex() == 1:
                limite = 50
            else:
                limite = 100 

            # Verificar o estado do filtro status dos pagamentos
            if self.ui.combo_filtro_alterapix.currentIndex() == 0:
                filtro = ''
            elif self.ui.combo_filtro_alterapix.currentIndex() == 1:
                filtro = 'aguardando'
            else:
                filtro = 'pago'

            # Verificar o estado do filtro de data
            if self.ui.combo_filtro_data_alterapix.currentIndex() == 0:
                filtroData = ''
            else:
                filtroData = 'Data'
            
            # Repassa a data escolhida na caixa de seleção de data em formato texto.
            dataBusca = self.ui.filtro_dia_alterapix.text()

            pagamentos = self.dbPix.searchPixByName('', limite, filtro, filtroData, dataBusca)
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
                self.ui.resultado_busca_autoriza.clear()
                self.ui.resultado_busca_autoriza.setText('Resultado da busca: nenhum registro encontrado')
            else:    
                self.ui.campo_buscar_id.setText('')
                self.ui.resultado_busca_autoriza.setText(
                    f'Resultado da busca: {len(pagamentos)} registro(s) encontrado(s)')
                linha = 0
                self.ui.tableBuscaEAutorizaPix.setRowCount(len(pagamentos))
                for pagamento in pagamentos:
                    reais = self.converterFloatReais(pagamento[2])
                    diaHora = self.converterDiaHora(pagamento[4])
                    for coluna in range(0,9,1):
                        if coluna == 2:
                            item_atual = QTableWidgetItem(reais)
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableBuscaEAutorizaPix.setItem(linha, 
                                coluna, item_atual)
                        elif coluna == 4:
                            item_atual = QTableWidgetItem(diaHora)
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableBuscaEAutorizaPix.setItem(linha, 
                                coluna, item_atual)
                            item_atual.setFont(self.fontTable)
                        else:
                            if coluna == 6 or coluna == 3:
                                # Se for a última coluna, verifica se o valor é none pra retornar ''
                                # Se não for none, aplica a sigla do usuário em maiúsculas
                                if str(pagamento[coluna]) == 'None':
                                    item_atual = QTableWidgetItem('')
                                else:
                                    item_atual = QTableWidgetItem(str(pagamento[coluna]).upper())
                            elif coluna == 8:
                                # Se for a última coluna, verifica se o valor é none pra retornar ''
                                # Se não for none, aplica a sigla do usuário em maiúsculas
                                if str(pagamento[coluna]) == 'None':
                                    item_atual = QTableWidgetItem('')
                                else:
                                    item_atual = QTableWidgetItem(str(pagamento[coluna]))
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableBuscaEAutorizaPix.setItem(linha, 
                                    coluna - 1, item_atual)
                                item_atual.setFont(self.fontTable)
                            else:
                                item_atual = QTableWidgetItem(str(pagamento[coluna]))
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                    self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableBuscaEAutorizaPix.setItem(linha, 
                                    coluna, item_atual)
                                item_atual.setFont(self.fontTable)

                    linha += 1
            self.ui.tableBuscaEAutorizaPix.resizeColumnsToContents()
            self.ui.tableBuscaEAutorizaPix.resizeRowsToContents()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle('Busca em duplicidade')
            msg.setText('Informar somente o nome ou somente o ID.')
            msg.exec_()

        self.ui.tableBuscaEAutorizaPix.setSortingEnabled(True)


    def carregarConsulta(self, caixa):
        # Inicializa limpando a tabela
        print('Carrega consulta pix')
        self.ui.tableConsultaPix.setRowCount(0)
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
        elif self.ui.combo_limite_consultapix.currentIndex() == 1:
            limite = 50
        else:
            limite = 100 


        # Verificar o estado do filtro de data
        if self.ui.combo_filtro_data_consultapix.currentIndex() == 0:
            filtroData = ''
        else:
            filtroData = 'Data'

        # Repassa a data escolhida na caixa de seleção de data em formato texto.
        dataBusca = self.ui.filtro_data_consultapix.text()

        if idPix == '':
            pagamentos = self.dbPix.searchPixByCaixa(
                caixa=caixa, 
                limite=limite,
                filtro=filtro,
                filtroData=filtroData,
                apresentante=apresentante,
                data=dataBusca
            )
        else:
            pagamentos = self.dbPix.searchPixByIDCaixa(
                txtID=idPix,
                caixa=caixa
            )
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
            self.ui.resultado_busca_autoriza.clear()
            self.ui.resultado_busca_autoriza.setText('Resultado da busca: nenhum registro encontrado')
        else:
            linha = 0
            self.ui.tableConsultaPix.setRowCount(len(pagamentos))
            self.ui.tableConsultaPix.setSortingEnabled(False)
            if idPix == '':
                for pagamento in pagamentos:
                    reais = self.converterFloatReais(pagamento[2])
                    diaHora = self.converterDiaHora(pagamento[4])
                    for coluna in range(0,9,1):
                        if coluna != 3:
                            if coluna == 2:
                                item_atual = QTableWidgetItem(reais)
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                    self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableConsultaPix.setItem(linha, 
                                    coluna, item_atual)
                            elif coluna == 4:
                                item_atual = QTableWidgetItem(diaHora)
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                    self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableConsultaPix.setItem(linha, 
                                    coluna - 1, item_atual)
                                item_atual.setFont(self.fontTable)
                            elif coluna == 5:   
                                item_atual = QTableWidgetItem(str(pagamento[coluna]))
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                    self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableConsultaPix.setItem(linha, 
                                    coluna - 1, item_atual)
                            elif coluna == 8:
                                if str(pagamento[coluna]) == 'None':
                                    pgtoColuna = ''
                                else:
                                    pgtoColuna = str(pagamento[coluna])
                                item_atual = QTableWidgetItem(pgtoColuna)
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                    self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableConsultaPix.setItem(linha, 
                                    coluna - 3, item_atual)
                            else:   
                                item_atual = QTableWidgetItem(str(pagamento[coluna]))
                                item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                    self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                                item_atual.setFont(self.fontTable)
                                self.ui.tableConsultaPix.setItem(linha, 
                                    coluna, item_atual)
                                item_atual.setFont(self.fontTable)
                    linha += 1
                    self.ui.tableConsultaPix.resizeColumnsToContents()
                    self.ui.tableConsultaPix.resizeRowsToContents()
            else:
                reais = self.converterFloatReais(pagamentos[2])
                diaHora = self.converterDiaHora(pagamentos[4])
                for coluna in range(0,6,1):
                    if coluna != 3:
                        if coluna == 2:
                            item_atual = QTableWidgetItem(reais)
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableConsultaPix.setItem(linha, 
                                coluna, item_atual)
                        elif coluna == 4:
                            item_atual = QTableWidgetItem(diaHora)
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableConsultaPix.setItem(linha, 
                                coluna - 1, item_atual)
                            item_atual.setFont(self.fontTable)
                        elif coluna == 5:   
                            item_atual = QTableWidgetItem(str(pagamentos[coluna]))
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableConsultaPix.setItem(linha, 
                                coluna - 1, item_atual)
                        else:   
                            item_atual = QTableWidgetItem(str(pagamentos[coluna]))
                            item_atual.setTextColor(QColor(self.temaAtual.mainTextColor[0],
                                self.temaAtual.mainTextColor[1],self.temaAtual.mainTextColor[2]))
                            item_atual.setFont(self.fontTable)
                            self.ui.tableConsultaPix.setItem(linha, 
                                coluna, item_atual)
                            item_atual.setFont(self.fontTable)
                linha += 1
                self.ui.tableConsultaPix.resizeColumnsToContents()
                self.ui.tableConsultaPix.resizeRowsToContents()
        self.ui.tableConsultaPix.setSortingEnabled(True)


    def telaCadastrarUsuario(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_cadastrar)
        self.ui.CadastrarUsuario.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            border: 2px solid rgb'''+f'{(self.temaAtual.corDestaque1)}'+''';
                                            padding: 6px 9px;
                                            text-align:left;
                                            border-radius:6px;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.GerarQrCode.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.Imprimir.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.ConsultaPgto.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')
        self.ui.AutorizarPix.setStyleSheet('''QPushButton {color: rgb'''+f'{(self.temaAtual.leftMenuTextColor)}'+''';
	                                        background-color: rgb'''+f'{(self.temaAtual.sideMenuBgColor)}'+''';
                                            border: 0px solid;
                                            padding: 6px 9px;
                                            text-align:left;
                                        }
                                        QPushButton::hover {
                                            background-color:rgb'''+f'{(self.temaAtual.sideMenuHoverBgColor)}'+''';
                                            text-align:left;
                                            padding: 6px 9px;
                                            border-radius:6px;
                                        }
                                        ''')


    def cadastraUsuario(self):
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


    def limparCamposQrCode(self):
        print("Limpar campos")
        self.ui.campo_apresentante.setText('')
        self.ui.campo_cpf_apresentante.setText('')
        self.ui.campo_valor.setText('')
        self.ui.txt_id_pix.setText('ID Pix: ')


    def limparCamposCadastro(self):
        print("Limpar campos")
        self.ui.combo_tipo_usuario.setCurrentIndex(0)
        self.ui.campo_usuario.setText('')
        self.ui.campo_nome_completo.setText('')
        self.ui.campo_senha.setText('')
        self.ui.campo_repetir_senha.setText('')


    def verificaCPF(self, cpf: str):
        cpf_digitos = ''
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

        for n in numbers:
            cpf_digitos = cpf_digitos + str(n)
        erro = False

        return erro, cpf_digitos


    def geraQrCode(self, apresentante, valor, cpf):
        erroPix = False
        print("Gerar QrCode")
        identificador = uuid.uuid4()
        txtId = geradorID(str(identificador))
        pgto = Pagamento(idTx=txtId,
                       nome=apresentante,
                       valor=valor,
                       copiaCola='')
        
        depositoInicial = pgto.valor
        valor_decimal = depositoInicial.replace('.', '')
        valor_decimal = valor_decimal.replace(',', '.')

        # Validar dados antes de gerar QRCode/PDF e gravar no banco
        if len(pgto.idTx) < 8:
            erroPix = True
            self.erroDadosPix('Não foi possível gerar o ID do Pix.')
        
        if len(pgto.nome) < 8:
            erroPix = True
            self.erroDadosPix('Informar pelo menos um nome e sobrenome.')

        cpf_informado = self.ui.campo_cpf_apresentante.text()
        err, cpf = self.verificaCPF(cpf_informado)
        if err:
            erroPix = True
            self.erroDadosPix('O CPF informado está incorreto.')

        try:
            valorPix=float(valor_decimal)
        except Exception as error:
            erroPix = True
            self.erroDadosPix('Formato de valor inválido, verificar. (ex.: 24.145,00)')
        
        if not erroPix:
            # Gerar QrCode com os dados preenchidos.
            self.ui.txt_id_pix.setText(f"ID Pix: {pgto.idTx}")

            #print(rgi.Nome, pgto.nome, rgi.ChavePix, pgto.valor, rgi.Cidade, pgto.idTx)
            payload = Payload(RGI_NOME, pgto.nome, RGI_CHAVE_PIX, valor_decimal, RGI_CIDADE, pgto.idTx)
            pixCopiaCola = payload.gerarPayload()
            pgto.copiaCola = pixCopiaCola
            # Gerar Arquivo PDF com os dados + QrCode
            pdf = PDF()
            pdf.print_chapter(pgto.nome, pgto.valor, pgto.idTx, pgto.copiaCola)
            pdf.output(ADOBE_PDF_FILE, 'F')

            # Gravar pix no banco de dados PostgreSQL
            try:
                self.dbPix.insertPix(txtID=pgto.idTx, nomeApresentante=pgto.nome, valor=valorPix,
                                createdBy=self.sigla, status='aguardando', cpf=cpf)
            except Exception as error:
                self.erroDadosPix(error)

            # Abrir qrquivo PDF para conferência dos dados
            cmd = '"{}" "{}"'.format(ADOBE_READER, ADOBE_PDF_FILE)
            subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def erroDadosPix(self, texto):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Erro ao gerar o Pix')
        msg.setText(f'Erro! {texto}')
        msg.exec_()


    def slideLeftMenu(self):
        width = self.ui.frame_left_base.width()

        if width == 45:
            newWidth = 235
            self.ui.Menu.setStyleSheet('''icon: url(:/icons/icons/chevron-left.svg);
                                        padding: 6px 9px;''')
        else:
            newWidth = 45
            self.ui.Menu.setStyleSheet('''icon: url(:/icons/icons/menu.svg);
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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    login_form = LoginWindow()
    login_form.show()
    sys.exit(app.exec_())
