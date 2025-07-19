import sys
sys.setrecursionlimit = 3000
encontrouCaminho = False
fila = []
jaVisitados = []
resposta = []
def dfs(x, y, matriz):
    global jaVisitados
    global fila
    global encontrouCaminho
    limite = len(matriz)
    
    if encontrouCaminho: 
        return
    # print(x,y)
    # print(jaVisitados)
    # print(fila)
    if 0 <= x < limite and 0 <= y < limite:
        elementoMatriz = matriz[x][y]
        # print(elementoMatriz)
        if elementoMatriz != '*' and elementoMatriz != '#' and (x,y) not in jaVisitados:
            # print(x,y,'entrou no if')
            # print('QTs?')
            jaVisitados.append((x,y))
            fila.append((x,y))
            if elementoMatriz == "T":
                encontrouCaminho = True
            
            
            dfs(x, y-1, matriz)
            dfs(x, y+1, matriz)
            dfs(x-1, y, matriz)
            dfs(x+1, y, matriz)


def main():
    while True:
        global fila
        fila = []
        numCol = int(input())
        Matriz = []
        posicaoJogador = tuple()
        for _ in range(numCol):
            entrada = input()
            if 'I' in entrada:
                posicaoJogador = (_, entrada.index("I"))
            Matriz.append(list(entrada))
        fila = [posicaoJogador]
        while len(fila) >= 1:
            if encontrouCaminho == True:
                break
            dfs(fila[0][0], fila[0][1], Matriz)
            fila.pop(0)
            
            
            
            
        if encontrouCaminho:
            print('S')
            resposta.append("S")
        else:
            print('N')
            resposta.append("N")

try:
    main()
except EOFError:
    for r in resposta:
        print(r)
