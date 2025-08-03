#rodrigo
from functools import lru_cache

fliperama = list()

qtdLinhas = int(input())
for _ in range(qtdLinhas):
    linha = [int(_) for _ in input().split()]
    fliperama.append(linha)
 
qtdElementos = int((1 + qtdLinhas) * qtdLinhas / 2)
 
@lru_cache(qtdElementos)
def somaMinima(posicao):
    i, j = posicao
    qtdColunas = qtdLinhas - i
    if i >= qtdLinhas or j >= qtdColunas:
        return 0
    valorPosicao = fliperama[i][j]
    
    infEsquerda = (i+1, j)
    infDireita = (i, j+1)
    
    return valorPosicao + min(somaMinima(infEsquerda), somaMinima(infDireita))

@lru_cache(qtdElementos)
def somaMaxima(posicao):
    i, j = posicao
    qtdColunas = qtdLinhas - i
    if i >= qtdLinhas or j >= qtdColunas:
        return 0
    valorPosicao = fliperama[i][j]
    
    infEsquerda = (i+1, j)
    infDireita = (i, j+1)
    
    return valorPosicao + max(somaMaxima(infEsquerda), somaMaxima(infDireita))

print('maximo:', somaMaxima((0, 0)))
print('minimo:', somaMinima((0, 0)))