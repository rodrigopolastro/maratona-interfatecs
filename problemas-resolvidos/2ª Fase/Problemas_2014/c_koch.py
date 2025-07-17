################################################################################
# Objetivo: 
#   Calcular a área do fractal de Koch (Koch Snowflake) dados a medida do lado e o nível
# Comentários: 
#   É uma recorrência que poderia ser resolvida com recursividade! 
#   Fiz por loops mesmo para poupar tempo, mas a ideia foi exatamente de recorrência
# Autor: Rodrigo
# Data: 16/07/2025
# Duração: 45m
################################################################################
from math import sqrt

def area_triangulo_equilatero(lado):
    # return 1
    return lado**2 * sqrt(3) / 4

while True:
    entrada = input().split()
    ladoTrianguloInicial, qtdNiveis = float(entrada[0]), int(entrada[1])
    if int(ladoTrianguloInicial) == int(qtdNiveis) == 0:
        break

    areaTotal = area_triangulo_equilatero(ladoTrianguloInicial)

    if qtdNiveis == 1:
        print(f"{areaTotal:.8f}")
    else:
        ladoAtual = ladoTrianguloInicial / 3
        qtdTriangulos = 3
        for _ in range(qtdNiveis-1):
            areaNivelAtual = area_triangulo_equilatero(ladoAtual) * qtdTriangulos
            areaTotal = areaTotal + areaNivelAtual

            ladoAtual = ladoAtual / 3
            qtdTriangulos = qtdTriangulos * 4

        print(f"{areaTotal:.8f}")
