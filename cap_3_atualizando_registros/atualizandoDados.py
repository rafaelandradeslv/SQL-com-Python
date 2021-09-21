import sqlite3
from contextlib import closing


# -- atualizando dados (update) --
def atualizandoDados():
    with sqlite3.connect('cap_1_conceitos_básicos/agenda.db') as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""
                            update agenda
                            set telefone = "2655-8973"
                            where nome = 'Nilo'
                            """)
            cursor.execute('select * from agenda where nome = "Nilo"')
            result = cursor.fetchone()
            print(result)

# ATENÇÃO: quando a query utilizando update não utiliza where, todos os valores
# da coluna selecionada serão alteradas.


# -- Verificando quantos valores foram alterados --
with sqlite3.connect('cap_1_conceitos_básicos/agenda.db') as conn:
    with closing(conn.cursor()) as cursor:
        print('Registros alterados: ', cursor.rowcount)
