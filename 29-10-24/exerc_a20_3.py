"""
3. Implementar um programa que utilize um dicionário para armazenar os nomes e telefones de contatos. O usuário deve poder adicionar, remover e buscar contatos. Ao final, o programa deve mostrar todos os contatos cadastrados.
"""
def inserir_contato(contatos: list, nome: str, telefone: str) -> None:
    contatos[nome] = telefone

def remover_contatos(contatos: list, nome: str):
    contatos.pop(nome)

def buscar_contato(contatos, nome: str):
    if nome in contatos:
        return contatos[nome]
    else:
        return None


def imprimir_contatos(contatos):
    for nome, telefone in contatos.items():
            print(nome, telefone, sep=", ")
    

contatos_telefonicos: dict = {}

while True:
    print("1 - inserir")
    print("2 - Remover")
    print("3 - Buscar")
    print("4 - Imprimir todos")
    print("0 - Sair")

    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        nome = input("nome? ")
        telefone = input("telefone? ")
        inserir_contato(contatos_telefonicos, nome, telefone)
    elif opcao == 2:
        nome = input("nome? ")
        remover_contatos(contatos_telefonicos, nome)
    elif opcao == 3:
        nome = input("nome? ")
        buscar_contato(contatos_telefonicos, nome)
    elif opcao == 4:
        imprimir_contatos(contatos_telefonicos)
    elif opcao == 0:
        break
    else:
        print("opção inválida")