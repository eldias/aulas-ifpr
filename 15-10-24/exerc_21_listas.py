"""
    5. Implementar um programa que solicite ao usuário duas listas de números. O programa deverá concatenar as listas e exibir o resultado.
"""

n1 = int(input("Informe a quantidade da lista1: "))
n2 = int(input("Informe a quantidade da lista2: "))

lista1 = []
for i in range(n1):
    num = int(input("Informe um número: "))
    lista1.append(num)

lista2 = []
for i in range(n2):
    num = int(input("Informe um número: "))
    lista2.append(num)

lista1.extend(lista2)
lista2 = []
[print(i) for i in lista1]


""" 
import os

lista = list() # criação de lista
lista2 = list()
parar = 'fim' # define comando na variável stop

while True: # abre loop while
    termo = input("Insira os itens da primeira lista, pare digitando 'fim'.\n=> ") # define val com entrada de texto
    if termo == parar: # loop se val for stop
        break # pare o loop
    lista.append(termo) # adicione os temos em lista

while True: # abre loop while
    termo = input("Agora vamos a segunda lista.\nInsira os itens da lista, pare digitando 'fim'.\n=> ") # define val com entrada de texto
    if termo == parar: # loop se val for stop
        break # pare o loop
    lista2.append(termo) # adicione os temos em lista

lista_concatenada = lista + lista2
os.system('cls')
print(f"\nA lista 1 é: {lista}\n")
print(f"A lista 2 é: {lista2}\n")
print(f"A lista concatenada é: {lista_concatenada}\n\n")



 """