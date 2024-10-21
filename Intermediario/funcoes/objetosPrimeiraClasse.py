def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a * 2 + b * 3


def exibir_resultado(a, b, operacao): # -> aqui ele vai puxar as variaveis a e b e difinir um nome para o calculo que ele vai fazer nesse caso foi "operacao" que dependendo da linha vai fazer a "soma", a "subtracao", e o "test"
    # delas onde ela na linha de baixo vai receber esses valores ja prontos depois deles ja passarem pela operação e entregar o resultado podendo ser printado depois
    resultado = operacao(a, b)
    print(f"O resultado da operação = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)
exibir_resultado(10, 10, test)

# Outra forma similar seria assim:

# op = somar
# op2 = subtrair
# op3 = test
# print(op(10, 10))
# print(op2(10, 10))
# print(op3(10, 10))