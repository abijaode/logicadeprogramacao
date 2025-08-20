nome = input("Digite seu nome: ")

tempo = input("Digite o tempo em meses que permaneceu na empresa: ")
tempo = int(tempo)

fgts = input("Digite o valor do seu FGTS: ")
fgts = float(fgts)

if tempo < 12:
    multa = fgts * 0.40 
elif tempo > 12: 
    multa = 0

print("O funcionário", nome, "tem direito a uma multa de", multa, "reais sobre o valor do FGTS.Pois trabalhou", tempo, "meses na empresa.")