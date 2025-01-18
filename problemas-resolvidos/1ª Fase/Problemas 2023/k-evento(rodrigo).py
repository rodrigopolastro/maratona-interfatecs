pontosVisitados = []
pontosCidade = None
ruasCidade = None

def dfs(numPonto):
    global pontosVisitados
    if pontosVisitados[numPonto] == True:
        return
    
    pontosVisitados[numPonto] = True
    for numConexao, haConexao in enumerate(conexoes[numPonto]):
        if haConexao is True:
            dfs(numConexao)
    
def testaCaminhos():
    for pontoInicial in range(pontosCidade):
        global pontosVisitados
        pontosVisitados = [False] * pontosCidade
        dfs(pontoInicial)
        if False in pontosVisitados:
            print("N") 
            return
             
    print("S")

while True:
    pontosCidade, ruasCidade = map(int,input().split(' '))
    if pontosCidade == ruasCidade == 0:
        break
    
    # Gera matriz de adjacências com todos os valores False
    conexoes = []
    for _ in range(pontosCidade):
        linha = list()
        for _ in range(pontosCidade):
            linha.append(False)
        conexoes.append(linha)
    
    # Preenche matriz de adjacências
    for _ in range(ruasCidade):
        a, b, tipoConexao = map(int,input().split(' '))
        if tipoConexao == 1:
            conexoes[a-1][b-1] = True
        else: 
            conexoes[a-1][b-1] = True
            conexoes[b-1][a-1] = True
            
    testaCaminhos()