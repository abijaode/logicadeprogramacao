numero = 5
#import random

tentativa = input("Advinhe o número entre 1 e 10: ")
tentativa = int(tentativa)

while tentativa != numero:
    if tentativa < numero:
        print("Muito baixo! Tente novamente.")
    elif tentativa > numero:
        print("Muito alto! Tente novamente.")

    tentativa = input("Advinhe o número entre 1 e 10: ")
    tentativa = int(tentativa)

print("Parabéns! Você adivinhou o número:", numero)

