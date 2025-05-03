linhas = []
try:
    while True:
        l = input()
        linhas += [i for i in l]
except EOFError:
    x, y = 0, 0

    for i in range(len(linhas)):
        linha = linhas[i]
        anterior = linha[0]
        for j in range(1, len(linhas)):
            print("linha:",linha)
            c = linha[j]
            if anterior != c and j == 1:
                if j+1 < len(linha) and linha[j+1] == anterior:
                    x, y = i, j
                else:
                    x, y = i, j+1
            elif anterior != c:
                x,y = i,j
            anterior = c


    print(f"LINHA {x} COLUNA {y}")

