valor_operador = float(input("Insira o valor total da compra:\n"))

tipo_pagamento = input("O valor será:\n1 - À vista\n2 - À prazo\n")

if tipo_pagamento == "2":
    qtde_parc = int(input("Qual a quantidade de parcelas? "))
    valor_prazo = valor_operador / qtde_parc
    print("O valor a prazo será de",qtde_parc,"X de R$", "%.2f" % valor_prazo)
elif tipo_pagamento == "1":
    valor_a_vista = valor_operador * .9
    print("O Valor à vista será de R$ ", "%.2f" % valor_a_vista)
else:
    print("Esta opção não é válida")