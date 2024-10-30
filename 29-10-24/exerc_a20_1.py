"""
    1. Implementar um programa que faça o cadastro de uma pessoa. Os dados informados pessoais são nome, idade, telefone e e-mail. O programa deve mostrar os dados cadastrados.
"""

"""import re, os

__all__ = ['TextWrapper', 'wrap', 'fill', 'dedent', 'indent', 'shorten']

def cadastra_dados() -> str:
    nome = input("Qual seu nome? ")
    idade = input("Qual a idade? ")
    telefone = input("Qual seu telefone?")
    email = input("Qual seu email?")

    cadastro = {
        "nome": nome.capitalize(),
        "idade": idade.capitalize(),
        "telefone": telefone.capitalize(),
        "email": email.capitalize(),
    }

    os.system('cls')

    print("\nDados cadastrados: \n")

    for chave, valor in cadastro.items():
        print(chave.capitalize(), valor, sep=": ")

os.system('cls')

cadastra_dados()"""

# solução do professor:

pessoa: dict [str, int, str, str] = {}

pessoa["nome"] = str(input("nome: ")).capitalize()
pessoa["idade"] = int(input("idade: "))
pessoa["telefone"] = input("telefone: ")
pessoa["email"] = input("email: ")

print("\n")
print(f"$" * 100)
print("\n")

for chave, valor in pessoa.items():
    print(chave, valor, sep=": ")