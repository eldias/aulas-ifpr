"""
    4. Implementar um programa que, a partir do usuário, receba um conjunto de nomes de pessoas e os apresente em ordem alfabética. O usuário deverá informar inicialmente qual é a quantidade de nomes.
"""
n = int(input("Informe a quantidade de nomes: "))
lista = list() # criação de lista
# parar = 'fim' # define comando na variável stop

for i in range(n):
    nome = input("Informe um nome: ")
    lista.append(nome)

    
lista.sort()
print(f"\nSua lista ordenada:")
[print(item) for item in lista]





""" while True: # abre loop while
    termo = input("Insira os nomes da lista, pare digitando 'fim'.\n=> ") # define val com entrada de texto
    if termo == parar: # loop se val for stop
        break # pare o loop
    lista.append(termo) # adicione os temos em lista

print(f"Sua lista ordenada é: {sorted(lista)}") # imprima a lista ordenada """