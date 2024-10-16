"""
    2. Implementar um programa que, a partir do usuário, receba um conjunto de números e troque o primeiro e o último número informados de posição. O usuário deverá informar inicialmente qual é a quantidade de números da lista.
"""
quantidade_numeros = int(input("Informe a quantidade de números: "))
lista = list()
i = 1


while i <= quantidade_numeros:
    num = int(input("Informe um número: "))
    lista.append(num) 
    i += 1
    
prim_lista = lista[0]
ult_lista = lista[-1]

print(prim_lista, ult_lista)
print(lista)

print(f"\nTrocando...\n")

remove_prim = lista.pop(prim_lista)
print("Retirando index 0")
print(lista, "\n")

lista.index(-1, remove_prim)
remove_ult = lista.pop(ult_lista)
lista.index(-1, remove_ult)

print(prim_lista, ult_lista)
print(lista)
