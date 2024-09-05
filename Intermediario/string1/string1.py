nome = "gUTãO"

print(nome.upper()) # vai deixar em maiusculo
print(nome.lower()) # vai deixar em minusculo
print(nome.title()) # vai deixar em forma de titulo (primeira letra maiuscula)

texto = "  Olá Mundo     "

print(texto + ".")
print("." + texto.strip() + ".") # vai tirar os espaços do texto
print("." + texto.lstrip() + ".") # vai tirar os espaços da esquerda do texto
print("." + texto.rstrip() + ".") # vai tirar os espaços da direita do texto
#obs: os pontos antes e depois só foram colocados para demonstrar melhor no terminal como funciona

menu = "Python"

print("####" + menu + "####") # vai adicionar obviamente os hastags dos lados 
print(menu.center(14)) # faz a mesma coisa so que sem os hastags e vai centralizar a palavra (serve para isso)
print(menu.center(14, "#")) # vai fazer o mesmo do primeiro exemplo alem de centralizar vai adicionar os hastags e se escreve assim para facilitar a indexação
print("P-y-t-h-o-n") # aqui so escrevi o jeito que quero que print a string
print("-".join(menu)) # já nesse caso ele faz a mesma coisa do de cima porem vai adicionar o traço automatico antes de cada letra

