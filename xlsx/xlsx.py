import xlsxwriter
from datetime import datetime



class Planilha:
    def __init__(self, nomeplanilha: str, linhas: int):
        
        self.nome_arquivo_xls = nomeplanilha
        self.linhas_planilha = linhas
        self.criaPlanilha()
    

    def diaCorrente(self):
        data = datetime.today()
        strData = data.strftime('%d/%m/%Y')
        return strData


    def criaPlanilha(self):
        ultima_linha = self.linhas_planilha
        self.workbook = xlsxwriter.Workbook(self.nome_arquivo_xls)
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.set_landscape()
        self.worksheet.add_table(f'A3:J{ultima_linha+3}',{'header_row' : False})


    def criar_titulo(self, titulo: str):
        self.worksheet.set_row(0, 25)
        mesclar_celula = self.workbook.add_format({
                                            'bold': 1,
                                            'border': 2,
                                            'font_size': 14,
                                            'align': 'center',
                                            'valign': 'vcenter'})
        self.worksheet.merge_range('A1:J1', titulo, mesclar_celula)


    def criar_cabecalho(self, colunas):
        letras_coluna = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        format = self.workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': 1, 'border': 1})
        self.worksheet.set_row(1, 6)
        self.worksheet.set_column(0, 0, 10)
        self.worksheet.set_column(1, 1, 11)
        self.worksheet.set_column(2, 2, 30)
        self.worksheet.set_column(3, 3, 15)
        self.worksheet.set_column(4, 4, 5)
        self.worksheet.set_column(5, 5, 11)
        self.worksheet.set_column(6, 6, 8)
        self.worksheet.set_column(7, 7, 4)
        self.worksheet.set_column(8, 8, 9)
        for i, nome_coluna in enumerate(colunas):
            celula = letras_coluna[i].upper() + '3'
            self.worksheet.write(celula, nome_coluna, format)


    def escrever(self, local: str, campo: any, negrito: bool, valor: bool):
        # Formatar texto em negrito
        if negrito:
            self.negrito = self.workbook.add_format({'bold': True})
            self.worksheet.write(local, campo, self.negrito)
        else:
            self.negrito = self.workbook.add_format({'bold': False})

        if valor:
            self.currency_format = self.workbook.add_format({'num_format': 'R$ #,##0.00'})
            self.worksheet.write(local, campo, self.currency_format)
        else:
            self.worksheet.write(local, campo, self.negrito)
        
    
    def fecha_planilha(self):
        self.workbook.close()

if __name__ == '__main__':
    planilha = Planilha('relatorio_teste.xlsx',linhas=1)
    colunas = ['PixID', 'Data', 'Nome', 'Valor', 'Caixa', 'Situação', 'Liberado', 'Ano', 'NumCert', 'NumProt']
    planilha.criar_titulo('Relatório de Pagamentos pix do dia: ' + planilha.diaCorrente())
    planilha.criar_cabecalho(colunas)
    planilha.escrever('A4', 125, False, False)
    planilha.escrever('B4', '09/08/2023', False, False)
    planilha.escrever('C4', 'Eduardo Rossini', False, False)
    planilha.escrever('D4', 741526.09, False, valor=True)
    planilha.escrever('E4', 'isa', False, False)
    planilha.escrever('F4', 'Pago', False, False)
    planilha.escrever('G4', 'bra', False, False)
    planilha.escrever('H4', 23, False, False)
    planilha.escrever('I4', 10258, False, False)
    planilha.escrever('J4', 502655, False, False)
    
    planilha.fecha_planilha()