respostas = []


def definirPosicao(forcaAtual, tipoBarra):
    if forcaAtual == 'E': #está indo para esquerda
        if tipoBarra == 'D':
            return 'I'
        if tipoBarra == 'I':
            return 'S'
    if forcaAtual == 'S' : # está indo para cima (superior)
        if tipoBarra == 'D':
            return 'D'
        if tipoBarra == 'I':
            return 'E'
    if forcaAtual == 'I':
        if tipoBarra == 'D':
            return 'E'
        if tipoBarra == 'I':
            return 'D'
    if forcaAtual == 'D':
        if tipoBarra == 'D':
            return 'S'
        if tipoBarra == 'I':
            return 'I'
        
try:
    while True:
        qtdeColunas = int(input()) # e sempre uma matriz quadrada
        qtdeBarras = int(input())
        posicoesBarras = dict()
        for _ in range(qtdeBarras):
            entrada = tuple(input().split(' '))
            posicoesBarras[(int(entrada[0])-1,int(entrada[1])-1)] = entrada[2]
        comeco = input().split()
        direcaoComeco = comeco[1]
        direcao = ''
        if direcaoComeco == 'I':
            posicaoBola = (qtdeColunas - 1,int(comeco[0]) -1)
            direcao = 'S'
        if direcaoComeco == 'S':
            posicaoBola = (0,int(comeco[0])-1)
            direcao = 'I'
        if direcaoComeco == 'D':
            posicaoBola = (int(comeco[0]) -1 ,qtdeColunas - 1)
            direcao = 'E'
        if direcaoComeco == 'E':
            posicaoBola = (int(comeco[0]) -1,0)
            direcao = 'D'
        # print(posicoesBarras)
        while True:
            # print(direcao)
            # print(posicaoBola)
            if posicaoBola[0] < 0 or posicaoBola[0] >= qtdeColunas or posicaoBola[1] < 0 or posicaoBola[1] >= qtdeColunas:
                if posicaoBola[0] < 0 or posicaoBola[0] >= qtdeColunas:
                    # print(f'{posicaoBola[1]+1} {direcao}')
                    respostas.append(f'{posicaoBola[1]+1} {direcao}')
                    break
                if posicaoBola[1] < 0 or posicaoBola[1] >= qtdeColunas:
                    # print(f'{posicaoBola[0]+1} {direcao}')
                    respostas.append(f'{posicaoBola[0]+1} {direcao}')
                    break
            if (posicaoBola[0],posicaoBola[1]) in posicoesBarras.keys():
                direcao = definirPosicao(direcao,posicoesBarras[(posicaoBola[0],posicaoBola[1])])
            if direcao == 'I':
                posicaoBola = (posicaoBola[0]+1,posicaoBola[1])
            if direcao == 'S':
                posicaoBola = (posicaoBola[0]-1,posicaoBola[1])
            if direcao == 'D':
                posicaoBola = (posicaoBola[0],posicaoBola[1]+1)
            if direcao == 'E':
                posicaoBola = (posicaoBola[0],posicaoBola[1]-1)  
                
                  
except EOFError:
    for r in respostas:
        print(r)