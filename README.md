# SisPag-Pix

## Programa para geração de pagamentos Pix para o cartório onde trabalho, como desenvolvedor em Python.

O programa consiste em criar um pagamento utilizando o layout de 750 posições do bradesco, 
repassando esse pagamento para o Bradesco e consumindo da API as informações de status do 
pagamento (aguardando, cancelado, pago etc.)

Inicialmente (enquanto aguardava-se a autorização do cartório para utilização do serviço)
foi desenvolvido para funcionar de modo manual, onde o setor de contabilidade iria efetuar
liberação manual de cada Pix cadastrado, mediante consulta de extrato, saldo na conta bancária

Num segundo passo, atualmente, estou desenvolvendo um servidor que irá consumir automaticamente
da API de Pix do Bradesco, as informações e status dos pagamentos cadastrados.

Utiliza para criação da chave PIX, como base, o módulo criado por Alexsussa 
(https://github.com/Alexsussa/pixqrcodegen), porém foram feitas algumas modificações
para ficar de acordo com a necessidade de geração de pagamentos pelo manual PIX Bradesco,
versão 2.0.0: https://exclusive.bradesco/pix/assets/docs/api_pix_200.pdf

## Instruções de uso:

É necessário utilizar as seguintes bibliotecas em python para rodar o sistema:

BCrypt (pip install bcrypt)

PsychoPG (pip install psycopg2)

PySide2 (pip install PySide2)

QrCode (pip install qrcode)

PyFPDF2 (pip install fpdf2)

uuid (pip install uuid) (Ka-Ping Yee's uuid)


## Modificações na GUI (interface gráfica de usuário)
Caso queira fazer alterações na GUI, basta instalar e utilizar o aplicativo QtDesigner 5
abrir os arquivos ".ui" dentro da pasta GUI e efetuar as modificações desejadas.

## Banco de dados
Neste projeto, utilizo o banco de dados sqlite (biblioteca já inclusa por padrão no python3), e Postres (psychopg2).
No banco de dados sqlite armazeno informações de login de usuários, nome, sigla, nível de acesso e senha.
Tanto a senha quanto o nível de acesso, são armazenados em hash utilizando o Bcrypt, para maior segurança dos dados
armazenados. Já o banco de dados Postgre é utilizado para armazenar os pagamentos pix em si, será acessado tanto pelos usuários,
cadastrando e alterando os pagamentos cadastrados bem como pelo servidor que será desenvolvido para consumir diretamente da API
Bradesco e gravar os dados no banco.

# Falta fazer...

Passar os dados de rgi.py para config.ini
criar um arquivo configer que utiliza variáveis de ambiente para login, evitando a necessidade de 
ter armazenado no arquivo config.ini as credenciais de login no banco de dados.
Desenvolver servidor de consumo da API Bradesco, agora que o contrato de serviços com o Bradesco
já foi liberado pelo cartório.