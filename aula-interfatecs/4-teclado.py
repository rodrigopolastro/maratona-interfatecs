# tipagem apenas para facilitar o intelisense e aparecer as builtin functions de string
def numero_tecla(tecla: str):
    if tecla.upper() in 'ABC':  # se atentar ao UPPER, mesmo que no enunciado fale q é maiuscula, não custa nada garantir pois já pegamos casos que o caso de teste estava errado
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
respostas = []  # apenas para o output ficar agrupado e mais facil de conferir
for palavra in range(palavras):
    palavraEscrever = input()
    combinacaoNumericaFormada = ''
    for letra in palavraEscrever:
        combinacaoNumericaFormada += numero_tecla(letra)
    respostas.append(combinacaoNumericaFormada)
for resposta in respostas:  # explicar que o boca nao importa a ordem de output, só agrupei p ficar mais facil ver na hora
    print(resposta)
