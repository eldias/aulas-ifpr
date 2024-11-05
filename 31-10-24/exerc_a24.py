"""
    Implementar um programa que inverta uma frase informada pelo usuário. Por exemplo, a entrada "Banana" deve retornar "ananaB".
"""

palavra: str = input("Qual a palavra? ")
palavra_invertida: str = palavra[::-1]
print(palavra_invertida)