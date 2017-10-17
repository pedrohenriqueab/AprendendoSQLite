import sqlite3

aux = sqlite3.connect('usuarios.db')
cursor = aux.cursor()

# criando uma lista de dados
lista = [(
    'Rhavy', 'rhavy@gmail.com', 'rhavy159'),
    ('Sabriny', 'sabrys@gmail.com', 'sabrineee159'),
    ('Pedro', 'pedroca@gmail.com', 'pedroso159')]

# inserindo dados na tabela
cursor.executemany("""
INSERT INTO clientes (nome, email, senha)
VALUES (?,?,?)
""", lista)

aux.commit()

print('Dados inseridos com sucesso.')

aux.close()