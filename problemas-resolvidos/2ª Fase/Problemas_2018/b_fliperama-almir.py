cache_max = {}
cache_min = {}

fliperama = []

qtdLinhas = int(input())
for _ in range(qtdLinhas):
    linha = [int(_) for _ in input().split()]
    fliperama.append(linha)

def somaMinima(i, j):
    qtdColunas = qtdLinhas - i
    if i >= qtdLinhas or j >= qtdColunas:
        return 0
    if (i, j) not in cache_min:
        cache_min[(i, j)] = fliperama[i][j] + min(somaMinima(i+1, j), somaMinima(i, j+1))
    return cache_min[(i, j)]

def somaMaxima(i, j):
    qtdColunas = qtdLinhas - i
    if i >= qtdLinhas or j >= qtdColunas:
        return 0
    if (i, j) not in cache_max:
        cache_max[(i, j)] = fliperama[i][j] + max(somaMaxima(i+1, j), somaMaxima(i, j+1))
    return cache_max[(i, j)]

print('maximo:', somaMaxima(0, 0))
print('minimo:', somaMinima(0, 0))
