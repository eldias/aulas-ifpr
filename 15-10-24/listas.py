import os

# Tipo de Listas

lista1 = []
lista2 = list()
lista3 = [1,2,3,4]
lista4 = list(lista3)
lista5 = [1,2,'Texto', 'abacate', 'uva']

# Exibição

os.system('cls')

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print("Tamanho da lista 3: ", len(lista3))
print("Tamanho da lista 5: ", len(lista5))
print("\n\n")

tecla = ""

tecla = input("Any keys to continue: ")

if tecla == any:
    os.system('cls')
    pass

print(lista5[0])
print(lista5[3])