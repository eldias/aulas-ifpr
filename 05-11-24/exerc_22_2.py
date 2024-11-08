"""
    2. Implementar um programa que leia e exiba todo o conteúdo de um arquivo de texto. O usuário deve informar o caminho do arquivo a ser lido.
"""
import textwrap

caminho: str = input("Qual o caminho do arquivo? ")
if caminho == "":
    caminho = "05-11-24/anedota.txt"
with open(caminho, "r", encoding="ISO-8859-1") as acesso:
    print(acesso.read())
