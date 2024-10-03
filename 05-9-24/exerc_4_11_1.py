quantidade_numeros = int(input("Informe a quantidade de números: "))
soma = 0
i = 1


while i <= quantidade_numeros:
    num = int(input("Informe um número: "))
    soma += num
    i += 1
    
media = soma / quantidade_numeros

print(f"A média dos números  é {media}")