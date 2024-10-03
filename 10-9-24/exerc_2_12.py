# 2. Implemente um programa que, dado um número inteiro informado pelo usuário, informe se o número é primo. Um número é considerado primo se for divisível apenas por 1 e por ele mesmo.

num = int(input("Digite um número para vermos se ele é um número primo: "))

i = 1
cont_divisores = 0

while i <= num:
    if num % i == 0:
        cont_divisores += 1
    if cont_divisores >= 3:
        break
    i += 1

if cont_divisores == 2:
    print("O número é primo.")
else:
    print("O número não é primo.")