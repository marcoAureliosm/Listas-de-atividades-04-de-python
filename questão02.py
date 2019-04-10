
cont=0
cont2=0
cont3=0
cont4=0
cont5=0
for i in range(1,16):
    idade=int(input("Digite a sua idade"))
    if idade >=1 and idade <=15:
        cont=cont+1
    elif idade >=16 and idade<=30:
        cont2=cont2+1
    elif idade >=31 and idade<=45:
        cont3=cont3+1

    elif idade >=46 and idade<=60:
        cont4=cont4+1

    elif idade >=61:
        cont5=cont5+1
total=(cont+cont2+cont3+cont4+cont5+cont5)
porprimeira = (cont*100)/total
porsegunda = (cont2*100)/total
porterceira = (cont3*100)/total
porquarta = (cont4*100)/total
porquinta = (cont5*100)/total

print("FAIXA I",cont)
print("Faixa II",cont2)
print("FAIXA III",cont3)
print("FAIXA IV",cont4)
print("FAIXA V",cont5)
print("Porcentagem faixa 1 %d"%porprimeira)
print("Porcentagem Faixa2 %d"%porsegunda)
print("Porcentagem Faixa3 %d"%porterceira)
print("Porcentagem Faixa4 %d"%porquarta)
print("Porcentagem Faixa5 %d"%porquinta)

