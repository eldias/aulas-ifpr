nome: str = input("Qual seu nome? ")
caminho: str = input("Onde gostaria de salvar o arquivo? ")
if caminho == "":
    caminho = "aulas-ifpr/05-11-24/"
arquivo: str = "nomes.txt"
abspath: str = caminho + arquivo

with open(abspath, "w") as acesso:
    acesso.write(nome)
