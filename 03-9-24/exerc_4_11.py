quantidade_numeros = int(input("Informe a quantidade de números: "))
soma = 0
for i in range(quantidade_numeros):
    num = int(input("Informe um número:"))
    soma += num
    
media = soma / quantidade_numeros

print(f"A média é de {media}")