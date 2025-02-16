# versão tentando ordenar manualmente - falha
def determinarPontuacao(lista):
    # formato:
    # Gabriel Torres;N;650;N;N;N
    # ... / 10.000.000 - x * 10 + 3 + 2 + 1
    retornarPontuacaoGeral = 0
    if lista[1] == 'S':
        retornarPontuacaoGeral += 100_000_000_000
    retornarPontuacaoGeral -= int(lista[2]) * 100000
    if lista[3] == 'S':
        retornarPontuacaoGeral += 10000
    if lista[4] == 'S':
        retornarPontuacaoGeral +=1000
    if lista[5] == 'S':
        retornarPontuacaoGeral += 100
    return retornarPontuacaoGeral
dados = []

valorLetra = {
    'a':'01',
    'b':'02',
    'c':'03',
    'd':'04',
    'e':'05',
    'f':'06',
    'g':'07',
    'h':'08',
    'i':'09',
    'j':'10',
    'k':'11',
    'l':'12',
    'm':'13',
    'n':'14',
    'o':'15',
    'p':'16',
    'q':'17',
    'r':'18',
    's':'19',
    't':'20',
    'u':'21',
    'v':'22',
    'w':'23',
    'x':'24',
    'y':'25',
    'z':'26',
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9',
    '0':'0',
    '-':'0',
    '.':'0',
    ' ':'0'
} 
import decimal

decimal.getcontext().prec(60)

def determinarNumero(nome:str, limite = 60):
    nome = nome.lower()
    retornar = ''
    for letra in nome:
        # if letra == ' ':
        #     pass
        # else:
            retornar += valorLetra[letra]
    while len(retornar) < limite:
        retornar+='0'
    retorno = '0.'+retornar
    return decimal(retorno)
    
    
try:
    while True:
        dadoEntrada = input().split(';')
        nome = dadoEntrada[0].lower().replace('á','a').replace('â','a').replace('ã','a').replace('õ','o').lower()
        dados.append(dadoEntrada)
        
        
        
except EOFError:
    respostas = []
    listaTemporaria = []
    for dado in dados:
        dado.append(determinarPontuacao(dado))
        listaTemporaria.append(dado)
    organizarResultado = sorted(listaTemporaria, key=lambda x: (-x[7], x[0]))
    
    # organizarResultado.reverse()
    posicao = 0
    ultimoAnalisado = None
    for classificacao in organizarResultado:
        
        if int(classificacao[7]) == ultimoAnalisado:
            respostas.append(f"{posicao} {classificacao[0]}")
        else:
            posicao+=1
            respostas.append(f"{posicao} {classificacao[0]}")
            ultimoAnalisado = int(classificacao[7])
    for r in respostas:
        print(r)


# def determinarPontuacao(lista):
#     # formato:
#     # Gabriel Torres;N;650;N;N;N
#     # ... / 10.000.000 - x * 10 + 3 + 2 + 1
#     retornarPontuacaoGeral = 0
#     if lista[1] == 'S':
#         retornarPontuacaoGeral += 100_000_000_000
#     retornarPontuacaoGeral -= int(lista[2]) * 100000
#     if lista[3] == 'S':
#         retornarPontuacaoGeral += 10000
#     if lista[4] == 'S':
#         retornarPontuacaoGeral +=1000
#     if lista[5] == 'S':
#         retornarPontuacaoGeral += 100
#     return retornarPontuacaoGeral
# dados = []

# try:
#     while True:
#         dadoEntrada = input().split(';')
#         nome = dadoEntrada[0].lower().replace('á','a').replace('â','a').replace('ã','a').replace('õ','o').lower()
#         dados.append(dadoEntrada)
        
        
        
# except EOFError:
#     respostas = []
#     listaTemporaria = []
#     for dado in dados:
#         dado.append(determinarPontuacao(dado))
#         listaTemporaria.append(dado)
#     organizarResultado = sorted(listaTemporaria, key=lambda x: (-x[6], x[0]))
    
#     # organizarResultado.reverse()
#     posicao = 0
#     ultimoAnalisado = None
#     for classificacao in organizarResultado:
        
#         if int(classificacao[6]) == ultimoAnalisado:
#             respostas.append(f"{posicao} {classificacao[0]}")
#         else:
#             posicao+=1
#             respostas.append(f"{posicao} {classificacao[0]}")
#             ultimoAnalisado = int(classificacao[6])
#     for r in respostas:
#         print(r)
            
            

    
            
            

    