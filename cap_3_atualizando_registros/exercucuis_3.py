import sqlite3
from contextlib import closing
# Exercício 1.5 Escreva um programa que aumente o preço de todos os produtos
# do banco preços.db em 10%


def aumentoDezPorcento():
    with sqlite3.connect('cap_1_conceitos_básicos/precos.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('select * from precos')
            result = cursor.fetchall()

            for valor in result:
                num = float(valor[1])
                num2 = round(num * 0.01 + num, 2)

                cursor.execute(f"""update precos
                                   set preco = '{num2}'
                                   where nome_do_produto = '{valor[0]}'
                                   """)


# Exercício 1.6 Escreva um programa que pergunte o nome do produto e um novo
# preço. Usando o banco preços.db, atualize o preço deste produto no banco de dados.
def atualizandoPreco():
    with sqlite3.connect('cap_1_conceitos_básicos/precos.db') as conn:
        with closing(conn.cursor()) as cursor:
            # visualizando dados da tabela
            cursor.execute('select * from precos')
            result = cursor.fetchall()
            for NomesDosDados in result:
                print(NomesDosDados)
            
            # Atualizando dados do item desejado
            pergunta = input('Qual item para alterar o preço: ')
            novoPreco = input('Novo preço: ')
            cursor.execute(f'''update precos
                              set preco = "{novoPreco}"
                              where nome_do_produto = "{pergunta}"
                              ''')


atualizandoPreco()
