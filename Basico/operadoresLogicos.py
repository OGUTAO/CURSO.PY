saldo = 1000
saque = 250
limite = 200
conta_especial = True

conta1 = saldo >= saque and saque <= limite # usando "and" (significa "e") nesse caso vai retornar falso pq para a expressão ser verdadeira as duas atribuições tem que ser verdadeiras se não retornará falso
conta2 = saldo >= saque or saque > limite # como citado no exemplo a cima aqui retornará verdadeiro pois os dois são verdadeiros
print(conta1)
print(conta2) 

conta3 = saldo >= saque or saque <= limite # usando "or" nesse caso vai retornar verdadeiro pq usando o "or" (significa "ou") basta uma ser verdadeira ou seja se tiver algum verdadeiro precisa existir pelo menos uma verdadeira, porem para ser falso é enscessario que os dois nesse caso sejam falso
conta4 = saldo == saque or saque == limite # como citado no exemplo a cima aqui retornará falso pois os dois são falso
print(conta3)
print(conta4)

contaParenteses = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # aqui ele faz dois tipos de operações com duas opções ou seja ou a primeira operação ta certa ou a segunda caso contrario retorne falso
print(contaParenteses)

# OPERADORES DE NEGAÇÃO "NOT" -> isso significa que não é vdd ou seja ele vai ser invertido se ele retornar falso usando o not vai ser true
contatos_emergencia = []

conta5 = not 1000 > 1500 # 1000 não pe maior que 1500 então retornaria false mas vai retornar true pois tem o not que significa que vai inverter
conta6 = not contatos_emergencia # a lista está vazia então retornaria false mas vai retornar true pois tem o not que significa que vai inverter
conta7 = not "saque 1500;" # essa string é verdadeira pq tem valor dentro das aspas mas vai retornar false pois tem o not que inverte
conta8 = not "" # essa string é falsa pq não tem valor dentro das aspas mas vai retornar true pois tem o not que inverte
print("1000 > 1500 =", conta5)
print("not contatos_emergencia =", conta6)
print("not saque 1500;= ", conta7)
print("not vazio =", conta8)


