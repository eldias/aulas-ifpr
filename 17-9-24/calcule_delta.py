def calcular_delta(a, b, c):
    delta =  b ** 2 - 4 * a * c
    return delta

# ----------------------------------------

def calcular_eq_segundo_grau(a, b, c):
    delta = calcular_delta(a, b, c)
    x1 = (-b + delta ** .5) / 2 * a
    x2 = (-b - delta ** .5) / 2 * a
    return x1, x2

# ----------------------------------------

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

print(f"\n{a:.0f}x² + {b:.0f}x + {c:.0f} = 0\n")

d = calcular_delta(a, b, c)

print(f"Delta da equação é {d:.0f}\n")

x1, x2 = calcular_eq_segundo_grau(a, b, c)

print(f"As raízes da equação são {x1:.0f} e {x2:.0f}")

