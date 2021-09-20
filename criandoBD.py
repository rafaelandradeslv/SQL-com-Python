import sqlite3

conn = sqlite3.connect("agenda.db")
cursor = conn.cursor()


# --- CRIANDO TABELA ---
def createTable():
    cursor.execute("""create table agenda(
                      nome text,
                      telefone text)
                    """)
# createTable()


# --- INSERINDO DADOS ---
def insereDados():
    cursor.execute(
        """insert into agenda (nome, telefone)
            values(?, ?)""",  ("Andrew", "5692-5643"))
# insereDados()


# --- CONSULTANDO DADOS ---
def consultaUmDado():
    cursor.execute("select * from agenda")
    result = cursor.fetchone()
    print(f"Nome: {result[0]}, Telefone: {result[1]}", )
# consultaUmDado()


# --- Inserindo Múltiplos Dados ---
def insertMultData():
    dados = [("João", "98901-0109"),
             ("André", "98902-8900"),
             ("Maria", "97891-3321")
             ]
    cursor.executemany(
        '''insert into agenda(nome, telefone) values(?, ?)''', dados)
# insertMultData()


# --- CONSULTANDO MÚLTIPLOS VALORES ---
def consultMultDados():
    cursor.execute('select * from agenda')
    result = cursor.fetchall()

    for resultado in result:
        dados = (f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
        print(dados)
# consultMultDados()


# --- CONSULTANDO REGISTRO POR REGISTRO ---
def registroRegistro():
    cursor.execute('select * from agenda')
    while True:
        resultado = cursor.fetchone()
        if resultado == None:
            break
        print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
# registroRegistro()



# --- FINALIZANDO CONEXÃO ---
conn.commit()
cursor.close()
conn.close()
