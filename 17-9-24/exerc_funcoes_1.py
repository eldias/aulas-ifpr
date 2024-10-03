def area_retang(base, altura):
    area_ret = base * altura
    return area_ret


b = float(input("Qual a medida de base? "))
h = float(input("Qual a medida de altura? "))

a = area_retang(b, h)

print(f"A área do retângulo é de {a}")

