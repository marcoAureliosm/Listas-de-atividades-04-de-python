conprimo=0
for i in range(1,11):
    num=int(input("Digite o {}ª valor: ".format(i)))

    if num%1==0 and num%num==0:
         print("numero é primo")
         conprimo = conprimo + 1
    else:
        print("Numero não primo")

print("Quantidade de numeros primos ",conprimo)