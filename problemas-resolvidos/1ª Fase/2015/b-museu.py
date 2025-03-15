# 1:45 -  2:20
def buscarRec(posicao):
    global jaVisitados
    if posicao in jaVisitados or posicao[0] >= colunas or posicao[0] < 0 or posicao[1] >= linhas or posicao[1] < 0:
        return
    if matriz[posicao[0]][posicao[1]] == '0':
        jaVisitados.add(posicao)
        return
    jaVisitados.add(posicao)
    buscarRec((posicao[0]+1, posicao[1]))
    buscarRec((posicao[0]-1, posicao[1]))
    buscarRec((posicao[0], posicao[1]+1))
    buscarRec((posicao[0], posicao[1]-1))

try:
    while True:   
            
        linhas,colunas = [int(x) for x in input().split()]
        matriz =[]
        for _ in range(colunas):
            matriz.append(input().split())
            
        jaVisitados = set()
        res = 0
        for linha in range(colunas):
            for coluna in range(linhas):
                if matriz[linha][coluna] == '1' and (linha,coluna) not in jaVisitados:
                    buscarRec((linha,coluna))
                    res+=1
        print(res)
        
except EOFError:
    pass       