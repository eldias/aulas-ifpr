quantidade_numeros = int(input("Informe a quantidade de números: "))
numero_pares = 0
numero_impares = 0

i = quantidade_numeros

while i > 0:
    num = int(input("Informe um número:"))
    
    if num % 2 == 0:
        numero_pares += 1
    else:
        numero_impares += 1
    
    i -= 1
    
print("A quantidade de números pares é de:", numero_pares)
print("A quantidade de números ímpares é de:", numero_impares)