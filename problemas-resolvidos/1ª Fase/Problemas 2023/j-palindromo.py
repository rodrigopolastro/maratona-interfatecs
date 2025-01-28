################################################################################
# Objetivo: recebe um texto e retorna se esse texto é um palindromo ou não
# OBS: ao fato de termos os casos de teste, esse problema é bem estranho em
# consideração há algumas pontuações, basicamente você tem que interpretar 
# peso de caracteres especiais (! , . #) no meio do código tem peso, 
# enquanto no final não (?)
# Autor: Alexandre
# Data: 27/01/2025
# Duração: ?
################################################################################

# from unicodedata import normalize,category,combining
# print([c for c in normalize('NFD', stringNormal) if not combining(c)])

stringNormal = None
while stringNormal != '':
    stringNormal = input().lower().replace('-','').replace(',','').replace('!','').replace('?','').replace(' ','').replace("á","a").replace("ã","a").replace("â","a").replace("é","e").replace("ê","e").replace("í","î").replace("ó","o").replace("õ","o").replace("ô","o").replace("ú","u").replace("û","u").replace("ç","c")
    if stringNormal[-1] == '.':
        stringNormal = stringNormal.replace('.','')
    stringNormalFormatada = ''
    for caractere in stringNormal:
        stringNormalFormatada+=caractere
            
    stringInvertida = stringNormalFormatada[::-1]

    
    if stringNormalFormatada == stringInvertida:
        print("Parabens, voce encontrou o Palindromo Perdido!")
    else:
        print("A busca continua, o Palindromo Perdido ainda nao foi encontrado.")

        
