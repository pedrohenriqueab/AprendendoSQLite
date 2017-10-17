import sqlite3

aux = sqlite3.connect('usuarios.db')
cursor = aux.cursor()

senha = 'rhavy159'

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM usuarios
WHERE senha = ?
""", (senha,))

aux.commit()

print('Registro excluido com sucesso.')

aux.close()