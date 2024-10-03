ins_ano = int(input("Insira o ano a verificar: "))

if (((ins_ano % 400) == 0) or ((ins_ano % 4) == 0)) and ((ins_ano % 100) != 0):
    print("Este ano é bissexto")
else:
    print("Este ano NÂO é bissexto.")