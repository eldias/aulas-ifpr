numero_da_conta = input("Informe o número da conta:\n")
saldo = 500.00

if numero_da_conta == "858585-8":
    senha = input("Informe sua senha:\n")
    if senha == "54321":
        print("Bem-vindo, acesse as opções abaixo:\n")
        print("1. Mostrar saldo atual\r")
        print("2. Fazer um saque\r")
        print("3. Fazer um depósito\r")
        print("4. Sair\r")
        opcao_menu = input("\rEscolha uma opção numérica:\n")
        if opcao_menu == "1":
            print("Seu saldo atual é de R$","%.2f" %  saldo)
        elif opcao_menu == "2":
            valor_saque = float(input("Qual valor que gostaria de sacar da conta?"))
            saldo = saldo - valor_saque
            print("Seu saldo atual é de R$","%.2f" %  saldo)
    else:
        print("Acesso negado.Senha incorreta, tente novamente.\n")
else:
    print("Conta não encontrada. Favor tentar novamente.\n")
