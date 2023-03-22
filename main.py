def calcular_valor_total(ano_uso, valor_maco, quant_macos_dia):
    dias_uso = ano_uso * 12 * 30
    valor_dia_maco = valor_maco * quant_macos_dia

    return dias_uso * valor_dia_maco

def retornar_mensagem(valor):

    if(valor < 20000):
        return "Com o valor de R$ {0:.2f}, você poderia ter dado entrada em um carro.".format(valor)
    elif(valor >= 20000 and valor <= 50000):
        return "Com o valor de R$ {0:.2f}, você poderia ter comprado um carro popular usado.".format(valor)
    else:
        return "Com o valor de R$ {0:.2f}, você poderia ter comprado um carro zero.".format(valor)

if __name__ == '__main__':
    anos_uso = float(input("Tempo como fumante (em anos).....:"))
    valor_maco = int(input("Valor do maço....................:"))
    quant_macos_dia = float(input("Quantidade de maços por dia............:"))

    valor_total = calcular_valor_total(anos_uso, valor_maco, quant_macos_dia)

    mensagem = retornar_mensagem(valor_total)

    print(mensagem)