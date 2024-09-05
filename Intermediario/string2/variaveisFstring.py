nome = "Gutão"
idade = 20
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")
# esse é o jeito ideal de usar pois usando o " f"blabla" " facilia muito pois dentro das chaves você so tem que colocar 
# as variaveis que você quer que retorne dentro de cada um deles caso ja tenham sido declarados anteriormente 


# Formatar strings com f-string
PI = 3.14159
print(f"Valor de PI: {PI}") # -> vai retornar o valor de PI já declado a cima porem vai ser printado o número todo 

print(f"Valor de PI:{PI: .2f}") # -> ": .2f" aqui ele está formatando indicando antes do ponto quantas casas ele quer que pule antes de retornar o valor e nesse caso não quer nenhuma porem 
# depois do ponto vai indicar quantas casas apos o ponto do seu número flutuante você quer que ele retorne nesse caso será so duas casas
print(f"Valor de PI:{PI: .4f}") # -> ": .4f" vai fazer o mesmo de cima porém vai imprimir agora 4 casas apos o ponto do seu numero de ponto flutuante em vez de duas casas como no exemplo a cima

print(f"Valor de PI:{PI:10.2f}") # -> ":10.2f" vai fazer o mesmo do primeiro exemplo porem vai pular a quantidade de casas selecionadas antes do ponto em "10.2f" nesse caso vai pular 10 casas antes de imprimir 
# o valor de ponto flutuante e depois vai impriri somente 2 casas apos o seu ponto fluante igaul no primeiro exemplo
print(f"Valor de PI:{PI:10.4f}") # -> ":10.4f"o mesmo de cima porem dessa vez igual no segundo exemplo vai imprimir 4 casas após o ponto flutuante em vez de duas casas


