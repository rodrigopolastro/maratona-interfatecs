entrada = [int(x) for x in input().split()]
if len(entrada) != 10:
    print("ERRO")
else:
    qtdImpar = 0
    qtdPar = 0
    for i in entrada:
        if i%2 == 0:
            qtdPar+=1
        else:
            qtdImpar +=1
    print(qtdPar,qtdImpar)


    