#inicio 7:55PM / término:  9:30PM
while True:
    meses = int(input())
    if meses == 0:
        break
    lucro = 0
    variacoes = []
    for mes in range(1,meses+1):
        lucro += int(input())
        variacoes.append((lucro,mes))
    
    while True:
        aRemover = []
        for index in range(1,len(variacoes)+1):
            if variacoes[index-1][0] < 0:
                aRemover.append(index-1)
                
        if aRemover == []:
            break
        else:
            for i in aRemover[::-1]:
                variacoes.pop(i) 

    
    def somarMax(lista : list[tuple]):
        somaReturn = 0
        for iten in lista:
            somaReturn+=iten[0]
        return somaReturn

    bestMax = []
    maximo = 0
    seq = []

    for numeros in variacoes:
        if seq != []:
            if numeros[0] > seq[-1][0]:
                seq.append(numeros)
            else:
                if somarMax(seq) > somarMax(bestMax):
                    bestMax = seq.copy()
                    seq = [numeros]
                else:
                    seq = [numeros]
                  
        else:
            seq.append(numeros)

    if somarMax(bestMax) > somarMax(seq):
        print(bestMax[0][1],bestMax[-1][1])
    else:
        print(seq[0][1],seq[-1][1])
