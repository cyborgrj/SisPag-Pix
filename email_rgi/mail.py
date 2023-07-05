import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

CONTA_PADRAO = 'cartoriorgirj@gmail.com'

def envia_email(nome_dest, email_dest, anexo, pix_copia_e_cola):
    status = ''
    message = MIMEMultipart()
    message["To"] = email_dest
    message["From"] = CONTA_PADRAO
    message["Subject"] = '2º Ofício de Registro de Imóveis/RJ - Solicitação de pagamento por Pix'

    body = f'''
    <font size=3>
    <b> Solicitação de pagamento por Pix - Cartório do 2º Ofício de Registro de Imóveis/RJ </b>
    </font>
    <br>
    <br>
    Prezado(a) Senhor(a) {nome_dest}, segue abaixo seu código Pix Copia e Cola:
    <br>

    Obs.: Certifique-se de selecionar todo o texto sublinhado, para garantir que o código seja aceito pelo aplicativo do banco.<br><br>
    <b><u><a name="copiaecola">{pix_copia_e_cola}</a></u></b>
    <br>
    <br>
    Anexo, segue o arquivo PDF com a imagem QRCode, caso queira escanear no aplicativo do banco.'''

    messageText = MIMEText(body,'html')
    message.attach(messageText)

    # body = f'''Prezado senhor {nome_dest}, segue abaixo seu código Pix Copia e Cola:<br>
    # {pix_copia_e_cola}<br>
    # Anexo, segue o arquivo PDF com a imagem QRCode, caso queira escanear no App.'''
    # messageBody = MIMEText(body)
    # message.attach(messageBody)

    binary_pdf = open(anexo, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name='dados para pagamento.pdf')
    payload.set_payload((binary_pdf).read())

    # enconding the binary into base64
    encoders.encode_base64(payload)

    # add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename='dados para pagamento.pdf')
    message.attach(payload)

    # pdf = MIMEApplication(open(anexo, 'rb').read())
    # pdf.add_header('Content-Disposition', 'attachment;filename=')
    # message.attach(pdf)

    email = CONTA_PADRAO
    #password incorreto para testes = 'trxnykgianxboom'
    password = 'lrukoabdjvlkmhlw'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    try:
        server.login(email,password)
    except Exception as error:
        print(f'Erro ao enviar e-mail: {error}')
        server.quit()
        return error
    else:
        status = 'sucesso'

    fromaddr = CONTA_PADRAO
    toaddrs  = email_dest
    try:
        server.sendmail(fromaddr,toaddrs,message.as_string())
    except Exception as error:
        print(f'Erro ao enviar e-mail: {error}')
        server.quit()
        return error
    else:
        status = 'sucesso'
    
    server.quit()
    return status

envia_email(
    nome_dest='Eduardo Rossini Xavier',
    email_dest='ajuda.apple@gmail.com',
    anexo=r'C:\SisPag Pix\src\dadospagamento.pdf',
    pix_copia_e_cola='''00020101021226860014BR.GOV.BCB.PIX2564qrpix.bradesco.com.br/qr/v2/63c8706d-6910-452d-b786-db348caf04d85204000053039865406134.755802BR5925RIO DE JANEIRO CARTORIO 26014RIO DE JANEIRO62070503***6304806D'''
)