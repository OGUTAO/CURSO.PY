#OBS: EXEMPLOS UM POR UM NOS ARQUIVOS DE VARIAVEIS (OLD%, FORMAT{}, FSTRING)

nome = "Gutão"
idade = 20
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": nome, "idade": idade}

print("Nome: %s idade: %d" % (nome, idade))
# não recomendado usar assim

print("Nome: {} idade: {}".format(nome, idade))
# tambem não recomendado

print("Nome: {nome} idade: {idade}".format(nome=nome, idade=idade))
# tambem não recomendado pois tem que nomear cada um da mais trabalho e fica um código bem maior

print("Nome: {0} idade: {1} Nome2: {0} Nome3: {0}".format(nome, idade))
# tambem não recomendado porém tem suas vantagem caso precise repetir alguma variavel mais de uma vez como exemplo nesse caso 

print("Nome: {nome} idade: {idade}".format(**dados))
# neste caso já começamos a entrar nos mais recomendados pois nesse a gente pode simplesmente criar um dicionário e colocar todas as informações já lá dentro e retornar tudo de uma vez chamando ela nesse caso o "dados" então facilita muito o código 

print(f"Nome: {nome} idade: {idade}")
# esse é o jeito mais recomendado pois assim basta colocar o "f" na frente e pronto ele já puxa todas as variaveis disponiveis para o print basta chamar a variavel dentro das chavez e dessa forma otimiza muito mais o código deixando assim bem mais simples

print(f"Nome: {nome} idade: {idade} saldo: {saldo}")
# aqui ele só vai imprimir para servir de exemplo pro próximo código

print(f"Nome: {nome} idade: {idade} saldo: {saldo: 10.2f}")
# nesse caso ele vai fazer o mesmo do exemplo de cima porem o saldo vai pular primeiro 10 casas para ser impresso e dpois vai imprimir somente duas casas após o ponto flutuante pois foi isso que eu exigi no código

print(f"Nome: {nome} idade: {idade} saldo: {saldo: .2f}")
# mesma coisa do exemplo de cima porem ele não vai pular nenhuma casa para começar a imprimri o número de ponto flutuante que eu pedi que ele imprimisse
