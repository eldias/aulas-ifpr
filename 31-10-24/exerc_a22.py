"""
    2. Implementar um programa que faça uma charada com o usuário. O programa deve perguntar: "O que é, o que é que está sempre a caminho, mas nunca chega?" A resposta correta é "amanhã". O usuário pode tentar uma única vez.
"""

resposta: str = "amanhã"
palpite: str = input("O que é, o que é que está sempre a caminho, mas nunca chega?\nDigite seu palpite: ")
if palpite == resposta:
    print("Você acertou!!!")
else:
    print(f"Errado! A resposta é {resposta}")