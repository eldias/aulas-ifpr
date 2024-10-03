def calcular_area(base, altura):
    """
    Função que calcula a área do retângulo:

    Args:
        - base: Valor do tipo float
        - altura: Valor do tipo float

    Returns:
        - retorna o valor 
    """


    area = base * altura
    return area

# ---------------------------------------------------------

b = float(input("Informe a base: "))
h = float(input("Informe a altura: "))
a = calcular_area(b, h)
print("O valor da área do retângulo é", a)