import sqlite3

aux = sqlite3.connect('usuarios.db')
cursor = aux.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)

aux.close()