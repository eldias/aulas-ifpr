"""
    3. Implementar um programa que conte e exiba o número total de linhas de um arquivo de texto. O usuário deve fornecer o caminho do arquivo a ser analisado.
"""


caminho: str = input("Qual o caminho do arquivo? ")
if caminho == "":
    caminho = "05-11-24/anedota.txt"
with open(caminho, "r", encoding="ISO-8859-1") as acesso:
    linhas = acesso.readlines()
    print(*linhas)
    quantidade_linhas = len(linhas)
    print(f"\nEste texto possui {quantidade_linhas} linhas.")