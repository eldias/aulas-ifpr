"""
    1.  Implementar um programa que solicite ao usuário seu nome completo e salve essa informação em um arquivo de texto. O usuário deve informar o nome completo e o caminho do arquivo onde o dado será armazenado.
"""


nome: str = input("Qual seu nome? ")
caminho: str = input("Onde gostaria de salvar o arquivo? ")
if caminho == "":
    caminho = "05-11-24/"
arquivo: str = "nomes.txt"
abspath: str = caminho + arquivo

with open(abspath, "w") as acesso:
    acesso.write(nome)
