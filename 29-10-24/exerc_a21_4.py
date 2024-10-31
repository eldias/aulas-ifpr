"""
    4. Implementar um programa que armazene os dados de uma turma de alunos. Cada aluno deve ter nome e notas de três disciplinas. O programa deve calcular e mostrar a média das notas de cada aluno e informar quais alunos estão aprovados (média maior ou igual a 7).
"""


n = int(input("Quantos estudantes? "))

lista_de_estudantes = []

for e in range(n):
    estudante: dict = {
        "nome": None,
        "nota_disc_1": None,
        "nota_disc_2": None,
        "nota_disc_3": None,
    }

    estudante['nome'] = input("informe o nome do aluno: ")
    estudante["nota_disc_1"] = float(input("Nota da disciplina 1: "))
    estudante["nota_disc_2"] = float(input("Nota da disciplina 2: "))
    estudante["nota_disc_3"] = float(input("Nota da disciplina 3: "))

    lista_de_estudantes.append(estudante)

for aluno in lista_de_estudantes:
    media = (aluno['nota_disc_1'] + aluno['nota_disc_2'] + aluno['nota_disc_3']) / 3
    print(f'{aluno['nome']} média: {media:.2f}')

    aprovacao = None
    if media >= 7:
        aprovacao = "aprovado!"
    else:
        aprovacao = "reprovado!"

     
    print(f"O aluno {estudante['nome']} teve a média de {media:.2f} e está {aprovacao}")












