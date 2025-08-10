qtd_linhas = int(input())
fliperama = [list(map(int, input().split())) for _ in range(qtd_linhas)]

def somaMinima():
    cache = {}
    stack = [(0, 0, 0)]

    while stack:
        i, j, st = stack.pop()
        if (i, j) in cache:
            continue

        if st == 0:
            if i == qtd_linhas - 1 or j == len(fliperama[i]) - 1:
                cache[(i, j)] = fliperama[i][j]
            else:
                stack.append((i, j, 1))
                stack.append((i+1, j, 0))
                stack.append((i, j+1, 0))
        else:
            cache[(i, j)] = fliperama[i][j] + min(cache[(i+1, j)], cache[(i, j+1)])

    return cache[(0, 0)]

def somaMaxima():
    cache = {}
    stack = [(0, 0, 0)]

    while stack:
        i, j, st = stack.pop()
        if (i, j) in cache:
            continue

        if st == 0:
            if i == qtd_linhas - 1 or j == len(fliperama[i]) - 1:
                cache[(i, j)] = fliperama[i][j]
            else:
                stack.append((i, j, 1))
                stack.append((i+1, j, 0))
                stack.append((i, j+1, 0))
        else:
            cache[(i, j)] = fliperama[i][j] + max(cache[(i+1, j)], cache[(i, j+1)])

    return cache[(0, 0)]

print('maximo:', somaMaxima())
print('minimo:', somaMinima())
