def fatorial(n):

    # n = int(input("Informe um número: "))

    produto = 1
    i = n

    while i > 0:
        produto = produto * i
        i = i -1

    print("O resultado é", produto)

fatorial(4)