# Qual o valor das variáveis a, b e c após a execução do laço de repetição?

a = 3
b = 4
c = 5
while a < b:
    b = b + 1
    c = c + a

print(f"Valores: {a, b, c}")

# Resposta: O loop é infinito, a = 3, b sempre incrementa ele msm +1 e c sempre incrementa ele msm e 3

