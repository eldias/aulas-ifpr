def area_quadrado(lado):
    area = lado * lado
    return lado

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def area_retangulo(base, altura):
    area = base * altura
    return area

# ------------------------------

print("Calcular area")
print("1 - Quadrado")
print("2 - Triangulo")
print("3 - Retângulo")

opcao = int(input("Qual a opção escolhida? "))

if opcao == 1:
    lado = float(input("qual o lado? "))
    area = area_quadrado(lado)
elif opcao == 2:
    base = float(input("Qual a base? "))
    altura = float(input("Qual a altura"))
    area = area_triangulo(base, altura)
elif opcao == 3:
    base = float(input("Qual a base? "))
    altura = float(input("Qual a altura"))
    area = area_retangulo(base, altura)

print(area)

