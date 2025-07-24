respostas = []
try:
    while True:
        jaVisitados = set()
        jaVisitados1 = set()
        qtdeColunas = int(input())
        matriz = []
        primeiro = tuple()
        for _ in range(qtdeColunas):
            entradaUsuario = list(input())
            if 'I' in entradaUsuario:
                primeiro = (_,entradaUsuario.index('I'))
            matriz.append(entradaUsuario)
        
        def bfs(x,y):
            limite = len(matriz)
            
            
            if 0 <= x < limite and 0 <= y < limite and (x,y) not in jaVisitados and matriz[x][y] not in "*#":
                
                if 'T' in jaVisitados1 and 'I' in jaVisitados1:
                    return 
                # print(x,y,limite)
                # matriz[x][y] = 'X'
                # for a in matriz:
                #     print(a)
                jaVisitados.add((x,y))
                jaVisitados1.add(matriz[x][y])
                proximos = [(1,0),(-1,0),(0,-1),(0,1)]
                for p in proximos:
                    bfs(x+p[0] , y+p[1])
        bfs(primeiro[0],primeiro[1])
        if 'T' in jaVisitados1 and 'I' in jaVisitados1:
            respostas.append("S")
        else:
            respostas.append("N")
except EOFError:
    for r in respostas:
        print(r)
    