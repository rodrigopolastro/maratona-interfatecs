entrada = tuple([int(_) for _ in input().split()])
saida = tuple([int(_) for _ in input().split()])
qtdMonstros = int(input())
matrizInicial = [
    list('.'*100) for _ in range(100)
]

for monstro in range(qtdMonstros):
    posicao_monstro = [int(_) for _ in input().split()]
    matrizInicial[posicao_monstro[0]][posicao_monstro[1]] = "#"

caminho = {entrada: None}
proximosNaLista = [entrada]



def varredura(posicao: tuple):
    
    # for x in [-1, 0, 1]:
    #     for y in [-1, 0, 1]:
            
    listaVerificar = [
        (posicao[0]-1, posicao[1]),
        (posicao[0]+1, posicao[1]),
        (posicao[0], posicao[1]+1),
        (posicao[0], posicao[1]-1),
    ]
        # if 0 <= posicao[0]+x < 100 and 0 <= posicao[1]+y < 100 and matrizInicial[posicao[0]+x][posicao[1]+y] != "#" and abs(x) != abs(y) and (posicao[0]+x, posicao[1]+y) not in proximosNaLista and (posicao[0]+x, posicao[1]+y) not in jaVisitados:
    for p in listaVerificar:
        if 0 <= p[0] < 100 and 0 <= p[1] < 100 and matrizInicial[p[0]][p[1]] != "#" and (p[0], p[1]) not in proximosNaLista and (p[0], p[1]) not in caminho:
            
                
            caminho[(p[0], p[1])] = posicao 
            proximosNaLista.append((p[0], p[1]))

while True:

    if proximosNaLista == []:
        break

    
    if proximosNaLista[0] == saida:
        break
    varredura(proximosNaLista[0])

    
    proximosNaLista.pop(0)

  

if saida not in caminho.keys():
    print(-1)
else:
   
    resposta = []
    while True:
        if caminho[saida] == None:
            break
        resposta.append(caminho[saida])
        saida = caminho[saida]
    print(len(resposta))
