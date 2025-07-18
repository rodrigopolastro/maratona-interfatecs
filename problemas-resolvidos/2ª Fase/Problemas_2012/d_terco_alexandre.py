# inicio 9:05 fim 10:44 - feat Rodrigo Polastro

import decimal
decimal.getcontext().prec = 50
while True:
    xImagemEsquerda, yImagemEsquerda, xImagemDireita, yImagemDireita = [
        decimal.Decimal(x) for x in input().split()]
    if xImagemEsquerda == yImagemEsquerda == xImagemDireita == yImagemDireita == 0:
        break
    xEnquadramentoObjetivoEsquerda, yEnquadramentoObjetivoEsquerdo, xEnquadramentoObjetivoDireito, yEnquadramentoObjetivoDireito = [
        decimal.Decimal(x) for x in input().split()]

    xTamanhoImagem = abs(xImagemDireita - xImagemEsquerda)
    # print(xTamanhoImagem)
    
    yTamanhoImagem = abs(yImagemEsquerda - yImagemDireita)
    # print(yTamanhoImagem)
    
    # print("Tamanho objeto X", abs(xEnquadramentoObjetivoEsquerda - xEnquadramentoObjetivoDireito) )
    # print("Tamanho objeto Y",abs(yEnquadramentoObjetivoEsquerdo - yEnquadramentoObjetivoDireito))
    umTercoX = decimal.Decimal(xTamanhoImagem / 3)
    umTercoY = decimal.Decimal(yTamanhoImagem / 3)

    pontoTercos = [
        (xImagemEsquerda + umTercoX, yImagemEsquerda - umTercoY),
        (xImagemEsquerda + umTercoX*2, yImagemEsquerda -umTercoY), 
        (xImagemEsquerda + umTercoX, yImagemEsquerda -umTercoY*2),
        (xImagemEsquerda + umTercoX*2, yImagemEsquerda -umTercoY*2)
]

    imprimirV = False
    for ponto in pontoTercos:
        # print(ponto)
        if (xEnquadramentoObjetivoEsquerda <= ponto[0] <= xEnquadramentoObjetivoDireito and yEnquadramentoObjetivoDireito <= ponto[1] <= yEnquadramentoObjetivoEsquerdo): # or (xEnquadramentoObjetivoEsquerda == ponto[0] == yEnquadramentoObjetivoEsquerdo) or (yEnquadramentoObjetivoEsquerdo == ponto[1] == yEnquadramentoObjetivoDireito):
            imprimirV = True
            break
    if imprimirV:
        print("V")
    else:
        print("F")
