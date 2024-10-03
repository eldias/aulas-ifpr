num = int(input("Qual o número: "))
soma = 0

while num != 0:
    resto = num % 10
    soma += resto
    num = num // 10
    
print(f"A soma dos algarismos é: {soma}")