# Distância = √︃((x1 – x2 )² + (y1 – y2 )² + (z1 – z2 )²)
import math

def calc(p1, p2):
    dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    return dist

x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))
ponto1 = (x1, y1, z1)

x2 = float(input("x2: "))
y2 = float(input("y2: "))
z2 = float(input("z2: "))
ponto2 = (x2, y2, z2)

distancia = calc(ponto1, ponto2)
print(f"{distancia:.2f}")