################################################################################
# Objetivo: A partir das posições de um rei preto e de uma rainha, torre e cavalo
#           brancos em um tabuleiro de xadrez 4x4, determinar se há cheque mate 
#           no próximo lance e, se sim, qual movimento deve ser feito.
# Autor: Rodrigo
# Data: 31/01/2025
# Duração: ... Fiquei 1 semana nessa porcaria
################################################################################
import copy

DIMENSAO_TABULEIRO = 4
MOVIMENTACAO_LINHAS_COLUNAS, MOVIMENTACAO_DIAGONAL = 'linhasColunas', 'diagonais'
REI, RAINHA, TORRE, CAVALO = 'K', 'R', 'T', 'C'
ATAQUE_RAINHA, ATAQUE_TORRE, ATAQUE_CAVALO = 'r', 't', 'c'
PECAS = ['R', 'T', 'C']
def geraMovimentosRetilineos(partidaI, partidaJ, tipoMovimento):
    INCREMENTOS_LINHAS_COLUNAS = [(0,1), (0,-1), (1,0), (-1,0)]
    INCREMENTOS_DIAGONAIS = [(1,1), (-1,-1), (1,-1), (-1,1)]
    
    if tipoMovimento == MOVIMENTACAO_LINHAS_COLUNAS:
        incrementos = INCREMENTOS_LINHAS_COLUNAS
    elif tipoMovimento == MOVIMENTACAO_DIAGONAL:
        incrementos = INCREMENTOS_DIAGONAIS
    else:
        return set()
    
    movimentos = set()
    for incI, incJ in incrementos:
        i, j = partidaI+incI, partidaJ+incJ
        while 1 <= i <= DIMENSAO_TABULEIRO and 1 <= j <= DIMENSAO_TABULEIRO:
            movimentos.add(tuple([i, j]))
            if tabuleiroAnalise[i][j] in PECAS:
                break
            i, j = i+incI, j+incJ
        
    return movimentos 

def movimentosTorre(torre, atacando=False):    
    movimentos = geraMovimentosRetilineos(torre[0], torre[1], MOVIMENTACAO_LINHAS_COLUNAS)
    if not atacando:
        movimentos = set([mov for mov in movimentos if tabuleiroAnalise[mov[0]][mov[1]] not in PECAS])
    
    return movimentos    
    
def movimentosRainha(rainha, atacando=False):    
    movimentosLinhasColunas = geraMovimentosRetilineos(rainha[0], rainha[1], MOVIMENTACAO_LINHAS_COLUNAS)
    movimentosDiagonais = geraMovimentosRetilineos(rainha[0], rainha[1], MOVIMENTACAO_DIAGONAL)    
    movimentos = movimentosLinhasColunas.union(movimentosDiagonais)  
    if not atacando:
        movimentos = set([mov for mov in movimentos if tabuleiroAnalise[mov[0]][mov[1]] not in PECAS])
        
    return movimentos

def movimentosCavalo(cavalo):
    movimentos = set()
    movimentos.add(tuple([cavalo[0]-2, cavalo[1]+1]))
    movimentos.add(tuple([cavalo[0]-2, cavalo[1]-1]))
    movimentos.add(tuple([cavalo[0]+2, cavalo[1]+1]))
    movimentos.add(tuple([cavalo[0]+2, cavalo[1]-1]))
    movimentos.add(tuple([cavalo[0]+1, cavalo[1]+2]))
    movimentos.add(tuple([cavalo[0]+1, cavalo[1]-2]))
    movimentos.add(tuple([cavalo[0]-1, cavalo[1]+2]))
    movimentos.add(tuple([cavalo[0]-1, cavalo[1]-2]))  
    
    for i, mov in enumerate(movimentos):
        movimentos = [pos for pos in movimentos if (1 <= pos[0] <= DIMENSAO_TABULEIRO) and (1 <= pos[1] <= DIMENSAO_TABULEIRO)]    
    return movimentos 

def movimentosRei(rei):
    movimentos = set()
    for addI in [-1, 1, 0]:
        for addJ in [-1, 0, 1]:
            newI, newJ = rei[0]+addI,  rei[1]+addJ
            if (1 <= newI <= 4) and (1 <= newJ <= 4): 
                if tabuleiroAnalise[newI][newJ] == '' or not temPecaAtacando(newI, newJ): 
                    movimentos.add(tuple([newI, newJ]))
    return list(movimentos)

def temPecaAtacando(i, j):
    for peca in PECAS:
        if peca.lower() in tabuleiroAnalise[i][j]:
            return True
    return False

def reiEstaEmCheque(rei):
    if temPecaAtacando(rei[0], rei[1]):
        return True
    return False

def rainhaAplicaMate(rainha, torre, cavalo):
    global tabuleiroAnalise 
    for movRainha in movimentosRainha(rainha):
        tabuleiroAntes = copy.deepcopy(tabuleiroAnalise)
        
        tabuleiroAnalise[rainha[0]][rainha[1]] = tabuleiroAnalise[rainha[0]][rainha[1]].replace(RAINHA, '')
        tabuleiroAnalise[movRainha[0]][movRainha[1]] += RAINHA
        
        for movTorre in movimentosTorre(torre, True):
            tabuleiroAnalise[movTorre[0]][movTorre[1]] += ATAQUE_TORRE 
        for movCavalo in movimentosCavalo(cavalo):
            tabuleiroAnalise[movCavalo[0]][movCavalo[1]] += ATAQUE_CAVALO
        for cheque in movimentosRainha(movRainha, True):
            tabuleiroAnalise[cheque[0]][cheque[1]] += ATAQUE_RAINHA
                    
        if reiEstaEmCheque(POSICAO_REI):
            if len(movimentosRei(POSICAO_REI)) == 0:
                return [movRainha[0], movRainha[1]]
                
        tabuleiroAnalise = copy.deepcopy(tabuleiroAntes)
    return False

def torreAplicaMate(rainha, torre, cavalo):
    global tabuleiroAnalise
    for movTorre in movimentosTorre(torre):
        tabuleiroAntes = copy.deepcopy(tabuleiroAnalise)
        
        tabuleiroAnalise[torre[0]][torre[1]] = tabuleiroAnalise[torre[0]][torre[1]].replace(TORRE, '')
        tabuleiroAnalise[movTorre[0]][movTorre[1]] += TORRE
        
        for movRainha in movimentosRainha(rainha, True):
            tabuleiroAnalise[movRainha[0]][movRainha[1]] += ATAQUE_RAINHA 
        for movCavalo in movimentosCavalo(cavalo):
            tabuleiroAnalise[movCavalo[0]][movCavalo[1]] += ATAQUE_CAVALO
        for cheque in movimentosTorre(movTorre, True):
            tabuleiroAnalise[cheque[0]][cheque[1]] += ATAQUE_TORRE
                    
        if reiEstaEmCheque(POSICAO_REI):
            if len(movimentosRei(POSICAO_REI)) == 0:
                return [movTorre[0], movTorre[1]]
            
        tabuleiroAnalise = copy.deepcopy(tabuleiroAntes)
    return False

def cavaloAplicaMate(rainha, torre, cavalo):
    global tabuleiroAnalise
    for movCavalo in movimentosCavalo(cavalo):
        tabuleiroAntes = copy.deepcopy(tabuleiroAnalise)

        tabuleiroAnalise[cavalo[0]][cavalo[1]] = tabuleiroAnalise[cavalo[0]][cavalo[1]].replace(CAVALO, '')
        tabuleiroAnalise[movCavalo[0]][movCavalo[1]] += CAVALO
        
        for movRainha in movimentosRainha(rainha, True):
            tabuleiroAnalise[movRainha[0]][movRainha[1]] += ATAQUE_RAINHA
        for movTorre in movimentosTorre(torre, True):
            tabuleiroAnalise[movTorre[0]][movTorre[1]] += ATAQUE_TORRE
        for cheque in movimentosCavalo(movCavalo):
            tabuleiroAnalise[cheque[0]][cheque[1]] += ATAQUE_CAVALO
                    
        if reiEstaEmCheque(POSICAO_REI):
            if len(movimentosRei(POSICAO_REI)) == 0:
                return [movCavalo[0], movCavalo[1]]
            
        tabuleiroAnalise = copy.deepcopy(tabuleiroAntes)
    return False

while True:
    POSICAO_REI =  tuple(map(int, input().split()))
    if POSICAO_REI == (0, 0):
        break
    POSICAO_RAINHA = tuple(map(int, input().split()))
    POSICAO_TORRE  =  tuple(map(int, input().split()))
    POSICAO_CAVALO =  tuple(map(int, input().split()))
    
    tabuleiro = [['' for i in range(DIMENSAO_TABULEIRO+1)] for j in range(DIMENSAO_TABULEIRO+1)]
    tabuleiro[POSICAO_REI[0]][POSICAO_REI[1]] = REI
    tabuleiro[POSICAO_RAINHA[0]][POSICAO_RAINHA[1]] = RAINHA
    tabuleiro[POSICAO_TORRE[0]][POSICAO_TORRE[1]] = TORRE
    tabuleiro[POSICAO_CAVALO[0]][POSICAO_CAVALO[1]] = CAVALO
    
    tabuleiroAnalise = copy.deepcopy(tabuleiro)
    mateRainha = rainhaAplicaMate(POSICAO_RAINHA, POSICAO_TORRE, POSICAO_CAVALO)
    if mateRainha:
        movI, movJ = mateRainha[0], mateRainha[1]
        print(RAINHA, movI, movJ)
        continue
    
    tabuleiroAnalise = copy.deepcopy(tabuleiro)
    mateTorre = torreAplicaMate(POSICAO_RAINHA, POSICAO_TORRE, POSICAO_CAVALO)
    if mateTorre:
        movI, movJ = mateTorre[0], mateTorre[1]
        print(TORRE, movI, movJ)
        continue
    
    tabuleiroAnalise = copy.deepcopy(tabuleiro)
    mateCavalo = cavaloAplicaMate(POSICAO_RAINHA, POSICAO_TORRE, POSICAO_CAVALO)
    if mateCavalo:
        movI, movJ = mateCavalo[0], mateCavalo[1]
        print(CAVALO, movI, movJ)
        continue
    
    print('N')      