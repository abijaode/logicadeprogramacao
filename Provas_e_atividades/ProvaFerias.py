print("Digite a quantidade de meses trabalhados: ")
meses = int(input())
print("Digite o valor do seu salario: ")
salario = float(input())
salario = salario/12
ferias = (salario * meses)
print("Seu salario será de R$", ferias, "reais")
