import psycopg2
import sqlite3
import bcrypt
import uuid

def genTxtID():
    struuid = uuid.uuid4()
    txtid = str(struuid).replace('-',"")
    return txtid

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

    # Consertar
    def insertSolicitante(self, cpf_cnpj, nomeApresentante):
        cursor = self.conn.cursor()
        tabela = "solicitante"
        resultado = ''
        search_query = f"""SELECT * FROM {tabela} WHERE cpf_cnpj = '{cpf_cnpj}'"""
        insert_query = f"""INSERT INTO {tabela} (cpf_cnpj, nome) 
                        VALUES('{cpf_cnpj}','{nomeApresentante}')"""

        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f'Erro ao buscar o solictante: {error}')
            self.conn.rollback()
            cursor.close()
            resultado = 'Erro ao buscar solicitante'
            return resultado
        else:
            soliticanteExistente = cursor.fetchone()

        if soliticanteExistente == None:
            try:
                cursor.execute(insert_query)
            except Exception as error:
                print(f'Erro ao inserir o solicitante: {error}')
                self.conn.rollback()
                resultado = 'Erro na inserção do solicitante'
            else:
                print(f'Solicitante de CPF_CNPJ: {cpf_cnpj} inserido com sucesso!')
                self.conn.commit()
                resultado = 'inserido'
            finally:
                cursor.close()
                return resultado
        else:
            print(f'Solicitante de CPF_CNPJ: {cpf_cnpj} já existe na base de dados!')
            resultado = "existente"
            cursor.close()
            return resultado

    def buscaSolicitante(self, cpf_cnpj):
        cursor = self.conn.cursor()
        tabela = "solicitante"
        resultado = ''
        search_query = f"""SELECT * FROM {tabela} WHERE cpf_cnpj = '{cpf_cnpj}'"""

        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f'Erro ao buscar o solictante: {error}')
            self.conn.rollback()
            cursor.close()
            resultado = 'erro'
            return resultado
        else:
            resultado = cursor.fetchone()
            return resultado
            
    def insertPix(self, txtID, valor, createdBy, status, cpf_cnpj):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela = "pagamento"
        insert_query = f"""INSERT INTO {tabela} (txtid, valor, createdby, status, createdat, cpf_cnpj) 
                        VALUES('{txtID}','{valor}','{createdBy}','{status}',now(),'{cpf_cnpj}')"""
        try:
            cursor.execute(insert_query)
        except Exception as error:
            print(f'Erro ao inserir o pix: {error} (db.InsertPix, linha 179)')
            self.conn.rollback()
        else:
            print(f'Pix de ID: {txtID} inserido com sucesso!')
            self.conn.commit()
        finally:
            cursor.close()


    def searchPixByName(self, apresentante, limite, filtro, filtroData, data):
        nomesEncontrados = []
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        dia, mes, ano = data.split('/')
        inicioDia = f"{ano}-{mes}-{dia} 00:00:00"
        fimDia = f"{ano}-{mes}-{dia} 23:59:59"
        tabela1 = "pagamento"
        tabela2 = "solicitante"
        tabela3 = "protocolo"
        tabela4 = "certidao"
        
        # Query full outer join
        # SELECT
        #     p.idpix,
        #     nome,
        #     valor,
        #     createdat,
        #     status,
        #     C.ano,
        #     C.num,
        #     PR.num
        # FROM
        #     pagamento AS P
        #     FULL outer JOIN certidao AS C ON C.idpix = P.idpix
        #     FULL outer JOIN protocolo AS PR ON PR.idpix = P.idpix
        #     INNER JOIN solicitante as S on S.cpf_cnpj = P.cpf_cnpj
        # WHERE
        # 	createdby = 'adm'
        # ORDER BY
        #     createdat DESC
        # LIMIT
        #     10;

        # Search query com nome do apresentante, filtro de status e/ou data
        # Search query com regex iniciando com case insensitive (*) e 
        # aceitando palavras, espaços etc. tanto antes quanto após o nome pesquisado.
        if apresentante != '' and filtro != '' and filtroData != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante != '' and filtro == '' and filtroData != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtroData != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        AND status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro == '' and filtroData != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtro de data desligado:                
        elif apresentante != '' and filtro != '' and filtroData == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND status = '{filtro}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante != '' and filtro == '' and filtroData == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtroData == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        AND status = '{filtro}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtros de data e status desligados (na posição "todos")
        else:
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        ORDER BY createdat DESC LIMIT {limite}"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao recuperar registros de pagamento pix, Erro: {error}")
            self.conn.rollback()
        else:
            nomesEncontrados = cursor.fetchall()
            self.conn.commit()
        finally:
            cursor.close()
            return nomesEncontrados

    # data = data completa ex.: 23/05/2023
    def searchPixAguardando(self, data):
        pix_aguardando = []
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'

        dia, mes, ano = data.split('/')
        inicioDia = f"{ano}-{mes}-{dia} 00:00:00"
        fimDia = f"{ano}-{mes}-{dia} 23:59:59"
        tabela1 = "pagamento"
        tabela2 = "solicitante"
        tabela3 = "protocolo"
        tabela4 = "certidao"
        filtro = 'aguardando'
        limite = 50

        search_query = f"""SELECT SELECT P.idpix, nome, valor, createdby, 
                        createdat, status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        AND status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao buscar pagamentos pix com estatus aguardando")
            self.conn.rollback()
        else:
            pix_aguardando = cursor.fetchall()
            self.conn.commit()
        finally:
            cursor.close()
        return(len(pix_aguardando))

    # caixa = sigla (edu, ana, fra), limite = 10, 50, filtro = 'pago', 'aguardando'
    # apresentante = parte de nome do solicitante ex.: eduardo, marcelo costa etc.
    # filtrodata = sim ou '', data = data completa ex.: 23/05/2023
    def searchPixByCaixa(self, caixa, limite, filtro, apresentante, filtroData, data) -> list:
        pgtosEncontrados = []
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'

        tabela1 = "pagamento"
        tabela2 = "solicitante"
        tabela3 = "protocolo"
        tabela4 = "certidao"

        dia, mes, ano = data.split('/')
        inicioDia = f"{ano}-{mes}-{dia} 00:00:00"
        fimDia = f"{ano}-{mes}-{dia} 23:59:59"

        # Search query com nome do caixa para exibir os pagamentos gerados pelo mesmo.
        # Search query com regex iniciando com case insensitive (*) e 
        # aceitando palavras, espaços etc. tanto antes quanto após o nome pesquisado.
        if apresentante != '' and filtro != '' and filtroData != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND createdby = '{caixa}' 
                        AND status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante != '' and filtro == '' and filtroData != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND createdby = '{caixa}' 
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtroData != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE createdby = '{caixa}' 
                        AND status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro == '' and filtroData != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE createdby = '{caixa}' 
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtro de data desligado:                
        elif apresentante != '' and filtro != '' and filtroData == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND createdby = '{caixa}' 
                        AND status = '{filtro}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante != '' and filtro == '' and filtroData == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND createdby = '{caixa}' 
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtroData == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE createdby = '{caixa}' 
                        AND status = '{filtro}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtros de data e status desligados (na posição "todos")
        else:
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE createdby = '{caixa}' 
                        ORDER BY createdat DESC LIMIT {limite}"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar os pagamentos pix do caixa {caixa}, Erro: {error}")
            self.conn.rollback()
        else:
            pgtosEncontrados = cursor.fetchall()
            self.conn.commit()
        finally:
            cursor.close()
            return pgtosEncontrados


    def searchPixByCpf_CnpjCaixa(self, cpf_cpnj, caixa) -> tuple:
        pixEncontrado: tuple
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "pagamento"
        tabela2 = "solicitante"
        tabela3 = "protocolo"
        tabela4 = "certidao"

        search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                    status, C.ano, C.num, PR.num
                    FROM {tabela1} AS P
                    FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                    FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                    INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj 
                    WHERE cpf_cnpj = '{cpf_cpnj}'
                    AND createdby = '{caixa}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar pagamentos pix do CPF_CNPJ: {cpf_cpnj}, Erro: {error}")
            self.conn.rollback()
        else:
            pixEncontrado = cursor.fetchall()
            self.conn.commit()
        finally:
            cursor.close()
            return pixEncontrado


    def getNome(self, cpf_cnpj) -> tuple:
        solicitanteEncontrado: tuple
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela = "solicitante"
        search_query = f"""SELECT * FROM {tabela} WHERE cpf_cnpj = '{cpf_cnpj}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o solicitante de CPF: {cpf_cnpj}, Erro: {error}")
            self.conn.rollback()
        else:
            solicitanteEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            if len(solicitanteEncontrado[0]) > 14:
                cpf = ''
                cnpj = solicitanteEncontrado[0]
            else:
                cnpj = ''
                cpf = solicitanteEncontrado[0]
            nome = solicitanteEncontrado[1]
            return cpf, cnpj, nome



    def searchPixByIDCaixa(self, pixID, caixa) -> tuple:
        pixEncontrado: tuple
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "pagamento"
        tabela2 = "solicitante"
        tabela3 = "protocolo"
        tabela4 = "certidao"

        search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE P.idpix = '{pixID}'
                        AND createdby = '{caixa}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {pixID}, Erro: {error}")
            self.conn.rollback()
        else:
            pixEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            return pixEncontrado


    def searchPixByID(self, pixID) -> tuple:
        pixEncontrado = ''
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "pagamento"
        tabela2 = "solicitante"
        tabela3 = "protocolo"
        tabela4 = "certidao"

        search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE P.idpix = '{pixID}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {pixID}, Erro: {error}")
            self.conn.rollback()
        else:
            pixEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            return pixEncontrado


    def getPixID(self, TxtID):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "pagamento"

        search_query = f"""SELECT idpix FROM {tabela1} WHERE txtid = '{TxtID}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {TxtID}, Erro: {error}")
            self.conn.rollback()
        else:
            pixEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            if pixEncontrado != None:
                return int(pixEncontrado[0])
            else:
                return 'Pix inexistente'
            

    def getCopiaCola(self, TxtID):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "pagamento"

        search_query = f"""SELECT pixcopiacola
                        FROM {tabela1}
                        WHERE txtid = '{TxtID}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {TxtID}, Erro: {error}")
            self.conn.rollback()
        else:
            pixEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            if pixEncontrado != None:
                return pixEncontrado[0]
            else:
                return 'erro'


    def updatePix(self, pixId, updatedBy, status):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela = "pagamento"
        update_status_query = f"""UPDATE {tabela} SET status = '{status}' WHERE idpix = '{pixId}'"""
        update_upBy_query = f"""UPDATE {tabela} SET updatedby = '{updatedBy}' WHERE idpix = '{pixId}'"""
        update_upAt_query = f"""UPDATE {tabela} SET updatedat = now() WHERE idpix = '{pixId}'"""
        try:
            cursor.execute(update_status_query, (status, pixId))
            cursor.execute(update_upBy_query, (updatedBy, pixId))
            cursor.execute(update_upAt_query, (pixId,))
        except Exception as error:
            print(f"Erro ao atualizar o pix de ID {pixId}, Erro: {error}")
            self.conn.rollback()
        else:
            print(f'Pix de ID: {pixId} atualizado com sucesso!')
            self.conn.commit()
        finally:
            cursor.close()

    #### CONSERTAR ####
    def insertPixNumInterno(self, pixid, anocert, numcert, numprot):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "certidao"
        tabela2 = "protocolo"
        if anocert != 0 and numcert != 0 and numprot != 0:
            insert_cert_query = f"""INSERT INTO {tabela1} (idpix, ano, num) 
                                    VALUES({pixid}, {anocert}, {numcert})"""
            insert_prot_query = f"""INSERT INTO {tabela2} (idpix, num) 
                                    VALUES({pixid}, {numprot})"""
            try:
                cursor.execute(insert_cert_query)
                cursor.execute(insert_prot_query)
            except Exception as error:
                print(f"Erro ao inserir prototolo e certidão para o pix de ID {pixid}, Erro: {error}")
                self.conn.rollback()
            else:
                print(f'Pix de ID: {pixid} atualizado com sucesso!')
                self.conn.commit()
                return 'sucesso'
            finally:
                cursor.close()
        elif anocert == 0 and numcert == 0 and numprot != 0:
            insert_prot_query = f"""INSERT INTO {tabela2} (idpix, num) 
                                    VALUES({pixid}, {numprot})"""
            try:
                cursor.execute(insert_prot_query)
            except Exception as error:
                print(f"Erro ao inserir prototolo para o pix de ID {pixid}, Erro: {error}")
                self.conn.rollback()
            else:
                print(f'Pix de ID: {pixid} atualizado com sucesso!')
                self.conn.commit()
                return 'sucesso'
            finally:
                cursor.close()
        elif anocert != 0 and numcert != 0 and numprot == 0:
            insert_cert_query = f"""INSERT INTO {tabela1} (idpix, ano, num) 
                                    VALUES({pixid}, {anocert}, {numcert})"""
            try:
                cursor.execute(insert_cert_query)
            except Exception as error:
                print(f"Erro ao inserir prototolo para o pix de ID {pixid}, Erro: {error}")
                self.conn.rollback()
            else:
                print(f'Pix de ID: {pixid} atualizado com sucesso!')
                self.conn.commit()
                return 'sucesso'
            finally:
                cursor.close()
        else:
            print('Erro! Verificar os dados antes de inserir')
            return 'erro'

            
    def deletePix(self, txtID) -> str:
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela = "pagamento"
        delete_query = f"""DELETE FROM {tabela} WHERE txtid = '{txtID}'"""
        pixID = self.getPixID(TxtID=txtID)
        buscaPix = self.searchPixByID(pixID)
        if buscaPix == None or buscaPix == '':
            return(f'O Pix de ID: {pixID} não foi encontrado, nada para deletar.')
        try:
            cursor.execute(delete_query)
        except Exception as error:
            print(f'Erro ao deletar pix: {error}')
            self.conn.rollback()
        else:
            print(f"Pix de ID: {pixID} excluído com sucesso")
        finally:
            self.conn.commit()
            cursor.close()
        return


    def closeDB(self):
        try:
            self.conn.close()
        except Exception as error:
            print(f'Erro ao fechar o banco PostgreSQL (SysPagDB): {error}')

if __name__ == "__main__":
    hostname = 'localhost'
    database = 'syspagpix'
    username = 'postgres'
    pwd = '3m193mRJA@'
    port_id = '5432'
    
    #  Informações para teste de gravação no banco
    txtID = genTxtID()
    cpf = "009.922.677-49"
    nome = "Jardel Frederico de Boscoli"
    valor = 76012.41
    createdBy = 'edu'
    status = 'aguardando'
    novoStatus = 'pago'
    updatedBy = 'edu'

    conn = None
    cur = None

    db = DataBasePix(hostname, database, username, pwd, port_id)

    # Teste de cadastro do solicitante
    print('Criando solicitante de Teste')
    try: 
        db.insertSolicitante(cpf, nome)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')

    pixID = db.getPixID(txtID)
    # Teste das funções de dados, primeiramente tentar apagar um pix caso exista
    print('Tentativa de deletar pix, caso o pix exista.')
    print(db.deletePix(txtID))
    print('\n')


    # Criar um pix de teste repassando menos valores para a função
    print('Criando pix de teste com valor faltando')
    try:
        db.insertPix(txtID, valor, createdBy, status)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')


    # Criar um pix de teste repassando valores corretos para a função
    print('Criando pix de teste com valores corretos')
    try:
        db.insertPix(txtID, valor, createdBy, status, cpf)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')


    # Verficar o pix inserido anteriormente
    pixID = db.getPixID(txtID)
    print("Verificando pix inserido")
    pixInserido = db.searchPixByID(pixID)
    if pixInserido != None:
        print('Pix inserido com sucesso, valores:')
        for i, valor in enumerate(pixInserido):
            print(f'Indice: {i} e valor: {valor}')
    else:
        print(f'O Pix de id {pixID} não pode ser verificado')
    print('\n')


    # Verficar o status do pix inserido anteriormente
    print("Atualizando pix inserido")
    try:
        db.updatePix(pixId=pixID, updatedBy=updatedBy, status=novoStatus)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')

    # # Verficar o status do pix inserido anteriormente
    # print("Atualizando número interno do pix inserido")
    # try:
    #     db.updatePixNumInterno(txtID=txtID, numInterno='22/22025672')
    # except Exception as error:
    #     print(f'Erro ao inserir: {error}')
    # print('\n')

    # Verifica o status do pix após atualizado
    print("Verificando pix atualizado")
    pixAtualizado = db.searchPixByID(pixID=pixID)
    if pixAtualizado != None:
        print('Pix localizado com sucesso, seguem os valores:')
        for i, valor in enumerate(pixAtualizado):
            print(f'Indice: {i} e valor: {valor}')
    else:
        print(f'O Pix de id {pixID} não pode ser localizado')
    print('\n')

    # # Testa query de busca por caixa
    # print("Verificando busca por caixa")
    # caixaPix = db.searchPixByCaixa(caixa='edu', limite=10, filtro="pago", apresentante='ross', filtroData='', data='19/05/2023')
    # for pix in caixaPix:
    #     print(pix)

    print("Verificando busca por nome")
    nomePix = db.searchPixByName(apresentante='ed', limite=10, filtro='', filtroData='', data='01/01/2023')
    for nome in nomePix:
        print(nome)

    print('\n')
    print('Teste de localizar PixID pelo TxtID')
    pixID = db.getPixID(txtID)
    print(f'Pix ID encontrado: {pixID}')
    # # Testar query de nome
    # nomes = db.searchPixByName('Eduardo', 10, 'aguardando', 'Data', '30/11/2022')
    # for nome in nomes:
    #     print(nome)

    # # Deletar o pix criado após rodada de testes finalizada.
    # print('Deletando pix criado após o teste com sucesso.')
    # print(db.deletePix(txtID))
    # print('\n')

    db.closeDB()
