#exemplo 1: transformando valores int para float
preco = 10 # vai imprimir um valor inteiro
print(preco)
preco = float(preco) # vai transformar o valor inteiro em float
print(preco)
preco = 10 / 2 # qualquer divisão em python trasnforma o valor inteiro em float
print(preco)

#exemplo 2: transformando valores float em int
preco2 = 10.30 # vai imprimir um valor float
print(preco2)
preco2 = int(preco2) # vai trasnformar o valor float para inteiro se tiver valor quebrado ele arrendonda  
print(preco2)

#exemplo 3: divisão de valores inteiros
preco3 = 10 # vai imprimir um valor inteiro
print(preco3)
print(preco3 / 2) # qualquer divisão em python trasnforma o valor inteiro em float
print(preco3 // 2) # se usar dois // na divisão ele retorna o valor da divisão so que inteiro em vez de float

#exemplo 4: transformando valores para strings
preco4 = 10.50
idade = 28
print(str(preco4)) # vai transformar o valor float em str
print(str(idade)) # vai transformar o valor int em str
texto = f"idade {idade} preco {preco4}" # vai imprimir cada valor em forma de str pois elas foram alteradas, tem que transformar em string pq não da pra concatenar no print str junto com valores sejam eles float ou int
print(texto)

#exemplo 5: transformando strings para valores para fazer operações (não da par fazer operações matemáticas com str)
preco5 = "10.50"
idade2 = "28"
print(float(preco5)) # mesma coisa de transformar int para float porem se vc fizer a transformação já dentro do print ele não arredonda o valor
print(int(idade2)) # vai fazer o mesmo so que transformar str para int
