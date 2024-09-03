# usar o "for" só quando sabe a quantidade exata que vai executar aquele código nesse caso ele diz da onde até a onde
for numero in range(0, 11): # -> de "0" até "10" quando tem só dois numeros significa isso
    print(numero, end=" ") # -> " end=" " " serve para colocar os numeros retornados na mesma linha horizontal caso contraio iria imprimir verticalmente
print() # outra forma de quebrar a linha além do "\n" póis em alguns casos como esse se usar o \n vai quebrar a formatção do código impresso e vai ficar bagunçado sem ser na mesma linha horizontal

for numero in range(0, 51, 5): # -> nesse caso tem 3 números ou seja vai do primeiro número "0" até o ultimo "51", pulando de 5 em 5 "5" no final dos três números
    print(numero, end=" ")

# obs: o primeiro número sempre vai ser impresso já o segundo só vai ser impresso um número atrás dele ou seja no primeiro exemplo só vai imprimir de 0 até 11 e no segundo de 0 até 50
