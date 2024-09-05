nome = "Gutão"
idade = 20
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": nome, "idade": idade, "profissao": profissao, "linguagem": linguagem}

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
# mesma coisa do modo old "%" não é aconselhavel pois é um método antigo que tem que indicar a ordem que ele vai printar as variaveis 


print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
# mesma coisa da de cima porem tem mais capacidade de costumização pois eu posso colocar na posição que eu quiser mudando elas dentro de cada chaves o número da ordem que eu quero que ele imprima de acordo o posicionamento com minhas variaveis declaradas no fim do código, também é pouco viavel usar assim


print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
# continuando a ideia ele vai fazer o mesmo porem aqui ja vou indicar oque eu quero que ele retorne e no final do codigo vou indicar oque cada variavel vai indicar devido ao nome qu eu coloquei no código, também não é muito viavel usar assim


print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))
# vai fazer o mesmo de cima porem de uma forma mais simples e compacta pois eles vao buscar as variaveis que eu coloquei ja dentro do dicionario "pessoa" já é um pouco mais indicado usar assim 
