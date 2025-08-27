notasmoedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

receber = float(input("Insira o valor recebido: "))
preco = float(input("Insira o preço: "))
troco = receber - preco
print ("Seu troco é de", troco, "reais.")

while troco != 0:
    
    if troco >= 200:
       print("1 nota de 200 reais.")
       troco = troco - 200
    elif troco >= 100:
        print("1 nota de 100 reais.")
        troco = troco - 100
    elif troco >= 50:
        print("1 nota de 50 reais.")
        troco = troco - 50
    elif troco >= 20:
        print("1 nota de 20 reais.")
        troco = troco - 20
    elif troco >= 10:
        print("1 nota de 10 reais.")
        troco = troco - 10
    elif troco >= 5:
        print("1 nota de 5 reais.")
        troco = troco - 5
    elif troco >= 2:
        print("1 nota de 2 reais.")
        troco = troco - 2
    elif troco >= 1:
        print("1 moeda de 1 real.")
        troco = troco - 1
    elif troco >= 0.50:
        print("1 moeda de 0.50 centavos.")
        troco = troco - 0.50
    elif troco >= 0.25:
        print("1 moeda de 0.25 centavos.")
        troco = troco - 0.25
    elif troco >= 0.10:
        print("1 moeda de 0.10 centavos.")
        troco = troco - 0.10
    elif troco >= 0.05:
        print("1 moeda de 5 centavos.")
        troco = troco - 0.5
    elif troco >= 0.01:
        print("1 moeda de 1 centavo.")
        troco = troco - 0.1