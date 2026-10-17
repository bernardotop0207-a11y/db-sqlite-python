import sqlite3

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

nome = input("Nome do aluno: ")
idade = int(input("Idade: "))
curso = input("Curso: ")

cursor.execute("""
insert into aluno (nome, idade, curso) values (?, ?, ?)
""", (nome, idade, curso))

conexao.commit()
conexao.close()

print("Aluno cadastrado com sucesso")