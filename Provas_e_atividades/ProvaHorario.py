tempo = input("Digite o tempo em horas trabalhadas na semana: ")
tempo = int(tempo)

if tempo > 44:
    extra = tempo - 44 
    salario = 44 * 15 + extra * 22.5

else:
    extra = 0
    salario = tempo * 15
print("O seu salário semanal é de", salario, "reais. Sendo ", extra, "horas extras e ", tempo - extra, "horas normais.")


    