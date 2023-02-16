import xlsxwriter
from datetime import datetime



class Planilha:
    def __init__(self, nomeplanilha: str):
        
        self.nome_arquivo_xls = nomeplanilha
        self.criaPlanilha()
    
    def diaCorrente(self):
        data = datetime.today()
        strData = data.strftime('%d/%m/%Y')
        return strData

    def criaPlanilha(self):
        self.workbook = xlsxwriter.Workbook(self.nome_arquivo_xls)
        self.worksheet = self.workbook.add_worksheet()


    def criarTitulo(self, titulo: str):
        mesclar_celula = self.workbook.add_format({
                                            'bold': 1,
                                            'border': 1,
                                            'align': 'center',
                                            'valign': 'vcenter'})
        self.worksheet.merge_range('A1:E1', titulo, mesclar_celula)


    def criarCabecalho(self, colunas):
        letras_coluna = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        format = self.workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': 1, 'border': 1})
        self.worksheet.set_row(1, 6)
        for i, nome_coluna in enumerate(colunas):
            celula = letras_coluna[i].upper() + '3'
            self.worksheet.set_column(0, 0, 10)
            self.worksheet.set_column(1, 1, 30)
            self.worksheet.set_column(2, 2, 15)
            self.worksheet.set_column(3, 3, 5)
            self.worksheet.set_column(4, 4, 20)
            self.worksheet.write(celula, nome_coluna, format)

    def escrever(self, local: str, campo: any, negrito: bool, valor: bool):
        # Formatar texto em negrito
        if negrito:
            self.negrito = self.workbook.add_format({'bold': True})
            self.worksheet.write(local, campo, self.negrito)
        else:
            self.negrito = self.workbook.add_format({'bold': False})
            if valor:
                self.currency_format = self.workbook.add_format({'num_format': 'R$#,##0.00'})
                self.worksheet.write(local, campo, self.currency_format)
            else:
                self.worksheet.write(local, campo, self.negrito)
        
    
    def fechaPlanilha(self):
        self.workbook.close()

if __name__ == '__main__':
    planilha = Planilha('relatorio.xlsx')
    colunas = ['Nome', 'CPF', 'Valor', 'Protocolo']
    planilha.criarTitulo('Relatório de Pagamentos pix do dia: ' + planilha.diaCorrente())
    planilha.criarCabecalho(colunas)
    planilha.escrever('A4', 'Eduardo Rossini', False, False)
    planilha.escrever('B4', '106.626.727-80', False, False)
    planilha.escrever('C4', 741526.09, False, valor=True)
    planilha.escrever('D4', '22/25641', False, False)
    planilha.fechaPlanilha()