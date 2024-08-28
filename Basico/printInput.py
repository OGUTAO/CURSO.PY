nome = input("informe seu nome: ")
idade = input("informe a sua idade: ")
print(nome, idade)
print(nome, idade, end="...\n") # se usar o end ou sep tem que usar o "\n" para quebrar a linha, porems e ja usou em uma linha não precisa usar na outra de baixo
print(nome, idade, sep="#") # não precisa usar a quebra de linha pois ela já foi definida em cima então todos em baixo vão estar com quebra de linha 
print(nome, idade, sep="#", end="...\n") # usando o "sep" e "end" juntos
