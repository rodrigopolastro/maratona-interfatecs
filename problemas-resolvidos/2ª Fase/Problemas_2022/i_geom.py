from math import sqrt

contador = 0

def printar_impossivel(contador):
    print(f"Triangle #{contador}")
    print("Impossible.")

def printar_resultado(contador, lado, valor):
    print(f"Triangle #{contador}")
    print(f"{lado} = {valor:.3f}")

while True:
    contador += 1

    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    if a == -1:
        calculo = c ** 2 - b ** 2

        if calculo < 0:
            printar_impossivel(contador)
        else:
            printar_resultado(contador, 'a', sqrt(calculo))

    if b == -1:
        calculo = c ** 2 - a ** 2

        if calculo < 0:
            printar_impossivel(contador)
        else:
            printar_resultado(contador, 'b', sqrt(calculo))

    if c == -1:
        calculo = a ** 2 + b ** 2

        if calculo < 0:
            printar_impossivel(contador)
        else:
            printar_resultado(contador, 'c', sqrt(calculo))