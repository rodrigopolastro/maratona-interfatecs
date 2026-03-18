from math import dist

qtdPerigos = 0
xCasa, yCasa, raio = [int(_) for _ in input().split()]
posicaoCasa = [xCasa, yCasa]
qtdInimigos = int(input())
for _ in range(qtdInimigos):
    xInimigo, yInimigo = [int(_) for _ in input().split()]
    posicaoInimigo = [xInimigo, yInimigo]
    distanciaInimigo = dist(posicaoCasa, posicaoInimigo)
    if distanciaInimigo <= raio:
        qtdPerigos += 1
print(qtdPerigos)

# 0 0 5
# 5
# 1 2
# 4 0
# 6 0
# -3 -4
# 0 5