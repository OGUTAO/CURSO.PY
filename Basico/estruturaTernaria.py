saldo = 2000
saque = 2500

#OBS: é a mesma coisa do jeito normal so que simplificando tudo em uma linha só
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!") # -> print igual o normal porem o " f"{} " vai puxar a variavel que vc quiser para dentro do print
