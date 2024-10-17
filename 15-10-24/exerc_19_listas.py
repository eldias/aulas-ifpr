"""
    3. Implementar um programa que verifique se um número está presente em uma lista de números informados pelo usuário. O programa deve solicitar inicialmente a lista de números e depois o número a ser buscado.
"""
import time

lista = list() # criação de lista
parar = 'fim' # define comando na variável stop

while True: # abre loop while
    termo = input("Insira os números da lista. Para parar, digite 'fim'.\n=> ") # define valores com entrada de texto
    if termo == parar: # loop se termo for fim
        break # pare o loop
    lista.append(termo) # adicione os itens na lista

print(f"\nSua lista é: {lista}\n") # imprima a lista


buscar = input("Qual o número a ser buscado?\n=> ")
if buscar in lista:
    print(f"O número {buscar} está na lista.")
else:
    print(f"O número {buscar} NÃO está na lista.")