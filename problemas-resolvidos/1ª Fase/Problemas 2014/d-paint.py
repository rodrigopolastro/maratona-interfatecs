import sys
sys.setrecursionlimit(1000000)
def introduzirVizinhos(comparacao:str|int,posicao:tuple,matriz,jaVisitados : set):
    global resposta
    if 0 > posicao[0] or posicao[0] >= len(matriz) or 0 > posicao[1] or posicao[1] >= len(matriz[0]):
        return
    if matriz[posicao[0]][posicao[1]] != comparacao or posicao in jaVisitados:
        return
    else:
        resposta.add(posicao)
        jaVisitados.add(posicao)
        introduzirVizinhos(comparacao,(posicao[0]+1,posicao[1]),matriz,jaVisitados)
        introduzirVizinhos(comparacao,(posicao[0]-1,posicao[1]),matriz,jaVisitados)
        introduzirVizinhos(comparacao,(posicao[0],posicao[1]+1),matriz,jaVisitados)
        introduzirVizinhos(comparacao,(posicao[0],posicao[1]-1),matriz,jaVisitados)
        
while True:
    jaVisitados = set()
    x , y = [int(_) for _ in input().split()]
    if x == 0:
        break
    matriz = []
    for inp in range(x):
        matriz.append(input().split())
    referencia = tuple([int(_)-1 for _ in input().split()])
    comparacao = matriz[referencia[0]][referencia[1]]
    resposta = set()
    introduzirVizinhos(comparacao,referencia,matriz,jaVisitados)
    print(len(resposta))
    
        