import sqlite3
#criando db
aux = sqlite3.connect('usuarios.db')
#definindo cursor
cursor = aux.cursor()
#criando o schema
cursor.execute("""
CREATE TABLE usuarios (
               nome TEXT NOT NULL,
               email TEXT NOT NULL,
               senha VARCHAR NOT NULL PRIMARY KEY,
);
""")

print("tabela criada com sucesso")
#desconectando
aux.close()