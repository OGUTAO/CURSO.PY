# Método sem pedir o valor para o cliente (eu já defini os valores lá embaixo quando chamei a função)
def sacando(valorsaque):
    conta = 500

    if conta >= valorsaque:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa")

print("Valor não sacado; valor mais alto do que você possui, obrigado por ser nosso cliente, tenha um bom dia!")


def deposito(valorsaque):
    conta = 500
    conta += valorsaque

valorsaque = sacando(100) # Dependendo do valor colocado aqui ele não vai sacar pois é maior que o valor da conta