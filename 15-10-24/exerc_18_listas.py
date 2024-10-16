"""
    2. Implementar um programa que, a partir do usuário, receba um conjunto de números e troque o primeiro e o último número informados de posição. O usuário deverá informar inicialmente qual é a quantidade de números da lista.
"""

# Pedir ao usuário a quantidade de números a computar
quantidade_numeros = int(input("Informe a quantidade de números: "))
# Cria lista vazia
lista = list()
# i recebe 1 
i = 1
# Loop em i para informar os números a inserir na lista usando append
while i <= quantidade_numeros:
    num = int(input("Informe um número: "))
    lista.append(num) 
    i += 1
# define variáveis para o receber o primeiro e últimos números da lista
primeiro = lista[0]
ultimo = lista[-1]
# retirar primeiro e último item da lista
lista.pop(0)
lista.pop(-1)
# Inserir as variáveis do primeiro e últimos números da lista de volta, invertendo a ordem deles
lista.insert(0, ultimo)
l = lista[-1]
lista.insert(l, primeiro)
print(lista)