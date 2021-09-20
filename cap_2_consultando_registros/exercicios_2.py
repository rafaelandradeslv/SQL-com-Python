import sqlite3
from contextlib import closing

# Exercício 1.3 Escreva um programa que realize consultas do banco de dados
# preços.db, criado no exercício 1.1. O programa deve perguntar o nome do produto
# e listar seu preço.


def consultandoPrecos():
    consulta = input('Nome do produto: ')

    with sqlite3.connect('cap_1_conceitos_básicos/precos.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''select * 
                            from precos
                            where nome_do_produto = ?''', (consulta, ))
            # x = 0
            while True:
                result = cursor.fetchone()
                if result == None:
                    # if x == 0:
                    #     print('Nada encontrado')
                    break
                print(f'Preço: {result[1]}')


# Exercício 1.4 Modifique o programa do exercício 1.3 de forma a perguntar dois
# valores e listar todos os produtos com preços entre esses dois valores.
def consultaDoisProdutos():
    consulta = input('Digite o primeiro produto: ')
    consulta2 = input('Digite o segundo produto: ')

    with sqlite3.connect('cap_1_conceitos_básicos/precos.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(f'''select * 
                                from precos
                                where nome_do_produto = "{consulta}" or nome_do_produto = "{consulta2}"
                            ''')
            while True:                                
                result = cursor.fetchone()
                if result == None:
                    print('Nada encontrado')
                    break
                print(result)
