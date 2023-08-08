# SisPag-Pix por Eduardo Rossini Xavier

## Programa para geração de pagamentos Pix para o cartório onde trabalho, como desenvolvedor em Python.

Versão 3.4
- Na criação de um novo solicitante, se o usuário digitar o nome todas em maiúsculas o nome sempre
será repassado para somente primeiras em maiúsculas com a função title(), assim tendo uma visão
mais homogênea no relatório e na consulta de pagamentos, visto que alguns usuários ao digitar os 
nomes, o faziam com CAPS deixando as letras em maíusculas e causando uma poluição visual.
- Ao digitar enter no CPF, tendo o cadastro, após exibir o nome da parte solicitante o foco já vai para
o valor, reduzindo assim os cliques do mouse/tabs que o caixa precisa dar.
- Acerto no nome de PIX para Pix, pois não é sigla e sim nome próprio, correção de versão e ano na 
barra de status do sistema.


Versão 3.3
- Corrigidos os acessos do grupo de usuários administradores para somente terem opções de configurações
e testes de relatórios e teste de envio de e-mail, opções de criar pagamento, consultar etc. não
estão mais disponíveis para esse grupo de usuário, pois já se passou a fase de testes.
- Corrigido um erro onde a sigla do usuário dependendo da digitação inicial podia ser repassada
com letras em maíusculas.

Versão 3.2
- Inserida opção de teste de e-mail para contas de usuário administrador, assim ao configurar
o sistema no computador do usuário o responsável do TI tem uma opção de teste dentro do
menu de configurações onde clica para enviar um e-mail sem precisar gerar uma cobrança de teste.

Versão 3.1
- Inclusão de pesquisa de pagamentos QrCodes gerados em outros caixas, para permitir a liberação
mesmo que não tenha sido o próprio caixa que gerou a cobrança. Correção de falha na
busca de pessoas por CPF ou CNPJ onde a verificação de CNPJ válido não estava sendo 
feita corretamente.

Versão 3.0
- Implementado nessa nova versão o uso da "system tray" ou seja a barra de tarefas em segundo plano,
agora ao fechar o app sem encerrar pelo botão específico ele oculta a janela e fica disponível na
tray do sistema, em caso de pagamento pix efetuado pela parte é exibida uma notificação do windows
ainda que o usuário esteja com a janela oculta ou até mesmo trabalhando em outra aplicação.
- Ao clicar na notificação, o sistema automaticamente é exibido já na tela de consulta de pagamentos.


Versão 2.1
- Correções de bugs visuais e correção da geração de PDF quando o usuário esquece o PDF base aberto
após gerar o pagamento QrCode anterior. Caso aconteça, é gerado um pdf secundário de segurança
pára impressão do pagamento atual e aviso para o usuário, solicitando fechar o PDF após o uso.

Versão 2.0
- Não é mais necessário criar o códico copia e cola com as 750 posições, em vez disso
as informações do pagamento são enviadas pela API do Bradesco em uma chamada PUT e a API retorna
com o código copia e cola, para que seja gerado o QRCode para pagamento.

- Um app "servidor" foi desenvolvido que roda no servidor do cartório e fica fazendo consultas 
na API bradesco e atualizando o banco de dados interno, para que este sistema "cliente" que
roda nas computadores cliente do cartório possa acessar essas informações no banco de dados.
Funcionando assim é desnecessária a conexão dos clientes com a rede de internet, evitando
brechas de segurança e também necessidade de certificado para acesso em todas as máquinas.

- Também foi criada uma nova estrutura de banco de dados, visando colocá-lo pelo menos na 
2ª forma normal, evitando campo multivalorados e trabalhando com tabelas relacionais, separando
as entidades (solicitante, pagamento, certidao e protocolo) em tabelas separadas.


Versão 1.0
- O programa consiste em criar um pagamento utilizando o layout de 750 posições do bradesco, 
repassando esse pagamento para o Bradesco e consumindo da API as informações de status do 
pagamento (aguardando, cancelado, pago etc.)

- Inicialmente (enquanto aguardava-se a autorização do cartório para utilização do serviço)
foi desenvolvido para funcionar de modo manual, onde o setor de contabilidade iria efetuar
liberação manual de cada Pix cadastrado, mediante consulta de extrato, saldo na conta bancária

- Num segundo passo, atualmente, estou desenvolvendo um servidor que irá consumir automaticamente
da API de Pix do Bradesco, as informações e status dos pagamentos cadastrados. (Já desenvolvido)

Utiliza para criação da chave PIX, como base, o módulo criado por Alexsussa 
(https://github.com/Alexsussa/pixqrcodegen), porém foram feitas algumas modificações
para ficar de acordo com a necessidade de geração de pagamentos pelo manual PIX Bradesco,
versão 2.0.0: https://exclusive.bradesco/pix/assets/docs/api_pix_200.pdf (não é mais utilizado
mas fica a referência caso alguém queira criar códigos estáticos com valor, independente da 
API Pix do Bradesco)




## Instruções de uso:

É necessário utilizar as seguintes bibliotecas em python para rodar o sistema:

BCrypt (pip install bcrypt)

PsychoPG (pip install psycopg2)

PySide2 (pip install PySide2)

QrCode (pip install qrcode)

PyFPDF2 (pip install fpdf2)

uuid (pip install uuid) (Ka-Ping Yee's uuid)

XlsxWriter (pip install XlsxWriter)


## Opcional:

PyInstaller (pip install pyinstaller) somente se quiser criar um executável (ler a OBS¹).


## Modificações na GUI (interface gráfica de usuário)
Caso queira fazer alterações na GUI, basta instalar e utilizar o aplicativo QtDesigner 5
abrir os arquivos ".ui" dentro da pasta GUI e efetuar as modificações desejadas.
para rodar o arquivo py da gui criada executar o comando: 
Ex1.: pyside2-uic "C:\SisPag Pix\gui\main.ui" -o "C:\SisPag Pix\gui\ui_main.py"
ou
Ex2.: pyside2-uic "C:\SisPag Pix\gui\InsereProtocolo.ui" -o "C:\SisPag Pix\gui\ui_InsereProtocolo.py"

## Banco de dados
Neste projeto, utilizo o banco de dados sqlite (biblioteca já inclusa por padrão no python3), e Postres (psychopg2).
No banco de dados sqlite armazeno informações de login de usuários, nome, sigla, nível de acesso e senha.
Tanto a senha quanto o nível de acesso, são armazenados em hash utilizando o Bcrypt, para maior segurança dos dados
armazenados. Já o banco de dados Postgre é utilizado para armazenar os pagamentos pix em si, será acessado tanto pelos usuários,
cadastrando e alterando os pagamentos cadastrados bem como pelo servidor que será desenvolvido para consumir diretamente da API
Bradesco e gravar os dados no banco.


## Falta fazer...
- Criar um arquivo configer que utiliza variáveis de ambiente para login, evitando a necessidade de 
ter armazenado no arquivo config.ini as credenciais de login no banco de dados.
- Desenvolver servidor de consumo da API Bradesco, agora que o contrato de serviços com o Bradesco
já foi liberado pelo cartório - Feito! :)
- Criar executável - Feito! :)

OBS¹: Sobre o executável, para criar utilizo o Pyinstaller, porém vale ressaltar que para incluir bibliotecas adicionais que não sejam anexadas gerando erro de módulo faltando, basta copiar
a pasta do módulo que fica em: PythonX.XX\Lib\site-packages para dentro da pasta do executável
Sobre o config.ini, apresentou erros ao ficar fora da pasta raiz (C:\API_Bradesco), vou verificar
posteriormente, por enquanto mantenha o arquivo na raiz junto ao executável.

Em desenvolvimento e criado por Eduardo Rossini Xavier da Silva em dezembro de 2022.
