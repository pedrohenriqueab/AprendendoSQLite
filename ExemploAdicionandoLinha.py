import sqlite3

aux = sqlite3.connect('usuarios.db')
cursor = aux.cursor()

# adicionando uma nova coluna na tabela clientes
cursor.execute("""
ALTER TABLE usuarios
ADD COLUMN sexo BOOLEAN;
""")

aux.commit()

print('Novo campo adicionado com sucesso!')

aux.close()