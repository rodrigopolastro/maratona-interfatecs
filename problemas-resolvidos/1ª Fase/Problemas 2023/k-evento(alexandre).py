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
                depoisAdicao = len(list(set(caminhos[ways])))
                if antesAdicao == depoisAdicao:
                    semMovimento +=1
                else:
                    semMovimento = 0
                if semMovimento == qtdeWays:
                    break
                    
                    
            # encaixouFor = False
            # for listaResultado in range(1,len(caminhos)+1):
            #     Checked = set()
            #     # for item in caminhos[listaResultado]:
            #     for caminhosNumero in range(1,pontos+1): 
            #         if caminhosNumero in caminhos[listaResultado] and caminhosNumero not in Checked:
            #             caminhos[listaResultado].add(caminhosNumero)
            #             Checked.add(caminhosNumero)
            #             encaixouFor = True
            # if encaixouFor == False:
            #     semMovimento +=1
            # else:
            #     semMovimento = 0
    printarN = False
    for item in range(1,len(caminhos)):
        if len(caminhos[item]) < pontos:
            printarN = True
         
    if printarN:
        print("N")
    else:
        print("S")
        
    
        