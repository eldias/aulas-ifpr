"""
1. Implementar um programa que verifique quais estudantes praticam simultaneamente atletismo e basquete. O usuário deve informar os estudantes de atletismo e, depois, os de basquete. O programa deve exibir os alunos que participam de ambas as atividades.
"""

atletismo = set()
basquete = set()

# código em while
""" parar = 'fim' # define comando na variável stop

while True: # abre loop while
    termo = input("Insira um nome para adicionar ao time de atletismo: ") # define val com entrada de texto
    if termo == parar: # loop se val for stop
        break # pare o loop
    atletismo.add(termo) # adicione os temos em lista

print('Sua lista é de jogadores de atletismo são: ',atletismo) # imprima a lista

while True: # abre loop while
    termo = input("Insira um nome para adicionar ao time de basquete: ") # define val com entrada de texto
    if termo == parar: # loop se val for stop
        break # pare o loop
    basquete.add(termo) # adicione os temos em lista

print('Sua lista é de jogadores de basquete são: ',basquete) # imprima a lista """

n = int(input("Qtde estudantes: "))
for e in range(n):
    estudante = input("Nome do estudante: ")
    atletismo.add(estudante)

n = int(input("Qtde estudantes: "))
for e in range(n):
    estudante = input("Nome do estudante: ")
    basquete.add(estudante)

jogadores = atletismo & basquete # interseção

print(f"\nOs jogadores que estão em ambos times são:\n{jogadores}")