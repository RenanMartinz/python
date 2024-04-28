valor_divida = float(input("Digite o valor da dívida: "))

def calcular_parcelas(valor_divida):
    juros = [0, 10, 15, 20, 25]
    parcelas = [1, 3, 6, 9, 12] 
    
    for i in range(len(juros)):
        valor_juros = valor_divida * juros[i] / 100
        total_com_juros = valor_divida + valor_juros
        valor_parcela = total_com_juros / parcelas[i]
        print("Total: R$ {:.2f}, Juros: R$ {:.2f}, Número de parcelas: {}, Valor da parcela: R$ {:.2f}".format(total_com_juros, valor_juros, parcelas[i], valor_parcela))

calcular_parcelas(valor_divida)


