# problema "Fusoes" da OBI para praticar union-find
#enunciado em https://br.spoj.com/problems/FUSOES1/

def encontraPatriarca(elemento):
    if paisElementos[elemento] == elemento:
        return elemento
    
    patriarca = encontraPatriarca(paisElementos[elemento])
    paisElementos[elemento] = patriarca
    return patriarca

def juntaFamilias(elementoA, elementoB):
    paisElementos[encontraPatriarca(elementoB)] = encontraPatriarca(elementoA)
    
# INICIO
qtdBancos, qtdOperacoes = [int(_) for _ in input().split()]
paisElementos = [i for i in range(qtdBancos)]

for _ in range(qtdOperacoes):
    entradaOperacao = input().split()
    operacao = entradaOperacao[0]
    banco1 = int(entradaOperacao[1])-1
    banco2 = int(entradaOperacao[2])-1
    
    if operacao == 'F':
        juntaFamilias(banco1, banco2)
    elif operacao == 'C':
        if(encontraPatriarca(banco1) == encontraPatriarca(banco2)):
            print('S')
        else:
            print('N')
            