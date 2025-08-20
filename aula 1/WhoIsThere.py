# O codigo vai identificar o nome da pessoa na variavel, depois vai dizer olá e inserir o nome registrado na variavel

pergunta = "qual o seu nome?"
resposta = input(pergunta)
if resposta == "":
    resposta = "pessoa"
saida = f"ola,{resposta} =)"
print(saida)