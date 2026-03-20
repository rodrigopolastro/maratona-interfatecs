def numero_tecla(tecla : str):
    if tecla.upper() in 'ABC':
        return '2'
    
    if tecla.upper() in 'DEF':
        return '3'
    
    if tecla.upper() in 'GHI':
        return '4'
    
    if tecla.upper() in 'JKL':
        return '5'

    if tecla.upper() in 'MNO':
        return '6'
    
    if tecla.upper() in 'PQRS':
        return '7'
    
    if tecla.upper() in 'TUV':
        return '8'
    
    if tecla.upper() in 'XYZ':
        return '9'
    
    return '0'

palavras = int(input())
respostas = [] # apenas para o output ficar agrupado e mais facil de conferir
for palavra in range(palavras):
    palavraEscrever = input()
    palavraNumero = ''
    for letra in palavraEscrever:
        palavraNumero += numero_tecla(letra)
    respostas.append(palavraNumero)
for resposta in respostas:
    print(resposta)
        

    