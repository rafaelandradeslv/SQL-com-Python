import sqlite3
from contextlib import closing

# -- consulta com filtro de seleção (WHERE)--


def consultaFiltroSelecao():
    with sqlite3.connect('cap_1_conceitos_básicos/agenda.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""select * 
                            from agenda 
                            where nome = 'João'
                            """)
            while True:
                result = cursor.fetchone()
                if result == None:
                    break
                print(f"Nome: {result[0]}, Telefone: {result[1]}", )


# -- consulta através de variável --
def consultaPorVariavel():
    nome = input('Nome a selecionar: ')
    with sqlite3.connect('cap_1_conceitos_básicos/agenda.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(f"""select * 
                               from agenda
                               where nome = '{nome}'
                            """)
            while True:
                result = cursor.fetchone()
                if result == None:
                    break
                print(f"Nome: {result[0]}, Telefone: {result[1]}")


# -- consulta utilizando parâmetros -- 
def consultaUtilizandoParametro():
    nome = input('Nome a selecionar: ')
    with sqlite3.connect('cap_1_conceitos_básicos/agenda.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("select * from agenda where nome = ?", (nome,))
            x = 0
            while True:
                resultado = cursor.fetchone()
                if resultado == None:
                    if x == 0:
                        print('Nada encontrado')
                    break
                print(f"Nome: {resultado[0]}, Telefone: {resultado[1]}")
                x += 1
            