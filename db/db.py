import psycopg2
import sqlite3
import bcrypt
import uuid

def gen_txt_id():
    struuid = uuid.uuid4()
    txtid = str(struuid).replace('-',"")
    return txtid

class DataBaseUsers():
    def __init__(self, dbname):
        self.dbname = dbname
        self.connect_users()
    
    def connect_users(self):
        try:
            self.db = sqlite3.connect(self.dbname)
        except Exception as error:
            print(f"Erro ao conectar: {error}")
        self.cursor = self.db.cursor()

    def close_users(self):
        try:
            self.db.close()
        except Exception as error:
            print(f'Erro ao fechar o banco SQLite3 (users): {error}')

    def insert_users(self, user, password, access, user_name) -> str:
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
                            VALUES(?,?,?,?)''', (sigla, hashPwd, hashAcesso, user_name))
            self.cursor.close()
            self.db.commit()
            return 'sucesso'


    def check_users(self, user, password):
        found = None
        acesso_usuario = ''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute('''SELECT * FROM users WHERE user=?''', (user,))
        except Exception as error:
            print(f'Erro: {error}')
            return 'credenciais', 'incorretas'
        else:
            found = self.cursor.fetchone()
            if found != None:
                stored_psswd = found[1]
                stored_acesso = found[2]
                user_name = found[3]
                lista_acessos = ['administrador', 'caixa', 'contabilidade']
            
                typed_psswd = password.encode('utf-8')

                try:
                    psswd_ok = bcrypt.checkpw(typed_psswd, stored_psswd)
                except:
                    return 'credenciais', 'incorretas'

                for acesso in lista_acessos:
                    chk_acesso = acesso.encode('utf-8')
                    if bcrypt.checkpw(chk_acesso, stored_acesso):
                        acesso_usuario = acesso
                        break

                if psswd_ok and acesso_usuario != '':
                    self.cursor.close()
                    return user_name, acesso_usuario
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
        self.user_name = user
        self.pwd = password
        self.port_id = port
        self.connect_db()

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
                    host = self.host,
                    dbname = self.dbname,
                    user = self.user_name,
                    password = self.pwd,
                    port = self.port_id)

        except Exception as error:
            print(error)

    # Consertar
    def insert_solicitante(self, cpf_cnpj, nome_apresentante):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela = "solicitante"
        resultado = ''
        search_query = f"""SELECT * FROM {tabela} WHERE cpf_cnpj = '{cpf_cnpj}'"""
        insert_query = f"""INSERT INTO {tabela} (cpf_cnpj, nome) 
                        VALUES('{cpf_cnpj}','{nome_apresentante}')"""

        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f'Erro ao buscar o solictante: {error}')
            self.conn.rollback()
            cursor.close()
            resultado = 'Erro ao buscar solicitante'
            return resultado
        else:
            solicitante_existente = cursor.fetchone()

        if solicitante_existente == None:
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

    def busca_solicitante(self, cpf_cnpj):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
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
            
    def insert_pix(self, txt_id, valor, created_by, status, cpf_cnpj):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela = "pagamento"
        insert_query = f"""INSERT INTO {tabela} (txtid, valor, createdby, status, createdat, cpf_cnpj) 
                        VALUES('{txt_id}','{valor}','{created_by}','{status}',now(),'{cpf_cnpj}')"""
        try:
            cursor.execute(insert_query)
        except Exception as error:
            print(f'Erro ao inserir o pix: {error} (db.InsertPix, linha 179)')
            self.conn.rollback()
        else:
            print(f'Pix de ID: {txt_id} inserido com sucesso!')
            self.conn.commit()
        finally:
            cursor.close()


    def search_pix_by_name(self, apresentante, limite, filtro, filtro_data, data):
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
        
        if apresentante != '' and filtro != '' and filtro_data != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num, horapagamento
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante != '' and filtro == '' and filtro_data != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num, horapagamento
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtro_data != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num, horapagamento
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        AND status = '{filtro}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro == '' and filtro_data != '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num, horapagamento
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        # Filtro de data desligado:                
        elif apresentante != '' and filtro != '' and filtro_data == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num, horapagamento
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND status = '{filtro}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante != '' and filtro == '' and filtro_data == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num, horapagamento
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtro_data == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdby, createdat,
                        status, updatedby, C.ano, C.num, PR.num, horapagamento
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
    def search_pix_status(self, sigla, data, filtro):
        pix_aguardando = []
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 0

        dia, mes, ano = data.split('/')
        inicioDia = f"{ano}-{mes}-{dia} 00:00:00"
        fimDia = f"{ano}-{mes}-{dia} 23:59:59"
        tabela1 = "pagamento"
        tabela2 = "solicitante"
        tabela3 = "protocolo"
        tabela4 = "certidao"
        limite = 50

        search_query = f"""SELECT P.idpix, nome, valor, createdby, 
                        createdat, status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        AND status = '{filtro}'
                        AND createdby = '{sigla}'
                        AND createdat >= '{inicioDia}'
                        AND createdat <= '{fimDia}'
                        ORDER BY createdat DESC LIMIT {limite}"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao buscar pagamentos pix com status: {filtro}")
            print(error)
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
    def search_pix_by_caixa(self, caixa, limite, filtro, apresentante, filtro_data, data) -> list:
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
        if apresentante != '' and filtro != '' and filtro_data != '':
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
        elif apresentante != '' and filtro == '' and filtro_data != '':
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
        elif apresentante == '' and filtro != '' and filtro_data != '':
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
        elif apresentante == '' and filtro == '' and filtro_data != '':
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
        elif apresentante != '' and filtro != '' and filtro_data == '':
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
        elif apresentante != '' and filtro == '' and filtro_data == '':
            search_query = f"""SELECT P.idpix, nome, valor, createdat, createdby,
                        status, C.ano, C.num, PR.num
                        FROM {tabela1} AS P
                        FULL outer JOIN {tabela4} AS C ON C.idpix = P.idpix
                        FULL outer JOIN {tabela3} AS PR ON PR.idpix = P.idpix
                        INNER JOIN {tabela2} AS S ON S.cpf_cnpj = P.cpf_cnpj
                        WHERE S.nome ~* '^.*{apresentante}.*$'
                        AND createdby = '{caixa}' 
                        ORDER BY createdat DESC LIMIT {limite}"""
        elif apresentante == '' and filtro != '' and filtro_data == '':
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



    def search_pix_by_id_caixa(self, pix_id, caixa) -> tuple:
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
                        WHERE P.idpix = '{pix_id}'
                        AND createdby = '{caixa}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {pix_id}, Erro: {error}")
            self.conn.rollback()
        else:
            pixEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            return pixEncontrado


    def search_pix_by_id(self, pix_id) -> tuple:
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
                        WHERE P.idpix = '{pix_id}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {pix_id}, Erro: {error}")
            self.conn.rollback()
        else:
            pixEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            return pixEncontrado


    def get_pix_id(self, txt_id):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "pagamento"

        search_query = f"""SELECT idpix FROM {tabela1} WHERE txtid = '{txt_id}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {txt_id}, Erro: {error}")
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


    def get_txt_id(self, pix_id):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "pagamento"

        search_query = f"""SELECT txtid FROM {tabela1} WHERE idpix = '{pix_id}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {pix_id}, Erro: {error}")
            self.conn.rollback()
        else:
            pixEncontrado = cursor.fetchone()
            self.conn.commit()
        finally:
            cursor.close()
            if pixEncontrado != None:
                return pixEncontrado[0]
            else:
                return 'Pix inexistente'


    def get_copia_cola(self, txt_id):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "pagamento"

        search_query = f"""SELECT pixcopiacola
                        FROM {tabela1}
                        WHERE txtid = '{txt_id}'"""
        try:
            cursor.execute(search_query)
        except Exception as error:
            print(f"Erro ao localizar o pix de ID {txt_id}, Erro: {error}")
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


    def update_pix(self, pix_id, updated_by, status):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela = "pagamento"
        update_status_query = f"""UPDATE {tabela} SET status = '{status}' WHERE idpix = '{pix_id}'"""
        update_upBy_query = f"""UPDATE {tabela} SET updatedby = '{updated_by}' WHERE idpix = '{pix_id}'"""
        update_upAt_query = f"""UPDATE {tabela} SET updatedat = now() WHERE idpix = '{pix_id}'"""
        try:
            cursor.execute(update_status_query, (status, pix_id))
            cursor.execute(update_upBy_query, (updated_by, pix_id))
            cursor.execute(update_upAt_query, (pix_id,))
        except Exception as error:
            print(f"Erro ao atualizar o pix de ID {pix_id}, Erro: {error}")
            self.conn.rollback()
        else:
            print(f'Pix de ID: {pix_id} atualizado com sucesso!')
            self.conn.commit()
        finally:
            cursor.close()

    #### CONSERTAR ####
    def insert_pix_num_interno(self, pix_id, anocert, numcert, numprot):
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela1 = "certidao"
        tabela2 = "protocolo"
        if anocert != 0 and numcert != '' and numprot != '':
            insert_cert_query = f"""INSERT INTO {tabela1} (idpix, ano, num) 
                                    VALUES({pix_id}, {anocert}, '{numcert}')"""
            insert_prot_query = f"""INSERT INTO {tabela2} (idpix, num) 
                                    VALUES({pix_id}, '{numprot}')"""
            try:
                cursor.execute(insert_cert_query)
                cursor.execute(insert_prot_query)
            except Exception as error:
                print(f"Erro ao inserir prototolo e certidão para o pix de ID {pix_id}, Erro: {error}")
                self.conn.rollback()
            else:
                print(f'Pix de ID: {pix_id} atualizado com sucesso!')
                self.conn.commit()
                return 'sucesso'
            finally:
                cursor.close()
        elif anocert == 0 and numcert == '' and numprot != '':
            insert_prot_query = f"""INSERT INTO {tabela2} (idpix, num) 
                                    VALUES({pix_id}, '{numprot}')"""
            try:
                cursor.execute(insert_prot_query)
            except Exception as error:
                print(f"Erro ao inserir prototolo para o pix de ID {pix_id}, Erro: {error}")
                self.conn.rollback()
            else:
                print(f'Pix de ID: {pix_id} atualizado com sucesso!')
                self.conn.commit()
                return 'sucesso'
            finally:
                cursor.close()
        elif anocert != 0 and numcert != '' and numprot == '':
            insert_cert_query = f"""INSERT INTO {tabela1} (idpix, ano, num) 
                                    VALUES({pix_id}, {anocert}, '{numcert}')"""
            try:
                cursor.execute(insert_cert_query)
            except Exception as error:
                print(f"Erro ao inserir prototolo para o pix de ID {pix_id}, Erro: {error}")
                self.conn.rollback()
            else:
                print(f'Pix de ID: {pix_id} atualizado com sucesso!')
                self.conn.commit()
                return 'sucesso'
            finally:
                cursor.close()
        else:
            print('Erro! Verificar os dados antes de inserir')
            return 'erro'

            
    def deletePix(self, txt_id) -> str:
        try:
            cursor = self.conn.cursor()
        except Exception as error:
            print(error)
            return 'conexão encerrada'
        tabela = "pagamento"
        delete_query = f"""DELETE FROM {tabela} WHERE txtid = '{txt_id}'"""
        pix_id = self.get_pix_id(txt_id)
        buscaPix = self.search_pix_by_id(pix_id)
        if buscaPix == None or buscaPix == '':
            return(f'O Pix de ID: {pix_id} não foi encontrado, nada para deletar.')
        try:
            cursor.execute(delete_query)
        except Exception as error:
            print(f'Erro ao deletar pix: {error}')
            self.conn.rollback()
        else:
            print(f"Pix de ID: {pix_id} excluído com sucesso")
        finally:
            self.conn.commit()
            cursor.close()
        return


    def close_db(self):
        try:
            self.conn.close()
        except Exception as error:
            print(f'Erro ao fechar o banco PostgreSQL (SysPagDB): {error}')

if __name__ == "__main__":
    hostname = 'localhost'
    database = 'syspagpix'
    user_name = 'postgres'
    pwd = '123456'
    port_id = '5432'
    
    #  Informações para teste de gravação no banco
    txt_id = gen_txt_id()
    cpf = "009.922.677-49"
    nome = "Jardel Frederico de Boscoli"
    valor = 76012.41
    created_by = 'edu'
    status = 'aguardando'
    novoStatus = 'pago'
    updated_by = 'edu'

    conn = None
    cur = None

    db = DataBasePix(hostname, database, user_name, pwd, port_id)

    # Teste de cadastro do solicitante
    print('Criando solicitante de Teste')
    try: 
        db.insert_solicitante(cpf, nome)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')

    pix_id = db.get_pix_id(txt_id)
    # Teste das funções de dados, primeiramente tentar apagar um pix caso exista
    print('Tentativa de deletar pix, caso o pix exista.')
    print(db.deletePix(txt_id))
    print('\n')


    # Criar um pix de teste repassando menos valores para a função
    print('Criando pix de teste com valor faltando')
    try:
        db.insert_pix(txt_id, valor, created_by, status)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')


    # Criar um pix de teste repassando valores corretos para a função
    print('Criando pix de teste com valores corretos')
    try:
        db.insert_pix(txt_id, valor, created_by, status, cpf)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')


    # Verficar o pix inserido anteriormente
    pix_id = db.get_pix_id(txt_id)
    print("Verificando pix inserido")
    pixInserido = db.search_pix_by_id(pix_id)
    if pixInserido != None:
        print('Pix inserido com sucesso, valores:')
        for i, valor in enumerate(pixInserido):
            print(f'Indice: {i} e valor: {valor}')
    else:
        print(f'O Pix de id {pix_id} não pode ser verificado')
    print('\n')


    # Verficar o status do pix inserido anteriormente
    print("Atualizando pix inserido")
    try:
        db.update_pix(pix_id=pix_id, updated_by=updated_by, status=novoStatus)
    except Exception as error:
        print(f'Erro ao inserir: {error}')
    print('\n')

    # # Verficar o status do pix inserido anteriormente
    # print("Atualizando número interno do pix inserido")
    # try:
    #     db.updatePixNumInterno(txt_id=txt_id, numInterno='22/22025672')
    # except Exception as error:
    #     print(f'Erro ao inserir: {error}')
    # print('\n')

    # Verifica o status do pix após atualizado
    print("Verificando pix atualizado")
    pixAtualizado = db.search_pix_by_id(pix_id=pix_id)
    if pixAtualizado != None:
        print('Pix localizado com sucesso, seguem os valores:')
        for i, valor in enumerate(pixAtualizado):
            print(f'Indice: {i} e valor: {valor}')
    else:
        print(f'O Pix de id {pix_id} não pode ser localizado')
    print('\n')

    # # Testa query de busca por caixa
    # print("Verificando busca por caixa")
    # caixaPix = db.search_pix_by_caixa(caixa='edu', limite=10, filtro="pago", apresentante='ross', filtro_data='', data='19/05/2023')
    # for pix in caixaPix:
    #     print(pix)

    print("Verificando busca por nome")
    nomePix = db.search_pix_by_name(apresentante='ed', limite=10, filtro='', filtro_data='', data='01/01/2023')
    for nome in nomePix:
        print(nome)

    print('\n')
    print('Teste de localizar PixID pelo txt_id')
    pix_id = db.get_pix_id(txt_id)
    print(f'Pix ID encontrado: {pix_id}')
    # # Testar query de nome
    # nomes = db.search_pix_by_name('Eduardo', 10, 'aguardando', 'Data', '30/11/2022')
    # for nome in nomes:
    #     print(nome)

    # # Deletar o pix criado após rodada de testes finalizada.
    # print('Deletando pix criado após o teste com sucesso.')
    # print(db.deletePix(txt_id))
    # print('\n')

    db.close_db()
