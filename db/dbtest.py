import sqlite3
import bcrypt

db = sqlite3.connect('banco.db')
acessos = ['administrador', 'caixa', 'contabil']
cursor = db.cursor()
sigla = 'edu'
password = ''
acesso = 'administrador'
nomeusuario = 'Eduardo Rossini Xavier'

acessoByte = acesso.encode('utf-8')
pwdByte = password.encode('utf-8')
salt = bcrypt.gensalt()
hashPwd = bcrypt.hashpw(pwdByte, salt)
hashAcesso = bcrypt.hashpw(acessoByte, salt)

# cursor.execute('''DROP TABLE IF EXISTS users''')

cursor.execute('''CREATE TABLE IF NOT EXISTS users(username CHAR, password CHAR, access CHAR)''')

cursor.execute('''INSERT INTO users(user, username, password, access) 
VALUES(?,?,?,?)''', (sigla, nomeusuario, hashPwd, hashAcesso))

cursor.execute('''SELECT * FROM users WHERE username=?''', (nomeusuario,))
found = cursor.fetchone()
storedPwd = found[1]
storedAcesso = found[2]

newPwd = '123456'
listaAcessos = ['administrador', 'caixa', 'contabil']
typedPwd = newPwd.encode('utf-8')

passwordOk = bcrypt.checkpw(typedPwd, storedPwd)

for acesso in listaAcessos:
    chkAcesso = acesso.encode('utf-8')
    if bcrypt.checkpw(chkAcesso, storedAcesso):
        acessoUsuario = acesso
        break

if passwordOk:
    print(f'Credenciais corretas para o usuário {nomeusuario} com acesso: {acessoUsuario}')
else:
    print('Credenciais incorretas para o usuário informado.')

cursor.close()
db.commit()
db.close()

