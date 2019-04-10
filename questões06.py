print("=============ELEIÇÕES===========")
print("[1]ARLINDO\n[2]JOSÉ\n[3]LULA\n[4]DILMA\n[5]NULO \n[6]BRANCOS \n[0]TERMINAR VOTAÇÃO ")
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0
while True:
    candidato = int(input('Digite o Numero do seu candidato: '))
    while candidato <0 and candidato >6:
        print("valor invalido")
        candidato = int(input('Digite o Numero do seu candidato: '))
    if candidato == 1:
        cont1 += 1
    elif candidato == 2:
        cont2 += 1
    elif candidato == 3:
        cont3 += 1
    elif candidato == 4:
        cont4 += 1
    elif candidato == 5:
        cont5 += 1
    elif candidato == 6:
        cont6 += 1
    elif candidato == 0:
        break
print("[{}] Candidato 1\n[{}] Candidato 2\n[{}] Candidato 3\n[{}] Candidato 4\n[{}] Candidato 5\n[{}] Candidato 6".format(cont1,cont2,cont3,cont4,cont5,cont6))


