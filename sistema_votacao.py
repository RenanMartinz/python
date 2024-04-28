menu = """
Bem-vindo ao nosso sistema de votação.
Por favor, digite o número do melhor dia para realização da Live:

a. Segunda-feira 
b. Terça-feira
c. Quarta-feira
d. Quinta-feira
e. Sexta-feira

=>"""

while True:
    opcao = input(menu)

    if opcao in ["a", "b", "c", "d", "e"]:
        if opcao == "a":
            dia = "Segunda-feira"
        elif opcao == "b":
            dia = "Terça-feira"
        elif opcao == "c":
            dia = "Quarta-feira"
        elif opcao == "d":
            dia = "Quinta-feira"
        elif opcao == "e":
            dia = "Sexta-feira"
            
        print("Você votou para realizar a live na {}. Obrigado por votar.".format(dia))
        break
    else:
        print("Valor inválido.")
