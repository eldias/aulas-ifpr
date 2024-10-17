import random

valores = []
for e in range(100):
    valor = random.randint(0, 1000) # Função de número aleatório
    valores.append(valor)

indice = int(input("Qual o índice a pesquisar?"))

print(valores)

print(f"\nO valor corresponte ao índice {indice} é {valores[indice]}")


