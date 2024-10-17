"""
    5. Implementar um programa que solicite ao usuário duas listas de números. O programa deverá concatenar as listas e exibir o resultado.
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



