base = float(input("Informe a base: "))
expoente = int(input("Informe o expoente: "))
resultado = 1

for i in range(expoente):
    resultado *= base

print("O resultado do cálculo é:", resultado)
