MAIOR_IDADE = 18
IDADE_ESPECIAL = 12


#1
idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade <= MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


#2
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Ainda não pode tirar a CNH.")
# Os dois jeitos a cima de fazer são iguais


#3
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teoricas mas não as teoricas")
else:
    print("Ainda não pode tirar a CNH.")

# Use o "elif" como um MAS ou seja (faça isso) "if", (se não faça isso e termine o bloco) "else", (mas) "ilif" for isso, faça isso -> (siga esse outro caminho).  