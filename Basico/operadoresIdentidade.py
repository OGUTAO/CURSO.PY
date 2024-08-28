curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200 # você pode atribuir mais de um valor para mais de uma variavel respectivamente em python usando a virgula como nesse exemplo

teste1 = curso is nome_curso # "is" significa "é"
teste2 = curso is not nome_curso # "is not" significa "não é"
teste3 = saldo is limite

print(teste1)
print(teste2)
print(teste3)