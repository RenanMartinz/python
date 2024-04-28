def calcular_ir(tipo_investimento, valor_resgate, dias_investidos):
    if tipo_investimento == 1:  # CDB
        if dias_investidos <= 180:
            return valor_resgate * 0.225  # alíquota de 22.5%
        elif 181 <= dias_investidos <= 360:
            return valor_resgate * 0.20  # alíquota de 20%
        elif 361 <= dias_investidos <= 720:
            return valor_resgate * 0.175  # alíquota de 17.5%
        else:
            return valor_resgate * 0.15  # alíquota de 15%
    elif tipo_investimento == 2 or tipo_investimento == 3:  # LCI ou LCA
        return 0  
    else:
        return "Tipo de investimento inválido"


def main():
    tipo_investimento = int(input("Digite o tipo de investimento (1 para CDB, 2 para LCI, 3 para LCA): "))
    if tipo_investimento not in [1, 2, 3]:
        print("Tipo de investimento inválido.")
        return

    valor_resgate = float(input("Digite o valor a ser resgatado: "))
    dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))

    imposto_de_renda = calcular_ir(tipo_investimento, valor_resgate, dias_investidos)

    if isinstance(imposto_de_renda, str):
        print(imposto_de_renda)
    else:
        print("Imposto de renda a ser pago: R$", round(imposto_de_renda, 2))


if __name__ == "__main__":
    main()
