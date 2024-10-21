# OBS: quando usar a "/" tudo que vier antes é obrigado a estar no lacal correto pois ela é somente por posição então não adianta chamar um nome por exemplo na posição 5 se ela estiver na posição 1 antes da barra ou seja tem que esta na mesma posição se não vai dar errado
# os que tiveres depois da barra não tem problema, basta chamar ele com kwords onde quiser em qualquer posição que ele vai dar certo 
# Exemplo do que são kwords -> "marca =", "ano =", "placa =" 
# Exemplo do que não são kwords -> "Palio", "1999", "ABC-1234" 
# Ou seja kwords você coloca primeiro a key depois por exemplo informa a marca nesse caso seria Palio, e sem a key você ja infroma o nome da marca direto pois ela está antes da "/" então só tem que colocar na posição certa

# KEYWORD ONLY
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo = "Palio", ano =1999, placa = "ABC-1234", marca = "Fiat", motor = "1.0", combustivel = "Gasolina") # válido pois so usou kwords antes de cada variavel

#KEYWORD AND POSITIONAL 
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca = "Fiat", motor = "1.0", combustivel = "Gasolina") # válido pois antes da barra não usou kwords nos argumentos e depois da barra usou as kwords

#KEYWORD OR POSITIONAL 
def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel): # -> pode escolher se passa o argumento "marca" por keyword ou direto
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", "Fiat", motor = "1.0", combustivel = "Gasolina") # válido pois nesse caso a "marca" eu posso escolher se quero passar ela com keyword ou sem ja que ela esta depois da barra porem antes do "*"
