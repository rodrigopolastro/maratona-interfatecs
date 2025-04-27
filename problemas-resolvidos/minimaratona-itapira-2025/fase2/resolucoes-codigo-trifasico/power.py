ataque = 1
qtdCavaleiros, qtdCartas = [int(_) for _ in input().split()]
cartas = input().split()

t, r, s = cartas.count('T'), cartas.count('R'), cartas.count('S')

ataque += t

ataque += (qtdCavaleiros // 2) * r

for _ in range(s):
    somaAtual = qtdCavaleiros * ataque
    somaPrevista = (ataque + ataque//2) * (qtdCavaleiros-1)
    if somaPrevista <= somaAtual:
        break

    qtdCavaleiros -= 1
    ataque += ataque // 2

print(qtdCavaleiros * ataque)
