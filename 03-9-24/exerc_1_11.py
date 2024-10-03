quantidade_numeros = int(input("Informe a quantidade de números: "))
quantidade_negativa = 0
for i in range(quantidade_numeros):
    num = int(input("Informe um número:"))
    
    if num < 0:
        quantidade_negativa += 1
    
print("A quantidade de números negativos é de:", quantidade_negativa)