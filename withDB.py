import sqlite3
from contextlib import closing


# --- Consulta um por um utilizando WITH --- 
def umAum():
    with sqlite3.connect("agenda.db") as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('select * from agenda')

            while True:
                result = cursor.fetchone()
                if result == None:
                    break
                print(f'Nome: {result[0]}\nTelefone: {result[1]}')




