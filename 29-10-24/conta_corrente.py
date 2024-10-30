dicionario: dict = {}
dicionario['agencia'] = input("Insira o nº da agência: ")
dicionario['conta'] = input("Insira o nº da conta: ")
dicionario['titular'] = input("Insira o nome do titular: ")
dicionario['titular'] = f"{dicionario['titular'].capitalize()}"
dicionario['saldo'] = float(input("Insira o saldo inicial: "))
dicionario['saldo'] = f"R$ {dicionario['saldo']:.2f}"


for keys, values in dicionario.items():
    print(keys, values, sep=": ")
