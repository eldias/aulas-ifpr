numero = int(input("Qual o número a ser fatorado? "))
number = numero
resultado = ""

if numero == 0:
    fatorial = 2
    numero = 1
else:
    fatorial = numero + 1

for i in range(numero, 0, -1):
    fatorial -= 1
    resultado += str(fatorial)
    
    if i == 1:
        resultado = resultado
    else:
        resultado += " * "
            
print("\nO Número fatorado é: ", number,"! = ", resultado," = ", eval(resultado),"\n")