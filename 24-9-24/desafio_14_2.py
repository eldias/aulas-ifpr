# 2. Implementar um programa que funcione como um jogo de adivinhação de números inteiros. O jogo deve gerar um número aleatório entre 0 e 10, e o usuário terá três tentativas para adivinhar o número. Ao final, o programa deve informar se o usuário ganhou ou perdeu.
import random

tentativas = 3
numero_certo = int(random.randrange(0, 11))

for i in range(tentativas):
    palpite = int(input("Dê o seu palpite: "))
    if palpite == numero_certo:
        print("Parabéns!")
    else:    
        tentativas -= 1
        print("Tente novamente!")

print("Game over")

