"""Implementar um programa que permita ao usuário adicionar elementos em uma lista até que ele decida parar. Em seguida, o programa deve exibir a lista resultante e a quantidade de elementos.
"""
lista = list() # criação de lista
parar = 'fim' # define comando na variável stop

while True: # abre loop while
    termo = input() # define val com entrada de texto
    if termo == parar: # loop se val for stop
        break # pare o loop
    lista.append(termo) # adicione os temos em lista

print('Sua lista é: ',lista) # imprima a lista
