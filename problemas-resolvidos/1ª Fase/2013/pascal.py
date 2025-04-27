import math

qtd = int(input())

for _ in range(qtd):
    x, y = map(int, input().split())
    print(math.comb(x, y))
