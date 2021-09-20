import sqlite3
from contextlib import closing

# Exercício 1.1 Faça um programa que crie o banco de dados preços.db com a
# tabela preços para armazenar uma lista de preços de venda de produtos. A tabela
# deve conter o nome do produto e seu respectivo preço. O programa também deve
# inserir alguns dados para teste

conn = sqlite3.connect("precos.db")
cursor = conn.cursor()


def criandoBancoDados(nomeBD):
    conn = sqlite3.connect(f'{nomeBD}')
    return conn
# criandoBancoDados('precos.db')


def criandoTabela():
    cursor.execute("create table precos(nome_do_produto text, preco text)")
# criandoTabela()


def insertDados():
    cursor.execute(
        'insert into precos(nome_do_produto, preco) values(?,?)', ('Feijão', '6.99'))
# insertDados()


# Exercício 1.2 Faça um programa para listar todos os preços do banco preços.db.
def consultaPreco():
    cursor.execute('select preco from precos')
    result = cursor.fetchall()
    print('Preços:')
    for resultado in result:
        print(f'- {resultado[0]}')
# consultaPreco()


conn.commit()
cursor.close()
conn.close()
