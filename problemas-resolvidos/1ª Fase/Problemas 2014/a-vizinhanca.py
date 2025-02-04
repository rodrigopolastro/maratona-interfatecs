#INICIO 8:50 / TÉRMINO  10:09 -> problemas com arquivo 'corrompido' no boca fez isso levar mais tempo doque o previsto
"""
° Alfredo não quer ser vizinho de Beto, e também não quer ser vizinho de Darci;
° Beto não deve ser vizinho de Alfredo e não suportaria a vizinhança de Cláudio;
° Darci não gostaria de ter Alfredo como vizinho;
° Cláudio não quer ter Beto como vizinho;
° Ernesto não tem problemas de relacionamento com ninguém, afinal ele sempre convida todos
para um samba no Brás.

**NÃO É CONSIDERADO VIZINHO SE ESTIVER NA DIAGONAL
"""

restricoes = {
    'A':['B','D'],
    'B':['A','C'],
    'C':['B'],
    'D':['A'],
    'E':[]
}
respostas = []
def pegarVizinhos(posicoes:tuple|list,matriz) -> list:
    lim_x,lim_y = len(matriz),len(matriz[0])
    retornar = []
    for x in [-1,0,1]:
        for y in [-1,0,1]:

            if abs(x) != abs(y) and lim_x > posicoes[0]+x and posicoes[0]+x >= 0 and lim_y > posicoes[1]+y and posicoes[1]+y >= 0:
                if matriz[posicoes[0]+x][posicoes[1]+y] != '0':
                    retornar.append(matriz[posicoes[0]+x][posicoes[1]+y])
    return retornar

while True:
    printarV = True
    x,y = [int(inp) for inp in input().split()]
    if x == 0:
        break
    matriz = []
    for _ in range(y):
        matriz.append(input().split())
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if matriz[linha][coluna] != '0':
                comparar = pegarVizinhos((linha,coluna),matriz)
                if printarV: # <-- gambiarra para rodar no nosso programa test
                    for restritos in comparar:
                        if restritos in restricoes[matriz[linha][coluna]]:
                            respostas.append("F")
                            # print("F")
                            printarV = False
                    
    if printarV:
        # print('V')
        respostas.append("V")
for r in respostas:
    print(r)
    

                    
                
        
    