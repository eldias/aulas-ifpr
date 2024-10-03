p = 8
q = 4
r = 2
resultado = (p - q * r <= q) and (not (r ** 2 > p))

print(resultado)

(p - q * r <= q) and (not (r ** 2 > p))
(8 - 4 * 2 <= 4) and (not (2 ** 2 > 8))
(4 <= 4) and (not (4 > 8))
(True) and (not (False))
True and True
True