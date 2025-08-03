# problema "Fusoes" da OBI para praticar union-find
#enunciado em https://br.spoj.com/problems/FUSOES1/

def encontraPatriarcaOtimizada(elemento):
    if paiElemento[elemento] == elemento:
        return elemento
    
    # conceito de programação dinâmica: evita recálculos já salvando o patriarca como o pai
    patriarca = encontraPatriarcaOtimizada(paiElemento[elemento])
    paiElemento[elemento] = patriarca
    return patriarca

def juntaFamiliasOtimizada(elementoA, elementoB):
    patriarcaA = encontraPatriarcaOtimizada(elementoA)
    patriarcaB = encontraPatriarcaOtimizada(elementoB)
    
    # se forem tiverem o mesmo patriarca, já estão na mesma família
    if patriarcaA == patriarcaB:
        return
    
    maiorDistanciaA = distanciaDescendenteMaisLonge[patriarcaA]
    maiorDistanciaB = distanciaDescendenteMaisLonge[patriarcaB]
    
    # leva em consideração a distância do descendente mais distante para decidir
    # quem será tido como pai de quem (minimizando as iterações)
    if maiorDistanciaA < maiorDistanciaB:
        paiElemento[patriarcaA] = patriarcaB
    elif maiorDistanciaB < maiorDistanciaA:
        paiElemento[patriarcaB] = patriarcaA
    elif maiorDistanciaA == maiorDistanciaB:
        # se estiverem a uma mesma distância, atribui qualquer um e aumenta a distância do outro
        paiElemento[patriarcaA] = patriarcaB
        distanciaDescendenteMaisLonge[patriarcaB] = maiorDistanciaB + 1
   
# INICIO 
qtdBancos, qtdOperacoes = [int(_) for _ in input().split()]
paiElemento = [i for i in range(qtdBancos)]
distanciaDescendenteMaisLonge = [0 for _ in range(qtdBancos)]

for _ in range(qtdOperacoes):
    entradaOperacao = input().split()
    operacao = entradaOperacao[0]
    banco1 = int(entradaOperacao[1])-1
    banco2 = int(entradaOperacao[2])-1
    
    if operacao == 'F':
        juntaFamiliasOtimizada(banco1, banco2)
    elif operacao == 'C':
        if(encontraPatriarcaOtimizada(banco1) == encontraPatriarcaOtimizada(banco2)):
            print('S')
        else:
            print('N')