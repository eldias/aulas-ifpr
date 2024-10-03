def fatorial(num):
    """
    _summary_

    Args:
        num (_type_): _description_
    """

    produto = 1

    for e in range(num, 0, -1):
        produto *= e

    return produto

num = int(input("Qual o numero? "))
fat = fatorial(num)
print(fat)
    