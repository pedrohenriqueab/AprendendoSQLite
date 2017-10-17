import sqlite3

aux = sqlite3.connect('usuarios.db')
cursor = aux.cursor()
nome_tabela = 'usuarios'

# obtendo informações da tabela
cursor.execute('PRAGMA table_info({})'.format(nome_tabela))

for coluna in colunas:
    print(coluna)

# listando as tabelas do bd
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print('Tabelas:')
for tabela in cursor.fetchall():
    print("%s" % (tabela))

# obtendo o schema da tabela
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,))

print('Schema:')
for schema in cursor.fetchall():
    print("%s" % (schema))

aux.close()