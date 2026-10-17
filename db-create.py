import sqlite3

#criar ou abrir o banco de dados
conexao = sqlite3.connect("escola.db")

cursor = conexao.cursor()

#criar tabelas de alunos
cursor.execute("""
create table if not exists aluno(
    codigo integer primary key autoincrement,
    nome text not null,
    idade integer,
    curso text
)
""")

conexao.commit()
conexao.close()

print("Banco de dados e tabela aluno criados com sucesso!")