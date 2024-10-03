# Desafio Fibonacci

n = int(input("Qual elemento da sequencia vc deseja: "))

if n < 3:
    atual = 1
    print(atual, end=" ")
else:
    ultimo = 1
    penultimo = 1
    for e in range(2, n):
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual
    print(atual, end=" ")