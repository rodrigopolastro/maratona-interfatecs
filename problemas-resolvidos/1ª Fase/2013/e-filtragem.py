# leitura = 21:12 - 21:12 (9)
# 09/04/25
# escrita 21:12 - 21:25 (parado aqui)
# 21:50 - 22:30 ... que problema tenso
# 10/04
# 20:20 - 20:30
# 21:00 - 21:45
from math import floor

def aplicaMascara(posicaoMeio: tuple):
    meioI, meioJ = posicaoMeio
    dif = [MEIO_MASCARA[0]-meioI, MEIO_MASCARA[1]-meioJ]
    soma = 0
    for i in range(linhasImagem):
        for j in range(colunasImagem):
            newI, newJ = i+dif[0], j+dif[1]
            if 0 <= newI < linhasMascara and 0 <= newJ < colunasMascara:
                soma += matrizImagem[i][j] * mascara[newI][newJ]
    return soma

while True:
    colunasImagem, linhasImagem, linhasMascara, colunasMascara = [int(_) for _ in input().split()]
    if colunasImagem == 0:
        break
    
    matrizImagem = list()
    for _ in range(linhasImagem):
        matrizImagem.append([int(_) for _ in input().split()])        
        
    mascara = list()
    for _ in range(linhasMascara):
        mascara.append([float(_) for _ in input().split()])        

    MEIO_MASCARA = (int((linhasMascara+1)/2)-1, int((colunasMascara+1)/2)-1)

    for i in range(linhasImagem):
        for j in range(colunasImagem):
            soma = aplicaMascara((i, j))
            finalLinha = "\n" if j == colunasImagem-1 else ' '
            print(floor(soma), end=finalLinha)     


