salario_bruto = float(input("Insira o salário bruto:"))

inss = 0

if salario_bruto <= 1412:
    inss = salario_bruto * .075
elif salario_bruto <= 2666.68:
    faixa_salario = salario_bruto - 1412.01
    inss = faixa_salario * .09 + 1412 * .075
elif salario_bruto <= 4000.03:
    faixa_salario = salario_bruto - 2666.69
    inss = faixa_salario * .12 + 1254.67 * .09 + 1412 * .075
elif salario_bruto <= 7786.02:
    faixa_salario = salario_bruto - 4000.04
    inss = faixa_salario * .14 + 1333.34 * .12 + 1254.67 * .09 + 1412 * .075
else:
    inss = 3785.98 * .14 + 1333.34 * .12 + 1254.67 * .09 + 1412 * .075

salario_tributavel = salario_bruto - inss

imposto = 0

if salario_tributavel <= 2259.2:
    imposto = 0
elif salario_tributavel <= 2826.65:
    imposto = salario_tributavel * .075 - 169.44
elif salario_tributavel <= 3751.05:
    imposto = salario_tributavel * .15 - 381.44
elif salario_tributavel <= 4664.68:
    imposto = salario_tributavel * .225 - 662.77
else:
    imposto = salario_tributavel * .275 - 896

salario_liquido = salario_tributavel - imposto


print("%.2f" %  inss)
print("%.2f" %  salario_bruto)
print("%.2f" %  salario_tributavel)
print("%.2f" %  imposto)
print("%.2f" %  salario_liquido)


    