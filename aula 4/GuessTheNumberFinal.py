import random

recorde = 0 

novamente = "s"
while novamente == "s":

    numero = random.randint(1, 100)

    nome = input("Digite seu nome: ")
    print("Olá,", nome, "! Vamos jogar um jogo de adivinhação.")

    tentativa = int(input("Advinhe o número inteiro entre 1 e 100: "))
    numerotentativa = 1
    tentativaspassadas = []

    while tentativa != numero:
        
        if tentativa in tentativaspassadas:
            print("Você já tentou esse número. Tente um diferente.")
        else: 
            tentativaspassadas.append(tentativa)
            if tentativa < numero:
                print("Muito baixo! Tente novamente.")
            else: 
                print("Muito alto! Tente novamente.")
        numerotentativa += 1
        tentativa = int(input("Advinhe o número inteiro entre 1 e 100: "))

    print("Parabéns", nome, "! Você adivinhou o número:", numero, "em", numerotentativa, "tentativas.")

    if recorde == 0 or numerotentativa < recorde:
        recorde = numerotentativa
   

    print("Seu recorde é de", recorde, "tentativas.")
    print("Você tentou os números:", tentativaspassadas)
    novamente = input("Gostaria de jogar novamente? (s/n): ")

print("Obrigado por jogar!")

