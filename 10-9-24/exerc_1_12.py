# 1.  Implemente um programa que some todos os números informados pelo usuário até que seja digitada a palavra "Fim".

soma = 0
entrada = 0

while entrada != "Fim":
    soma += int(entrada)
    entrada = input("Informe o número ou digite Fim: ")
    
print(f"Resultado da soma é {soma}")