qtdElementos = 999
paiElemento = [i for i in range(qtdElementos)]

# =============== FUNÇÕES DO UNION FIND - VERSÕES PADRÃO ===============
def encontraPatriarca(elemento): #FIND
    if paiElemento[elemento] == elemento:
        return elemento

    return encontraPatriarca(paiElemento[elemento])

def juntaFamilias(elementoA, elementoB): #UNION
    paiElemento[encontraPatriarca(elementoB)] = encontraPatriarca(elementoA)
    
# =============== FUNÇÕES DO UNION FIND - VERSÕES OTIMIZADAS ===============
qtdElementos = 999
paiElemento = [i for i in range(qtdElementos)]
distanciaDescendenteMaisLonge = [0 for _ in range(qtdElementos)]
#opcionalmente, armazena a quantidade de descendentes de cada elemento
qtdDescendentes = [1 for _ in range(qtdElementos)] 
#para contar a quantidade de componentes conexas, inicialize um contador com o número de 
#nós  e diminua-o em uma unidade sempre que um nó for adicionado como filho de outro
qtdComponentesConexas = qtdElementos

def encontraPatriarcaOtimizada(elemento): #FIND
    if paiElemento[elemento] == elemento:
        return elemento
    
    # conceito de programação dinâmica: evita recálculos já salvando o patriarca como o pai
    #OBS: essa otimização é essencial para tornar o algoritmo performático
    patriarca = encontraPatriarcaOtimizada(paiElemento[elemento])
    paiElemento[elemento] = patriarca
    return patriarca

def juntaFamiliasOtimizada(elementoA, elementoB): #UNION
    patriarcaA = encontraPatriarcaOtimizada(elementoA)
    patriarcaB = encontraPatriarcaOtimizada(elementoB)
    
    # se forem tiverem o mesmo patriarca, já estão na mesma família
    if patriarcaA == patriarcaB:
        return
    qtdComponentesConexas = qtdComponentesConexas-1
    
    maiorDistanciaA = distanciaDescendenteMaisLonge[patriarcaA]
    maiorDistanciaB = distanciaDescendenteMaisLonge[patriarcaB]
    
    # leva em consideração a distância do descendente mais distante para decidir
    # quem será tido como pai de quem (minimizando as iterações)
    #OBS: essa otimização é mais avançada; nem sempre será necessária
    if maiorDistanciaA < maiorDistanciaB:
        paiElemento[patriarcaA] = patriarcaB
        qtdDescendentes[patriarcaB] = qtdDescendentes[patriarcaB] + qtdDescendentes[patriarcaA]
    elif maiorDistanciaB < maiorDistanciaA:
        paiElemento[patriarcaB] = patriarcaA
        qtdDescendentes[patriarcaA] = qtdDescendentes[patriarcaA] + qtdDescendentes[patriarcaB]
    elif maiorDistanciaA == maiorDistanciaB:
        # se estiverem a uma mesma distância, atribui qualquer um e aumenta a distância do outro
        paiElemento[patriarcaA] = patriarcaB
        qtdDescendentes[patriarcaB] = qtdDescendentes[patriarcaB] + qtdDescendentes[patriarcaA]
        distanciaDescendenteMaisLonge[patriarcaB] = maiorDistanciaB + 1
    
