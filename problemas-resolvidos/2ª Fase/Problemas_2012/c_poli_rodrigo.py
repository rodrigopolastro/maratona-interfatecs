################################################################################
# Objetivo:
#
# Autor: Rodrigo
# Data: 12/07/2025
# Duração: 40m
################################################################################

qtdCasos = int(input())
# qtdCasos = 1
for indexCaso in range(qtdCasos):
    strPolinomio = input()
    # strPolinomio = '3x5+x3-2x-1'
    termos = strPolinomio.replace('+', 'SPLIT+').replace('-', 'SPLIT-').split('SPLIT')
    termos = list(filter(lambda t: t != '' ,termos))
    
    if(termos[0][0] != '-'):
        termos[0] = '+' + termos[0]

    qtdValoresX = int(input())
    # qtdValoresX = 1
    
    valoresX = [int(_) for _ in input().split()]
    # valorX = 1for valo
    respostasPolinomio = list()
    for valorX in valoresX:
        resultado = 0
        # print('valorX -> ', valorX)
        for termo in termos:
            # sinal = termo[0]
            splitX = termo.split('x')
            if len(splitX) > 1: #tem x
                termoTemX = True
                coeficiente, expoente = splitX[0], splitX[1]
            else:
                termoTemX = False
                coeficiente, expoente = termo, 1
                
            
            if coeficiente == '+' or coeficiente == '-':
                coeficiente = coeficiente + '1'
            
            if not expoente:
                expoente = 1
                
            # print(coeficiente, expoente)
            # coeficiente, expoente = int(coeficiente)
    #         valor = coeficiente * pow(valorX, expoente)
            if termoTemX:
                valorTermo = int(coeficiente) * pow(valorX, int(expoente))
            else: 
                valorTermo = int(coeficiente)
            # print('valorTermo', valorTermo)
            resultado = resultado + valorTermo
        respostasPolinomio.append(resultado)
            # if
    print(f"Caso {indexCaso+1}: ", end='')
    for iResp, resposta in enumerate(respostasPolinomio, 1):
        if iResp == qtdValoresX : #ultimo
            print(resposta)
        else: 
            print(resposta, end=' ')

# 2
# 3x5+x3-2x-1
# 4
# 0 1 2 3