nome = "Guilherme Arthur de Carvalho"

print("Exemplo 1:")
nome1 = nome[0] # "nome[0]" -> ele vai retornar so o primeiro elemento da string nome
print(nome1) 

print("Exemplo 2:")
nome2 = nome[:9] # "nome[:9]" -> ele vai retornar do primeiro elemento da string nome até o nono elemento
print(nome2)

print("Exemplo 3:")
nome3 = nome[10:] # "nome[10:]" -> ele vai retornar apartir do décimo elemento da string nome até o final
print(nome3)

print("Exemplo 4:")
nome4 = nome[10:16] # "nome[10:16]" -> ele vai retornar apartir do décimo elemento da string nome até o décimo sexto elemento
print(nome4)

print("Exemplo 5:")
nome5 = nome[10:16:2] # "nome[10:16:2]" -> ele vai retornar apartir do décimo elemento da string nome até o décimo sexto elemento porém pulando de 2 em 2 elementos
print(nome5)

print("Exemplo 6:")
nome6 = nome[:] # "nome[:]" -> ele vai retornar a string nome inteira
print(nome6)

print("Exemplo 7:")
nome7 = nome[:: -1] # "nome[:: -1]" -> ele vai retornar a string nome inteira porem ele vai espelhar a string ou seja inverter ela
print(nome7)
