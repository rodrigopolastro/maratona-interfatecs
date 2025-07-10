# fim 21:13
linhas = list()
qtdLinhas = 0
try:
    while True:
        l = input()
        # if l == 'x':
        #     raise EOFError
        qtdLinhas += 1
        linhas.append(list(l))
except EOFError:
    QTD_COLUNAS = len(linhas[0])
    primeiro, segundo, terceiro = linhas[0][:3]
    if primeiro == segundo:
        padrao = primeiro
    else:
        if primeiro == terceiro:
            #segundo é o diferente
            print('LINHA 1 COLUNA 2')
            exit()
        else: #segundo == terceiro
            print("LINHA 1 COLUNA 1")
            exit()
            
    for i in range(qtdLinhas):
        for j in range(QTD_COLUNAS):
            if linhas[i][j] != padrao:
                print(f"LINHA {i+1} COLUNA {j+1}")
