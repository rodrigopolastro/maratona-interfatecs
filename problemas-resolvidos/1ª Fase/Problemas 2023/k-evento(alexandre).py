################################################################################
# Objetivo: Determinar se é possível viajar entre quaisquer dois pontos em uma 
#           cidade a partir das conexões entre os pontos da mesma. Tecnicamente, 
#           trata-se de verificar se um grafo direcionado é conexo.
# Autor: Alexandre
# Data: 20/01/2025
# Duração: 1h 09m
################################################################################
# inicio 20:25 -> término 21:34
while True:
    pontos , ruas =list(map(int,input().split()))
    if pontos == 0 and ruas == 0:
        break
    caminhos = [None]
    for i in range(pontos):
        caminhos.append([])

    for i in range(ruas):
        entrada = list(map(int,input().split()))
        caminhos[entrada[0]].append(entrada[1])
        if entrada[2] == 2:
            caminhos[entrada[1]].append(entrada[0])
    qtdeWays = len(caminhos) - 1
    semMovimento = 0
    while True:
        if semMovimento == qtdeWays:
            break
        else:
            for ways in range(1,len(caminhos)):
                antesAdicao = len(list(set(caminhos[ways])))
                for item in caminhos[ways]:                   
                    caminhos[ways].extend(caminhos[item])
                    caminhos[ways] = list(set(caminhos[ways]))
                    if len(caminhos[ways]) == qtdeWays:
                        break
                depoisAdicao = len(list(set(caminhos[ways])))
                if antesAdicao == depoisAdicao:
                    semMovimento +=1
                else:
                    semMovimento = 0
                if semMovimento == qtdeWays:
                    break
    printarN = False
    for item in range(1,len(caminhos)):
        if len(caminhos[item]) < pontos:
            printarN = True
    if printarN:
        print("N")
    else:
        print("S")
        
    
        