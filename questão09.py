for i in range(1,4):
    try:
        altura=float(input("Digite a altura"))
        if altura>maior:
            maior=altura
    except:
        print("Invalido")
    try:
        sexo=str(input("Digite o seu sexo [F]Feminino [M]Masculino"))
        if sexo="F":
        soma=soma+1
    except:
        print("Invalido")
