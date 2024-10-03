quantidade_numeros = int(input("Qual a quantidade de números? "))
soma = 0
for i in range(quantidade_numeros):
    numero = int(input("Qual o próximo número? "))
    soma += numero

print("O total dos números somados é: ", soma)
