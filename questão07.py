n=0
soma=0
idade=int(input("Digite a idade"))
while idade >=1:
    idade = int(input("Digite a idade"))
    soma=soma+idade
    n=n+1
    if idade==0:
        break
media=soma/n
print("A media é",media)