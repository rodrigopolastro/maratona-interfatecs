QTD_ELEMENTOS = 999
pai = [i for i in range(QTD_ELEMENTOS)]
peso = [0] * QTD_ELEMENTOS
tamanhoConjunto = [1] * QTD_ELEMENTOS
qtdComponentes = QTD_ELEMENTOS

def find(a):
    if pai[a] == a:
        return a
    patriarca = find(pai[a])
    pai[a] = patriarca
    return patriarca

def union(a, b):
    global qtdComponentes
    paiA = find(a)
    paiB = find(b)
    
    if paiA == paiB:
        return
    qtdComponentes -= 1
    
    if peso[paiA] < peso[paiB]: 
        pai[paiA] = paiB
        tamanhoConjunto[paiB] += tamanhoConjunto[paiA]
    elif peso[paiB] < peso[paiA]: 
        pai[paiB] = paiA
        tamanhoConjunto[paiA] += tamanhoConjunto[paiB]
    else: 
        pai[paiA] = paiB
        peso[paiB] += 1  
        tamanhoConjunto[paiB] += tamanhoConjunto[paiA]
        
        
        
        
        
        
        
        