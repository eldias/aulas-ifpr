salario_bruto = float(input("Informe seu salário bruto: "))

if salario_bruto <= 1412:
    faixa_1 = (salario_bruto ) * .075
    valor_inss = faixa_1
            
elif salario_bruto <= 2666.68:
    faixa_2 = (salario_bruto - 1412.00) * .09
    valor_inss = 105.90 + faixa_2

elif salario_bruto <= 4000.03:
    faixa_3 = (salario_bruto - 2666.68) * .12
    valor_inss = 105.90 + 112.92 + faixa_3
    
elif salario_bruto <= 7786.02:
    faixa_4 = (salario_bruto - 4000.03) * .14
    valor_inss = 105.90 + 112.92 + 160.00 + faixa_4

print("\nO valor da contribuição previdenciária é de R$","%.2f" %  valor_inss)


salario_restante = salario_bruto - valor_inss
print("\nO salário restante foi de R$", "%.2f" %  salario_restante)

if salario_restante < 2259.20:
    print("\nEstá isento de pagamento do IRPF.")
    aliquota_irpf = 0
    
elif salario_restante < 2826.65:
    aliquota_irpf = (salario_restante * .075) - 169.44
    
elif salario_restante < 3751.05:
    aliquota_irpf = (salario_restante * .15) - 381.44
    
elif salario_restante < 4664.68:
    aliquota_irpf = (salario_restante * .225) - 662.77
    
else:
    aliquota_irpf = (salario_restante * .275) - 896.00
    

salario_liquido = salario_restante - aliquota_irpf

print("\nO imposto devido será de R$", "%.2f" % aliquota_irpf)
print("\rO salário líquido será de R$", "%.2f" % salario_liquido)