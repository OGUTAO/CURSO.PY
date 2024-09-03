opcao = -1 # -> colocou um número qualquer so para entender que a variavel é um inteiro mas esse valor vai ser substituido logo após o valor colocado pelo usuario no input

while opcao != 0: 
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2: # "elif" pode siginificar senão-se ou seja para continuar o bloco rodando e não termine e pare de rodar o bloco use "elif" pois se usar "else" ele obrigatóriamente tem que parar o bloco depois do else como demosntrado na linha abaixo que caso digite "0" vai terminar o codigo e printar a mensagem
        print("Exibindo o extrato...")
else: 
    print("Obrigado por usar nosso sistema bancário, até logo")
# A estrutura "while" vai rodar o código até o final ou infinitamente que é esse caso, ou seja nesse caso tá siginificando que equanto (while) for diferente de 0 não saia da operação então vai ficar executando infinitamente até decidir sair