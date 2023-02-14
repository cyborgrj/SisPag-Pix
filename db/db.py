import psycopg2
import sqlite3
import bcrypt

class DataBaseUsers():
    def __init__(self, dbname):
        self.dbname = dbname
        self.connectUsers()
    
    def connectUsers(self):
        try:
            self.db = sqlite3.connect(self.dbname)
        except Exception as error:
            print(f"Erro ao conectar: {error}")
        self.cursor = self.db.cursor()

    def closeUsers(self):
        try:
            self.db.close()
        except Exception as error:
            print(f'Erro ao fechar o banco SQLite3 (users): {error}')

    def insertUsers(self, user, password, access, username) -> str:
        self.cursor = self.db.cursor()
        sigla = user.lower()
        print('Início de cadastro de usuários')
        acessoByte = access.encode('utf-8')
        pwdByte = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashPwd = bcrypt.hashpw(pwdByte, salt)
        hashAcesso = bcrypt.hashpw(acessoByte, salt)
        self.cursor.execute('''SELECT * FROM users WHERE user=?''',(sigla,))
        found = self.cursor.fetchone()
        if found != None:
            print('Usuário já cadastrado!')
            return 'existente'
        else:
            self.cursor.execute('''INSERT INTO users(user, password, access, username) 
                            VALUES(?,?,?,?)''', (sigla, hashPwd, hashAcesso, username))
            self.cursor.close()
            self.db.commit()
            return 'sucesso'


    def checkUsers(self, user, password):
        found = None
        acessoUsuario = ''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute('''SELECT * FROM users WHERE user=?''', (user,))
        except Exception as error:
            print(f'Erro: {error}')
            return 'credenciais', 'incorretas'
        else:
            found = self.cursor.fetchone()
            if found != None:
                storedPwd = found[1]
                storedAcesso = found[2]
                username = found[3]
                listaAcessos = ['administrador', 'caixa', 'contabilidade']
            
                typedPwd = password.encode('utf-8')

                try:
                    passwordOk = bcrypt.checkpw(typedPwd, storedPwd)
                except:
                    return 'credenciais', 'incorretas'

                for acesso in listaAcessos:
                    chkAcesso = acesso.encode('utf-8')
                    if bcrypt.checkpw(chkAcesso, storedAcesso):
                        acessoUsuario = acesso
                        break

                if passwordOk and acessoUsuario != '':
                    self.cursor.close()
                    return username, acessoUsuario
                else:
                    self.cursor.close()
                    return 'credenciais', 'incorretas'
            else:
                self.cursor.close()
                return 'credenciais', 'incorretas'
        

class DataBasePix():
    def __init__(self, host, dbname, user, password, port):
        self.host = host
        self.dbname = dbname
        self.username = user
        self.pwd = password
        self.port_id = port
        self.connectDB()

    def connectDB(self):
        try:
            self.conn = psycopg2.connect(
                    host = self.host,
                    dbname = self.dbname,
                    user = self.username,
                    password = self.pwd,
                    port = self.port_id)

        except Exception as error:
            print(error)


    def insertPix(self, txtID, nomeApresentante, valor, createdBy, status, cpf):
        cursor = self.conn.cursor()
        insert_query = """INSERT INTO pix(txtid, name, valor, createdby, status, createdat, cpf) 
                        VALUES(%s,%s,%s,%s,%s,now(),%s)"""
        try:
            cursor.execute(insert_query,(txtID, nomeApresentante, valor, createdBy, status, cpf))
        except Exception as error:
            print(f'Erro ao inserir o pix: {error}')
        else:
            print(f'Pix de ID: {txtID} inserido com sucesso!')
            self.conn.commit()
        finally:
            cursor.close()


    def searchPixByName(self, nome, limite, estado, filtroData, data):
        nomesEncontrados = []
        cursor = self.conn.cursor()
        dia, mes, ano = data.split('/')
        inicioDia = f"{ano}-{mes}-{dia} 00:00:00"
        fimDia = f"{ano}-{mes}-{dia} 23:59:59"

        # Search query com regex iniciando com case insensitive (*) e 
        # aceitando palavras, espaços etc. tanto antes quanto após o nome pesquisado.
        if nome != '' and estado != '' and filtroData != '':
            search_query = f"""SELECT * FROM pix WHERE name ~* '^.*{nome}.*$' 
                        AND status = '{estado}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif nome != '' and estado == '' and filtroData != '':
            search_query = f"""SELECT * FROM pix WHERE name ~* '^.*{nome}.*$'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif nome == '' and estado != '' and filtroData != '':
            search_query = f"""SELECT * FROM pix WHERE status = '{estado}' 
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif nome == '' and estado == '' and filtroData != '':
            search_query = f"""SELECT * FROM pix WHERE createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtro de data desligado:                
        elif nome != '' and estado != '' and filtroData == '':
            search_query = f"""SELECT * FROM pix WHERE name ~* '^.*{nome}.*$' 
                        AND status = '{estado}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif nome != '' and estado == '' and filtroData == '':
            search_query = f"""SELECT * FROM pix WHERE name ~* '^.*{nome}.*$'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif nome == '' and estado != '' and filtroData == '':
            search_query = f"""SELECT * FROM pix WHERE status = '{estado}' 
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtros de data e status desligados (na posição "todos")
        else:
            search_query = f"""SELECT * FROM pix 
                        ORDER BY createdat DESC LIMIT {limite}"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {txtID}, Erro: {error}")
        else:
            nomesEncontrados = cursor.fetchall()
            self.conn.commit()
        finally:
            cursor.close()
            return nomesEncontrados


    def searchPixAguardando(self, data):
        pix_aguardando = []
        cursor = self.conn.cursor()

        dia, mes, ano = data.split('/')
        inicioDia = f"{ano}-{mes}-{dia} 00:00:00"
        fimDia = f"{ano}-{mes}-{dia} 23:59:59"
        
        filtro = 'aguardando'
        limite = 50
        search_query = f"""SELECT * FROM pix WHERE status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao buscar pagamentos pix com estatus aguardando")
        else:
            pix_aguardando = cursor.fetchall()
            self.conn.commit()
        finally:
            cursor.close()
        return(len(pix_aguardando))

    def searchPixByCaixa(self, caixa, limite, filtro, apresentante, filtroData, data) -> list:
        pgtosEncontrados = []
        cursor = self.conn.cursor()

        dia, mes, ano = data.split('/')
        inicioDia = f"{ano}-{mes}-{dia} 00:00:00"
        fimDia = f"{ano}-{mes}-{dia} 23:59:59"

        # Search query com nome do caixa para exibir os pagamentos gerados pelo mesmo.
        # Search query com regex iniciando com case insensitive (*) e 
        # aceitando palavras, espaços etc. tanto antes quanto após o nome pesquisado.
        if apresentante != '' and filtro != '' and filtroData != '':
            search_query = f"""SELECT * FROM pix WHERE name ~* '^.*{apresentante}.*$'
                        AND createdby = '{caixa}' 
                        AND status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante != '' and filtro == '' and filtroData != '':
            search_query = f"""SELECT * FROM pix WHERE name ~* '^.*{apresentante}.*$'
                        AND createdby = '{caixa}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtroData != '':
            search_query = f"""SELECT * FROM pix WHERE status = '{filtro}' 
                        AND createdby = '{caixa}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro == '' and filtroData != '':
            search_query = f"""SELECT * FROM pix WHERE createdat >= '{inicioDia}'
                        AND createdby = '{caixa}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtro de data desligado:                
        elif apresentante != '' and filtro != '' and filtroData == '':
            search_query = f"""SELECT * FROM pix WHERE name ~* '^.*{apresentante}.*$' 
                        AND createdby = '{caixa}'
                        AND status = '{filtro}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante != '' and filtro == '' and filtroData == '':
            search_query = f"""SELECT * FROM pix WHERE name ~* '^.*{apresentante}.*$'
                        AND createdby = '{caixa}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtroData == '':
            search_query = f"""SELECT * FROM pix WHERE status = '{filtro}' 
                        AND createdby = '{caixa}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtros de data e status desligados (na posição "todos")
        else:
            search_query = f"""SELECT * FROM pix WHERE createdby = '{caixa}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix do caixa {caixa}, Erro: {error}")
        else:
            pgtosEncontrados = cursor.fetchall()
            self.conn.commit()
        finally:
            cursor.close()
            return pgtosEncontrados


    def searchPixByIDCaixa(self, txtID, caixa) -> tuple:
            pixEncontrado: tuple
            cursor = self.conn.cursor()
            search_query = f"""SELECT * FROM pix WHERE txtid = '{txtID}'
                            AND createdby = '{caixa}'
                            """
            try:
                cursor.execute(search_query)
            except Exception as error:
                print(f"Erro ao localizar o pix de ID {txtID}, Erro: {error}")
            else:
                pixEncontrado = cursor.fetchone()
                self.conn.commit()
            finally:
                cursor.close()
                return pixEncontrado


    def searchPixByID(self, txtID) -> tuple:
        pixEncontrado: tuple
        cursor = self.conn.cursor()
        search_query = """SELECT * FROM pix WHERE txtid = %s"""
        try:
            cursor.execute(search_query,(txtID,))
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {txtID}, Erro: {error}")
        else:
            pixEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            return pixEncontrado


    def updatePix(self, txtID, updatedBy, status):
        cursor = self.conn.cursor()
        update_status_query = """UPDATE pix SET status = %s WHERE txtid = %s"""
        update_upBy_query = """UPDATE pix SET updatedby = %s WHERE txtid = %s"""
        update_upAt_query = """UPDATE pix SET updatedat = now() WHERE txtid = %s"""
        try:
            cursor.execute(update_status_query, (status, txtID))
            cursor.execute(update_upBy_query, (updatedBy, txtID))
            cursor.execute(update_upAt_query, (txtID,))
        except Exception as error:
            print(f"Erro ao atualizar o pix de ID {txtID}, Erro: {error}")
        else:
            print(f'Pix de ID: {txtID} atualizado com sucesso!')
            self.conn.commit()
        finally:
            cursor.close()


    def updatePixNumInterno(self, txtID, numInterno):
        cursor = self.conn.cursor()
        update_status_query = """UPDATE pix SET num_interno = %s WHERE txtid = %s"""
        try:
            cursor.execute(update_status_query, (numInterno, txtID))
        except Exception as error:
            print(f"Erro ao atualizar o pix de ID {txtID}, Erro: {error}")
        else:
            print(f'Pix de ID: {txtID} atualizado com sucesso!')
            self.conn.commit()
        finally:
            cursor.close()

    def deletePix(self, txtID) -> str:
        cursor = self.conn.cursor()
        delete_query = """DELETE FROM pix WHERE txtid = %s"""
        if self.searchPixByID(txtID) == None:
            return(f'O Pix de ID: {txtID} não foi encontrado, nada para deletar.')
        try:
            cursor.execute(delete_query,(txtID,))
        except Exception as error:
            print(f'Erro ao deletar pix: {error}')
        else:
            return(f"Pix de ID: {txtID} excluído com sucesso")
        finally:
            self.conn.commit()
            cursor.close()


    def closeDB(self):
        try:
            self.conn.close()
        except Exception as error:
            print(f'Erro ao fechar o banco PostgreSQL (Pix): {error}')

if __name__ == "__main__":
    hostname = 'localhost'
    database = 'syspagpix'
    username = 'postgres'
    pwd = '3m193mRJA@'
    port_id = '5432'
    
    #  Informações para teste de gravação no banco
    txtID = '23dF34FR'
    nomeApresentante = 'Eduardo Rossini Xavier'
    valor = 24512.41
    createdBy = 'edu'
    status = 'aguardando'
    novoStatus = 'pago'
    updatedBy = 'edu'

    conn = None
    cur = None

    db = DataBasePix(hostname, database, username, pwd, port_id)

    # Teste das funções de dados, primeiramente tentar apagar um pix que ainda não existe
    print('Tentativa de deletar pix, porém o pix ainda não existe.')
    print(db.deletePix(txtID))
    print('\n')


    # Criar um pix de teste repassando menos valores para a função
    print('Criando pix de teste com valor faltando')
    try:
        db.insertPix(nomeApresentante, valor, createdBy, status)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')

    # Criar um pix de teste repassando menos valores para a função
    print('Criando pix de teste com valores corretos')
    try:
        db.insertPix(txtID, nomeApresentante, valor, createdBy, status)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')


    # Verficar o pix inserido anteriormente
    print("Verificando pix inserido")
    pixInserido = db.searchPixByID(txtID)
    if pixInserido != None:
        print('Pix inserido com sucesso, valores:')
        for i, valor in enumerate(pixInserido):
            print(f'Indice: {i} e valor: {valor}')
    else:
        print(f'O Pix de id {txtID} não pode ser inserido')
    print('\n')

    # Verficar o status do pix inserido anteriormente
    print("Atualizando pix inserido")
    try:
        db.updatePix(txtID=txtID, updatedBy=updatedBy, status=novoStatus)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')

    # Verficar o status do pix inserido anteriormente
    print("Atualizando número interno do pix inserido")
    try:
        db.updatePixNumInterno(txtID=txtID, numInterno='22/22025672')
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')

    # Verifica o status do pix após atualizado
    print("Verificando pix atualizado")
    pixAtualizado = db.searchPixByID(txtID)
    if pixAtualizado != None:
        print('Pix inserido com sucesso, valores:')
        for i, valor in enumerate(pixAtualizado):
            print(f'Indice: {i} e valor: {valor}')
    else:
        print(f'O Pix de id {txtID} não pode ser inserido')
    print('\n')

    # Testar query de nome
    nomes = db.searchPixByName('Eduardo', 10, 'aguardando', 'Data', '30/11/2022')
    for nome in nomes:
        print(nome)

    # Deletar o pix criado após rodada de testes finalizada.
    print('Deletando pix criado após o teste com sucesso.')
    print(db.deletePix(txtID))
    print('\n')

    db.closeDB()