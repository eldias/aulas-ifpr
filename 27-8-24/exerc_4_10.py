quantidade_numeros = int(input("Qual a quantidade de números? "))

menor_valor = ""

for i in range(quantidade_numeros):
    numero_pedido = int(input("Qual o próximo número? "))
    
    if menor_valor == "":
        menor_valor = numero_pedido

    if numero_pedido <= menor_valor:
        resultado = numero_pedido
        menor_valor = numero_pedido
    else:
        resultado = menor_valor
                 
print("O menor número é: ", resultado)