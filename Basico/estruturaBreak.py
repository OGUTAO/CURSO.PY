# exemplo 1:
while True:
    numero = int(input("Informe um número: "))

    if numero ==  10:
        break # -> aqui está fazendo o seguinte, qualquer número que coloque vai rodar infinito mas se for 10 vai cortar o laço e parar (break) o código, parar de rodar

    print(numero)



# exemplo 2:
for numero in range(100):

    if numero == 12:
        break # -> aqui ele vai parar o código (laço) quando chegar no 12 ou seja não vai exibir até o 99 que era oque era para ser feito caso não tivesse um (break)

    print(numero, end=" ")



# exemplo 3:
for numero in range(100):

    if numero == 12:
        continue # -> aqui ele vai exibir todos os números do laço ate o 99 pois foi oque eu solicitei, menos (continue), o número "12"

    print(numero, end=" ")


#obs: comente cada exemplo para que rode um por um para ver como funciona cada exemplo se tentar rodar todos descomentados vai rodar só o primeiro