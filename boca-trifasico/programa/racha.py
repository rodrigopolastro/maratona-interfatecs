# 16:11 -> 20:47
"""
FACABAR
AARABQT
TOMABMQ
EECIGAA
CFYYLNA
TAUHHIB
WCHNQMA 


FATEC
FACA
CAFE
FAMILIA
BOLA

"""
# matriz = [
# 'AACABAR',
# 'AIRABQT',
# 'TOLABMQ',
# 'EECIGAA',
# 'CFYYMNA',
# 'TAUHHAB',
# 'WCHNQMF', 
# ]
vezes = int(input())
matriz= []
for i in range(vezes):
    matriz.append(input())
def gerarcolunas():
    retornar = []
    c = len(matriz)
    for i in range(c):
        palavra = ''        # matriz[LINHa][COLUNA]  -> [0:6][0]
        for a in range(c):
            palavra+=matriz[a][i]
        retornar.append(palavra)
    return retornar
col = gerarcolunas()

contador = 0
# lista = [ 'FACA','FATEC','CAFE','FAMILIA']
palavras = int(input())
lista = []
for i in range(palavras):
    lista.append(input())

    ##
# for index_x in range(len(matriz)): # horizontal
#     for index_y in range(len(matriz[0])):
#         if matriz[index_x][index_x:index_y] in lista or matriz[index_x][index_y-1:index_x:-1] in lista or matriz[index_x][index_y::-1] in lista:
#             contador+=1
for i in range(len(matriz)):
    for index,palavra in enumerate(lista):
        if palavra in matriz[i] or palavra in matriz[i][::-1]: 
            lista[index] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            contador+=1
           
    ###

for i in range(len(lista)): # coluna

    for j in col:
        
        if lista[i] in j or lista[i] in ''.join(reversed(j)):
            lista[i]='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            
            contador+=1


def gerar_diagonais():
    """
   
    m[0][5]+m[1][6]
    m[0][4]+m[1][5]+m[2][6]
    m[0][3]+m[1][4]+m[2][5]+m[3][6]
    m[0][2]+m[1][3]+m[2][4]+m[3][5]+m[4][6]
    m[0][1]+m[1][2]+m[2][3]+m[3][4]+m[4][5]+m[5][6]



    m[0][0]+m[1][1]+m[2][2]+m[3][3]+m[4][4]+m[5][5]+m[6][6]

    
    m[1][0]+m[2][1]+m[3][2]+m[4][3]+m[5][4]+m[6][5]
    m[2][0]+m[3][1]+m[4][2]+m[5][3]+m[6][4]
    m[3][0]+m[4][1]+m[5][2]+m[6][3]
    m[4][0]+m[5][1]+m[6][2]
    m[5][0]+m[6][1]
    m[6][0]
    """
    numero = len(matriz)
    diagonal_principal = []
    diagonal_secundaria = []
    for i in range(numero):
        diagonal_principal.append(matriz[i][i])
        diagonal_secundaria.append(matriz[i][numero-i-1])
    diagonal_principal = ''.join(diagonal_principal)
    diagonal_secundaria = ''.join(diagonal_secundaria)
    
    diagonais= []
    linha = 0
    coluna = 1

    for i in range(1,numero):
        linha = 0
        coluna = i

        diagonal = []
        diagonalembaixo = []
        for j in range(numero-i):
            
            diagonal.append(matriz[linha][coluna])
            diagonalembaixo.append(matriz[coluna][linha])
            linha+=1
            coluna+=1
            
        diagonais.append(''.join(diagonal))  
        diagonais.append(''.join(diagonalembaixo))
    diagonais.append(diagonal_principal)
    diagonais.append(diagonal_secundaria)
    # matriz = [
    # 'AACABAR',
    # 'AIRABQT',
    # 'TOLABMQ',
    # 'EECIGAA',
    # 'CFYYMNA',
    # 'TAUHHAB',
    # 'WCHNQMF', 
    # ]
    
    for i in range(numero-2,-1,-1):
        linha = 0
        coluna = i

        diagonal = []
        diagonalembaixo = []
        for j in range(i+1):
            
            diagonal.append(matriz[linha][coluna])
            diagonalembaixo.append(matriz[coluna][linha])
            linha+=1
            coluna-=1
            
        diagonais.append(''.join(diagonal))  
        diagonais.append(''.join(diagonalembaixo))
    


    
    return diagonais
        
    

diagonais = gerar_diagonais()

for i in diagonais:
    for index,j in enumerate(lista):
        if j in i or j in i[::-1]:
            lista[index] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            contador+=1

print(contador)









