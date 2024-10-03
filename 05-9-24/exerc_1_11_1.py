n = int(input("Quantos elementos para somar? "))

i = 0
soma = 0

while i < n:
    
    num = int(input("Informe um número: "))
    
    if num < 0:
        soma += 1

    i+= 1

print(f"A soma dos valores negativos é de {soma}")