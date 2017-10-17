import sqlite3

aux = sqlite3.connect('usuarios.db')
cursor = aux.cursor()

# solicitando os dados ao usuário
p_nome = input('Nome: ')
p_email = input('Email: ')
p_senha = input('Senha: ')

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, email, senha)
VALUES (?,?,?)
""", (p_nome, p_email, p_senha))

aux.commit()

print('Dados inseridos com sucesso.')

aux.close()