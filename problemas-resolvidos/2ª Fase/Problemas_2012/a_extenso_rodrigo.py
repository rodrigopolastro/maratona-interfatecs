################################################################################
# Objetivo: Escrever uma lista de valores monetários em extenso
# Autor: Rodrigo
# Data: 10/07/2025
# Duração: 2 horas 
# (vergonha, eu sei... mas era o 1º exercício depois de muito tempo, dá um boi aí)
################################################################################

NOMES_UNIDADES = {
    '0': '',
    '1': 'UM',
    '2': 'DOIS',
    '3': 'TRES',
    '4': 'QUATRO',
    '5': 'CINCO',
    '6': 'SEIS',
    '7': 'SETE',
    '8': 'OITO',
    '9': 'NOVE',
}

NOMES_DEZ_AO_VINTE = {
    '11': 'ONZE',
    '12': 'DOZE',
    '13': 'TREZE',
    '14': 'QUATORZE',
    '15': 'QUINZE',
    '16': 'DEZESSEIS',
    '17': 'DEZESSETE',
    '18': 'DEZOITO',
    '19': 'DEZENOVE',
}

NOMES_DEZENAS = {
    '0': '',
    '1': 'DEZ',
    '2': 'VINTE',
    '3': 'TRINTA',
    '4': 'QUARENTA',
    '5': 'CINQUENTA',
    '6': 'SESSENTA',
    '7': 'SETENTA',
    '8': 'OITENTA',
    '9': 'NOVENTA',
}

NOMES_CENTENAS = {
    '0': '',
    '1': 'CENTO',
    '2': 'DUZENTOS',
    '3': 'TREZENTOS',
    '4': 'QUATROCENTOS',
    '5': 'QUINHENTOS',
    '6': 'SEISCENTOS',
    '7': 'SETECENTOS',
    '8': 'OITOCENTOS',
    '9': 'NOVECENTOS',  
}

def trataAte3(reais):
    strReais = ''
    qtdDigitos = len(reais)
    if qtdDigitos == 1:
        if reais != '0':
            strReais = NOMES_UNIDADES[reais]
    elif qtdDigitos == 2:
        if reais in NOMES_DEZ_AO_VINTE:
            strReais = NOMES_DEZ_AO_VINTE[reais]
        else:
            dezenas, unidades = reais[0], reais[1]
            strReais = NOMES_DEZENAS[dezenas]
            if unidades != '0':   
                if dezenas != '0':
                    strReais = strReais + ' E '
                strReais = strReais + NOMES_UNIDADES[unidades]
    elif qtdDigitos == 3:
        strReais = tresDigitos(reais)
        
    return strReais

def tresDigitos(reais):
    strReais = ''
    if reais == '100':
        strReais += 'CEM'
    else:
        centenas, dezenas, unidades = reais[0], reais[1], reais[2]
        strReais = strReais + NOMES_CENTENAS[centenas] + ' E '
        if dezenas == '0':
            strReais = strReais + NOMES_UNIDADES[unidades]
        else:
            doisUltimos = dezenas + unidades
            if doisUltimos in NOMES_DEZ_AO_VINTE:
                strReais = strReais + NOMES_DEZ_AO_VINTE[doisUltimos]
            else:
                strReais = strReais + NOMES_DEZENAS[dezenas]
                if unidades != '0':   
                    if dezenas != '0':
                        strReais = strReais + ' E '
                    strReais = strReais + NOMES_UNIDADES[unidades]
    return strReais

respostas = list()
while True: 
    valor = input()
    if float(valor) == 0.0:
        break
    
    reais, centavos = valor.split('.')
    reais = str(int(reais))
    if len(centavos) == 1:
        centavos = centavos + '0'
    
    # processar centavos:
    strCentavos = ''
    if centavos in NOMES_DEZ_AO_VINTE:
        strCentavos = NOMES_DEZ_AO_VINTE[centavos]
    else:
        dezenas, unidades = centavos[0], centavos[1]
        if dezenas != '0':
            strCentavos = NOMES_DEZENAS[dezenas]
        if unidades != '0':   
            if dezenas != '0':
                strCentavos = strCentavos + ' E '
            strCentavos = strCentavos + NOMES_UNIDADES[unidades]
            
    if centavos != '00':
        if centavos == '01':
            strCentavos = strCentavos + ' CENTAVO'
        else:
            strCentavos = strCentavos + ' CENTAVOS'
        
    # processar reais
    strReais = ''
    qtdDigitos = len(reais)
    if qtdDigitos in (1,2,3):
        if reais != '0':
            strReais = trataAte3(reais)
    elif qtdDigitos in (4,5,6):
        qtdAntes3 = qtdDigitos - 3
        tresPrimeiros, tresUltimos = reais[:qtdAntes3], reais[qtdAntes3:]
        strReais = strReais + trataAte3(tresPrimeiros) + ' MIL'
        if tresUltimos != '000':
            if tresUltimos[0] != '0':
                strReais = strReais + ' E '
            strReais = strReais + trataAte3(tresUltimos)
    elif qtdDigitos == 7:
        strReais = 'UM MILHAO DE'
        
    if int(reais) != 0:
      if reais == '1':
          strReais = strReais + ' REAL'
      else: 
          strReais = strReais + ' REAIS'
        
    strFinal = strReais
    if strCentavos != '':
        if int(reais) != 0:
            strFinal = strFinal + ' E '
        strFinal = strFinal + strCentavos
    
    respostas.append(strFinal)
    
for r in respostas: print(r)