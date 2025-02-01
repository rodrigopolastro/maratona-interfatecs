def popularMatrizHorizontalmenteVertical(posicao, matriz, outrasPecas = []):
    for x in [1,2,3]:    
        if posicao[0]+x <= 4 :
            if [posicao[0]+x,posicao[1]] in outrasPecas:
                matriz[posicao[0]+x][posicao[1]] = 'x'
                break
            else:
                matriz[posicao[0]+x][posicao[1]] = 'x'
    for x in [-1,-2,-3]:    
        if posicao[0]+x > 0:
            if [posicao[0]+x,posicao[1]] in outrasPecas:
                matriz[posicao[0]+x][posicao[1]] = 'x'
                break
            else:    
                matriz[posicao[0]+x][posicao[1]] = 'x'
    for y in [1,2,3]:    
        if posicao[1]+y <= 4 :
            if [posicao[0],posicao[1]+y] in outrasPecas:
                matriz[posicao[0]][posicao[1]+y] = 'x'
                break
            else:
                matriz[posicao[0]][posicao[1]+y] = 'x'
    for y in [-1,-2,-3]:    
        if posicao[1]+y > 0:
            if [posicao[0],posicao[1]+y] in outrasPecas:
                matriz[posicao[0]][posicao[1]+y] = 'x'
                break
            else:    
                matriz[posicao[0]][posicao[1]+y] = 'x'
                
def popularMatrizDiagonalmente(posicao, matriz, outrasPecas):
    for xy in [1,2,3]:
        if posicao[0]+xy <= 4 and posicao[1]+xy <=4:
            if [posicao[0]+xy,posicao[1]+xy] in outrasPecas:
                matriz[posicao[0]+xy][posicao[1]+xy] = 'x'
                break
            matriz[posicao[0]+xy][posicao[1]+xy] = 'x'
    for xy in [-1,-2,-3]:
        if posicao[0]+xy > 0 and posicao[1]+xy > 0:
            if [posicao[0]+xy,posicao[1]+xy] in outrasPecas:
                matriz[posicao[0]+xy][posicao[1]+xy] = 'x'
                break
            matriz[posicao[0]+xy][posicao[1]+xy] = 'x'
    for xy in [1,2,3]:
        if posicao[0]+xy <= 4 and posicao[1]-xy > 0 and posicao[0]+posicao[1] == (posicao[0] + xy) + (posicao[1] - xy):
            if [posicao[0]+xy,posicao[1]-xy] in outrasPecas:
                matriz[posicao[0]+xy][posicao[1]-xy]
                break
            matriz[posicao[0]+xy][posicao[1]-xy]
    for xy in [1,2,3]:
        if posicao[0]-xy > 0 and posicao[1]+xy <= 4 and posicao[0]+posicao[1] == (posicao[0] - xy) + (posicao[1] + xy):
            if [posicao[0]-xy,posicao[1]+xy] in outrasPecas:
                matriz[posicao[0]-xy][posicao[1]+xy]
                break
            matriz[posicao[0]-xy][posicao[1]+xy]
            
    
                
def popularMatrizCavalo(posicao,matriz,tipo='adicionar'):
    for x in [-2,-1,1,2]:
        for y in [-2,-1,1,2]:
            if posicao[0]+x > 0 and posicao[0]+x <= 4 and posicao[1]+y > 0 and posicao[1]+y <= 4 and abs(x-y) == 1:
                if tipo == 'remover':
                    matriz[posicao[0]+x][posicao[1]+y] = '.'
                else:
                    matriz[posicao[0]+x][posicao[1]+y] = 'x'
                
def estaCercado(posicao,matriz):
    for x in [-1,0,1]:
        for y in [-1,0,1]:
             if posicao[0]+x > 0 and posicao[0]+x <= 4 and posicao[1]+y > 0 and posicao[1]+y <= 4:
                 if matriz[posicao[0]+x][posicao[1]+y] == '.':
                     return False
    return True   

def posicoesQueAbrangeHorizontal(posicao,matriz, outraspecas = [])->list:
    retornar = []
    for x in [1,2,3]:    
        if posicao[0]+x <= 4 :
            if [posicao[0]+x,posicao[1]] in outraspecas:
                break
            else:
                retornar.append((posicao[0]+x,posicao[1]))
    for x in [-1,-2,-3]:    
        if posicao[0]+x > 0:
            if [posicao[0]+x,posicao[1]] in outraspecas:
                break
            else:    
                retornar.append((posicao[0]+x,posicao[1]))
    for y in [1,2,3]:    
        if posicao[1]+y <= 4 :
            if [posicao[0],posicao[1]+y] in outraspecas:
                break
            else:
                retornar.append((posicao[0],posicao[1]+y))
    for y in [-1,-2,-3]:    
        if posicao[1]+y > 0:
            if [posicao[0],posicao[1]+y] in outraspecas:
                break
            else:    
                retornar.append((posicao[0],posicao[1]+y))
    return retornar
def posicoesQueAbrangeDiagonal(posicao,matriz,outrasPecas)->list:
    retornar = []
    for xy in [1,2,3]:
        if posicao[0]+xy <= 4 and posicao[1]+xy <=4:
            if [posicao[0]+xy,posicao[1]+xy] in outrasPecas:
                break
            retornar.append((posicao[0]+xy,posicao[1]+xy))
    for xy in [-1,-2,-3]:
        if posicao[0]+xy > 0 and posicao[1]+xy > 0:
            if [posicao[0]+xy,posicao[1]+xy] in outrasPecas:
                break
            retornar.append((posicao[0]+xy,posicao[1]+xy))
    for xy in [1,2,3]:
        if posicao[0]+xy <= 4 and posicao[1]-xy > 0 and posicao[0]+posicao[1] == (posicao[0] + xy) + (posicao[1] - xy):
            if [posicao[0]+xy,posicao[1]-xy] in outrasPecas:
                break
            retornar.append((posicao[0]+xy,posicao[1]-xy))
    for xy in [1,2,3]:
        if posicao[0]-xy > 0 and posicao[1]+xy <= 4 and posicao[0]+posicao[1] == (posicao[0] - xy) + (posicao[1] + xy):
            if [posicao[0]-xy,posicao[1]+xy] in outrasPecas:
                break
            retornar.append((posicao[0]-xy,posicao[1]+xy))
    return retornar

def posicoesQueAbrangeCavalo(posicao,matriz)->list:
    retornar = []
    for x in [-2,-1,1,2]:
        for y in [-2,-1,1,2]:
            if posicao[0]+x > 0 and posicao[0]+x <= 4 and posicao[1]+y > 0 and posicao[1]+y <= 4 and abs(x-y) == 1:
                retornar.append((posicao[0]+x,posicao[1]+y))
    return retornar
respostas = []
while True:

    reiPreto = [int(x) for x in input().split()]
    if reiPreto[0] == 0:
        for r in respostas:
            print(r)
        quit()
    rainhaBranca = [int(x) for x in input().split()]
    torreBranca = [int(x) for x in input().split()]
    cavaloBranco = [int(x) for x in input().split()]
    # ordem d precedencia: rainha, torre e cavalo
    matrizInicial = [
    [None,None,None,None,None],
    [None,'.','.','.','.'],
    [None,'.','.','.','.'],
    [None,'.','.','.','.'],
    [None,'.','.','.','.'],
    ]
    ProximosRainha = posicoesQueAbrangeDiagonal(rainhaBranca,matrizInicial,[cavaloBranco,torreBranca])
    ProximosRainha.extend(posicoesQueAbrangeHorizontal(rainhaBranca,matrizInicial,[cavaloBranco,torreBranca]))
    ProximosTorre = posicoesQueAbrangeHorizontal(torreBranca,matrizInicial,[rainhaBranca,cavaloBranco])
    proximosCavalo = posicoesQueAbrangeCavalo(cavaloBranco,matrizInicial)
    achouPosicao = False

    for proximoMov in ProximosRainha:
        novaMatriz = [
        [None,None,None,None,None],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        ]
        if not achouPosicao:
            popularMatrizCavalo(cavaloBranco,novaMatriz)
            popularMatrizHorizontalmenteVertical(torreBranca,novaMatriz,[cavaloBranco])
            popularMatrizHorizontalmenteVertical(proximoMov,novaMatriz,[cavaloBranco,torreBranca])
            popularMatrizDiagonalmente(proximoMov,novaMatriz,[torreBranca,cavaloBranco])
            if estaCercado(reiPreto,novaMatriz):
                respostas.append(f"R {proximoMov[0]} {proximoMov[1]}")
                achouPosicao = True
    
    for proximoMov in ProximosTorre:
        novaMatriz = [
        [None,None,None,None,None],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        ]
        if not achouPosicao:
            popularMatrizCavalo(cavaloBranco,novaMatriz)
            popularMatrizHorizontalmenteVertical(rainhaBranca,novaMatriz,[cavaloBranco])
            popularMatrizDiagonalmente(rainhaBranca,novaMatriz,[cavaloBranco])
            popularMatrizHorizontalmenteVertical(proximoMov,novaMatriz,[cavaloBranco,rainhaBranca])
            if estaCercado(reiPreto,novaMatriz):
                respostas.append(f"T {proximoMov[0]} {proximoMov[1]}")
                achouPosicao = True
    
    for proximoMov in proximosCavalo:
        novaMatriz = [
        [None,None,None,None,None],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        [None,'.','.','.','.'],
        ]
        if not achouPosicao:
            popularMatrizCavalo(proximoMov,novaMatriz)
            popularMatrizHorizontalmenteVertical(torreBranca,novaMatriz,[rainhaBranca,list(proximoMov)])
            popularMatrizHorizontalmenteVertical(rainhaBranca,novaMatriz,[torreBranca,list(proximoMov)])
            popularMatrizDiagonalmente(rainhaBranca,novaMatriz,[torreBranca,list(proximoMov)])
            if estaCercado(reiPreto,novaMatriz):
                respostas.append(f"C {proximoMov[0]} {proximoMov[1]}")
                achouPosicao = True
    if not achouPosicao:
        respostas.append("N")
        