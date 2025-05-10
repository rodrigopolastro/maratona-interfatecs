# 7:50 - 8:50
import sys
sys.setrecursionlimit(10000)

linhas, colunas, x_inicial, y_inicial = [int(x) for x in input().split()]
tolerancia = int(input())
matriz = []
for _ in range(linhas):
   matriz.append(input().split())

valorComparacaoPositivo = int(matriz[x_inicial-1][y_inicial-1]) + tolerancia
valorComparacaoNegativo = int(matriz[x_inicial-1][y_inicial-1]) - tolerancia
jaVisitados = set()
respostaTotal = 0
def bfs(posicao_x,posicao_y):
    global respostaTotal
    global jaVisitados
    global tolerancia
    if posicao_x < 0 or posicao_x > linhas - 1 or posicao_y < 0 or posicao_y > colunas - 1:
        return
    if int(matriz[posicao_x][posicao_y]) <= valorComparacaoPositivo and int(matriz[posicao_x][posicao_y]) >= valorComparacaoNegativo and (posicao_x,posicao_y) not in jaVisitados:
    # if abs(int(matriz[posicao_x][posicao_y]) - int(matriz[x_inicial-1][y_inicial-1])) <= tolerancia and (posicao_x,posicao_y) not in jaVisitados:
        jaVisitados.add((posicao_x,posicao_y))
        respostaTotal += 1
        bfs(posicao_x-1,posicao_y)
        bfs(posicao_x+1,posicao_y)
        bfs(posicao_x,posicao_y-1)
        bfs(posicao_x,posicao_y+1)
    else:
        jaVisitados.add((posicao_x,posicao_y))
        

bfs(x_inicial-1,y_inicial-1)
print(respostaTotal)