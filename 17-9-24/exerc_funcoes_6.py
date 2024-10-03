def calcule_areas():
    while True:
        tipo = input("""
Qual tipo de forma para calcularmos a área?
(q)uadrado
(r)etângulo
(t)riângulo
=> """)

        if tipo == "q":
            base = int(input("Qual a medida do base? "))
            area_quadrado = base * base
            print(f"\n\nA área do quadrado é de {area_quadrado}")

        elif tipo == "r":
            base = int(input("Qual a medida do base? "))
            altura = int(input("Qual a medida do base? "))
            area_retangulo = base * altura
            print(f"\n\nA área do quadrado é de {area_retangulo}")

        elif tipo == "t":
            base = int(input("Qual a medida do base? "))
            altura = int(input("Qual a medida do base? "))
            area_triangulo = base * altura / 2
            print(f"\n\nA área do triângulo é de {area_triangulo}")

        
calcule_areas()