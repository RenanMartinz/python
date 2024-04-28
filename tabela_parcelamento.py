def calcular_preco_final(valor_carro, parcelas):
    desconto_avista = 0.2
    acrescimo_parcelado = [0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24, 0.27, 0.30]

    preco_avista = valor_carro * (1 - desconto_avista)

    indice_acrescimo = parcelas // 6 - 1
    acrescimo = acrescimo_parcelado[indice_acrescimo]

    preco_parcelado = valor_carro * (1 + acrescimo)

    return preco_avista, preco_parcelado


def gerar_tabela(valor_carro):
    parcelas_disponiveis = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

    preco_avista = calcular_preco_final(valor_carro, 1)[0]
    print("O preço final à vista é: R${:.2f}".format(preco_avista))

    for parcela in parcelas_disponiveis:
        preco_parcelado = calcular_preco_final(valor_carro, parcela)[1]
        valor_parcela = preco_parcelado / parcela
        print("O preço final parcelado em {} x é R${:.2f} com parcelas de R${:.2f}".format(parcela, preco_parcelado, valor_parcela))

valor_carro = float(input("Digite o valor do carro: R$"))
gerar_tabela(valor_carro)
