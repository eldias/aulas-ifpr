usuario = input("Informe seu email: ")


if usuario == "eldias@gmail.com":
    senha = input("Informe sua senha: ")
    if senha == "123456":
        print("Acesso liberado")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")