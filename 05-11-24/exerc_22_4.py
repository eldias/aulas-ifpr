"""
    4. Implementar um programa que simule um sistema básico de autenticação. O programa deve ler um arquivo de texto fixo, onde estão armazenados o nome de usuário e a senha. O usuário deverá informar seu nome de usuário e senha, e o programa verificará se as informações correspondem aos dados salvos no arquivo.
"""
import getpass

caminho: str = "05-11-24/auth.txt"
auth: list = []
with open(caminho, "r", encoding="ISO-8859-1") as acesso:
    
    for linha in acesso:
        dados_linha: list = linha.replace("\n", "").split(";")
        auth.append(dados_linha)

login = auth[0][1] # login = eldias
senha = auth[1][1] # senha = 1234


while True:
    q_login: str = input("Qual o nome do usuário? ")
    q_senha: str = getpass.getpass("Qual a senha do usuário? ")
    if q_login == login:
        if q_senha == senha:
            print(f"\nOlá, você está logado!")
            break
        else:
            print(f"Erro! Favor tentar novamente a senha.\n Esqueceu sua senha? Clique aqui.(link para recuperação de senha por e-mail)")
    else:
        print("Usuário incorreto! Tente novamente.")

print('"Usuário acessou o sistema"\n')