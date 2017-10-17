import sqlite3

aux = sqlite3.connect('usuarios.db')
cursor = aux.cursor()

#Colocando dados dentro da tabela

cursor.execute("""
INSERT INTO usuarios (nome, email, senha)
VALUES ('Pedro', 'peedrohenriquearaujo@gmail.com', 'pedro0910')
""")

cursor.execute("""
INSERT INTO usuarios (nome, email, senha)
VALUES ('Sabriny', 'sabrinypereirabezerra@gmail.com', 'sabriny0')
""")

cursor.execute("""
INSERT INTO usuarios (nome, email, senha)
VALUES ('Rhavy', 'Rhavy@gmail.com', 'euamopython123')
""")

#gravando bd
aux.commit()

print('Dados inseridos com sucesso.')

aux.close()