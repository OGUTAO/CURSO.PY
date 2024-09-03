while True:
    numero = int(input("Informe um número: "))

    if numero ==  10: # -> aqui mesmo o 10 sendo par ele vai para o código pois ele está indicando que quando o usuario colocar o número "10" o código tem que parar, é nescessario que coloque alguma saida assim para o código não ficar rodando infinitamente
        break 

    if numero % 2 == 0: # -> aqui ele vai verificar se o número é par ou seja "% 2" vai fazer a conta de modulo se sobrar resto na divisão ele é impar se não sobrar ou seja se for igual a "0" ele é par
        continue 
    
    print(numero)