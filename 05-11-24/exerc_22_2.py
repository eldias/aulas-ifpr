caminho: str = input("Qual o caminho do arquivo? ")
if caminho == "":
    caminho = "aulas-ifpr/05-11-24/anedota.txt"
with open(caminho, "r", encoding="ISO-8859-1") as acesso:
    print(acesso.read())
