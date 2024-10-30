"""
    2. Implementar um programa que faça o cadastro de produtos de um supermercado. Um produto tem descrição, valor e código de barras (número inteiro). O usuário deve informar quantos produtos deseja cadastrar. O programa deve mostrar a lista de produtos cadastrados.
"""


n: int = int(input("quant prod? "))

produtos: list = []

for e in range(n):
    produto: dict = {}
    produto["desc"] = input("desc: ")
    produto["valor"] = float(input("valor: "))
    produto["EAN"] = int(input("EAN: "))
    produtos.append(produto)

print(*produtos, sep="\n")