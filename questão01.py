cont=0
cont2=0
for i in range(1,11):
    idade=int(input("Digite qual a sua idade)"))
    if idade>18:
        cont=cont+1
    else:
        cont2=cont2+1
print("quantidade de alunos maiores de idade",cont)
print("quantidade de alunos menos de idade",cont2)