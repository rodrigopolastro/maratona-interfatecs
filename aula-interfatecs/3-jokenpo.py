pontosBeatriz = 0
pontosArtur = 0

PEDRA   = '*'
PAPEL   = 'O'
TESOURA = 'V'
while True: # perguntar porque implementar while -- SE NAO RESPONDEREM, FAZER FUNÇÃO PRINCIPAL DE PONTUAÇÃO E DEPOIS VOLTA PARA ESSA PARTE
    entradaDados = input().split(' ') # mostrar para os alunos no texto que fala que o primeiro input é sempre da beatriz
    beatriz = entradaDados[0] 
    artur = entradaDados[1]
    
    if beatriz == '-' and artur == '-': 
        break
    if beatriz == PEDRA:
        if artur == TESOURA:
            pontosBeatriz += 1
        elif artur == PAPEL: # explicar que não precisa de else pois se der empate ninguem ganha nem perde ponto
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