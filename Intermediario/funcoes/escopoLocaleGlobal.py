salario = 2000 # -> aqui foi definido o valor do salario sem o bonus 

def salario_bonus(bonus, lista): # -> aqui esta abrindo uma função com os valores bonus e lista para que começe as operações
    global salario # -> "global" serve para usar variaveis que está fora do escopo e são globais porem tem que definir "global" antes da variavel quando colocar ela dentro do escopo

    lista_aux = lista.copy() # -> ".copy" serve para copiar o valor sem altera-lo fazendo assim que ele não mude
    lista_aux.append(5) # - -> quando você usa o ".append" ele vai seguir os números que você definir ou seja nesse caso colocou 5 então ele imprimir o número inicial da lista definido la embaixo que foi 1 e tambem vai imprimrir o número 5
    print(f"O calor da lista auxiliar é de {lista_aux}") # -> aqui só vai printar o valor da lista auxiliar que foi criada que retornará [1, 5]

    salario += bonus #-> aqui vai fazer a operação de soma do salário + o bonus
    return salario # -> aqui vai retornar o novo valor do salario ja com o bonus somado para que ele possa ser printado depois com o valor atualizado

lista = [1] # -> aqui vai definir o valor inicial da lista
a = salario_bonus(500, lista) # aqui vai definir o valor do bonus e chamar a lista para que ela possa ser printada depois
print(f"O salario bonus é de {a}") # -> aqui so vai imprimir o valor do salario + o bonus
print(lista) # -> aqui vai imprimir o valor padrão da lista definido logo a cima que vai ser [1]