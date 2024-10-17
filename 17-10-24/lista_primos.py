def primo(num):
    divisores = 0
    i = 1
    while i <= num:
        if num % i == 0:
            divisores += 1
        i += 1

    if divisores == 2:
        return True
    else:
        return False
    
# ---------------------------------------------------------
n = int(input("Qual o último valor do intervalo?:\n==> "))
num_primos = []

for e in range(2 , n + 1):
    if primo(e):
        num_primos.append(e)

print(num_primos)