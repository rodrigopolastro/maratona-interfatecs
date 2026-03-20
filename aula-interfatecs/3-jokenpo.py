pontosBeatriz = 0
pontosArtur = 0

PEDRA   = '*'
PAPEL   = 'O'
TESOURA = 'V'

while True:
    entradaDados = input().split()
    beatriz = entradaDados[0] 
    artur = entradaDados[1]
    
    if beatriz == artur == '-':
        break
    if beatriz == PEDRA:
        if artur == TESOURA:
            pontosBeatriz += 1
        elif artur == PAPEL:
            pontosArtur += 1
    elif beatriz == TESOURA:
        if artur == PAPEL:
            pontosBeatriz += 1
        elif artur == PEDRA:
            pontosArtur += 1
    elif beatriz == PAPEL:
        if artur == PEDRA:
            pontosBeatriz += 1
        elif artur == TESOURA:
            pontosArtur += 1
    
if pontosBeatriz > pontosArtur:
    print('BEATRIZ WIN')
elif pontosArtur > pontosBeatriz:
    print('ARTUR WIN')
else:
    print('TIE')