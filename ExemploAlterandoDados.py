import sqlite3

aux = sqlite3.connect('usuarios.db')
cursor = aux.cursor()

senha = 'pedro0910'
novo_email = 'pedrohb@gmail.com'

# alterando os dados da tabela
cursor.execute("""
UPDATE usuarios
SET email = ?
WHERE senha = ?
""", (novo_email, senha))

aux.commit()

print('Dados atualizados com sucesso!')

aux.close()