def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}") # -> salva o carro no banco de dados


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # -> não é recomendado passar dessa forma pois se alterar a ordem sem querer ele vai baguncar tudo pois os nomes não estão ligados diretamente a cada componente respectivo
salvar_carro(marca = "Fiat", modelo = "Palio", ano = 1999, placa = "ABC-1234") # -> dessa forma é mais recomendado pois assim os nomes estão respectivamente ligados a cada um certinho para não ter erro
# caso mude sem querer a ordem porem se mudar o nome chamado na função vai dar erro então tem que ter cuidado 
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # -> "**" aqui ele vai passar um dicionario para a função e dessa forma fazer igual o jeito de cima porem um pouco mais complexo e com menos erros 
