print("Digite o seu salário: ")
salario = float(input())

print("Digite a quantidade de dias de atraso: ")
atraso = int(input())

if atraso <= 5:
    print("Não há multa.")
else:
    dias_com_multa = atraso - 5  
    multa = salario * 0.02 * dias_com_multa
    print(f"A multa é de: R$ {multa:.2f}")
