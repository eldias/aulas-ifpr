def calc_imc(altura, peso):
    imc = peso / (altura * altura)
    return imc


p = float(input("Qual o peso em Kg? "))
a = float(input("Qual a altura em metros? "))
q = calc_imc(a, p)
print(f"O IMC é de: {q:.0f}")