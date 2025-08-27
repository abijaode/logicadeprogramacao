#algoritmo para calcular o MDC (Máximo Divisor Comum) de dois números inteiros

primeiro_numero = input("Digite o primeiro número inteiro: ")
primeiro_numero = int(primeiro_numero)

segundo_numero = input("Digite o segundo número inteiro: ")
segundo_numero = int(segundo_numero)

while not primeiro_numero == segundo_numero:
    if primeiro_numero > segundo_numero:
        primeiro_numero = primeiro_numero - segundo_numero
    else:
        segundo_numero = segundo_numero - primeiro_numero

print ("O MDC é:", primeiro_numero)