notasmoedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

receber = float(input("Insira o valor recebido: "))
preco = float(input("Insira o preço: "))
troco = receber - preco
print ("Seu troco é de", troco, "reais.")

for item in notasmoedas:
    quantidadeitens = 0
    while item <= troco:
        quantidadeitens += 1
        troco -= item
    if quantidadeitens > 0:
        print(f"{quantidadeitens} notas de {item} reais.")


    