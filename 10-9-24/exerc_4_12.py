# 4. Implemente um programa que simule um sistema de caixa de supermercado. O programa deve solicitar a quantidade e o valor unitário de cada produto. Esse processo deve ser repetido até que o usuário informe a palavra "fim". Após a entrada da palavra "fim", o programa deve exibir o valor total da compra.

soma = 0
quantidade = ""
valor = 0

while  quantidade != "Fim":
    quantidade = input("Informe a quantidade do produto ou digite Fim: ")
    if quantidade != "Fim":
        valor = float(input("Informe o valor: "))
        total_produto = int(quantidade) * valor
        soma += total_produto
    
print(f"Resultado da soma é {soma}")
