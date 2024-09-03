""" Exemplo em portguês do que eu quero que ele faça

repita N vezes:
    a += 1
    print(a) 

Dessa forma ele vai repetir N vezes essa operação de incrementação """

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print () # -> serve para fazer uma quebra de linha, so demosntraçao nao precisa desse "else"
    print("Executa no final do laço")
# usar o "for" só quando sabe a quantidade exata que vai executar aquele código nesse caso ele vai executar so uma vez procurandoa as letras