"""
    Implementar um programa que conta o número de vogais em uma string informada pelo usuário. Por exemplo, a entrada "Aprender Python" deve retornar 5.
"""

vogais: str = "aeiou"
palavra: str = input("Palavra? ")

total_vogais: list = []

for letra in palavra.lower():
    if letra in vogais:
        total_vogais.append(letra)

quantidade_de_vogais: int = len(total_vogais)

print(f'Quantidade de vogais são {quantidade_de_vogais}.')