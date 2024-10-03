def calcule_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

p = float(input("Qual seu peso em Kg? "))
h = float(input("Qual sua altura em metros? "))
    
a = calcule_imc(p, h)

print(f" O IMC calculado é de {a}")
