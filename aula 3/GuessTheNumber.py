#algoritmo para adivinhar um número aleatorio entre 1 e 10

import random
numero = random.randint(1, 10) 

nome = input("Digite seu nome: ")
print("Olá,", nome, "! Vamos jogar um jogo de adivinhação.")


tentativa = input("Advinhe o número inteiro entre 1 e 10: ")
tentativa = int(tentativa)

numerotentativa = 1

while tentativa != numero:
    if tentativa < numero:
        print("Muito baixo! Tente novamente.")
    elif tentativa > numero:
        print("Muito alto! Tente novamente.")
    numerotentativa = numerotentativa + 1
    tentativa = input("Advinhe o número inteiro entre 1 e 10: ")
    tentativa = int(tentativa)

print("Parabéns", nome, "! Você adivinhou o número:", numero, "em", numerotentativa, "tentativas.")