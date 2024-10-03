altura = float(input("Insira a altura em metros para análise do IMC:\n"))
peso = float(input("Insira o seu peso em Kg para análise do IMC:\n"))

imc = peso / (altura ** 2)

print("Seu IMC é de","%.2f" % imc, "\n")

if imc > 30:
    print("IMC está em nível de obesidade")
elif imc > 25:
    print("IMC está acima do peso")
elif imc > 18.5:
    print("IMC está normal")
else:
    print("IMC está abaixo do peso")