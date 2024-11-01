"""
    Implementar um programa que conta o número de vogais em uma string informada pelo usuário. Por exemplo, a entrada "Aprender Python" deve retornar 5.
"""

vogais: str = "aeiou"
palavra: str = input("Palavra? ")

total_vogais: list = []

for letra in palavra.lower():
    if letra in vogais:
        total_vogais.append(letra)

print(len(total_vogais))