################################################################################
# Objetivo: Dada uma lista de pessoas e uma relação que determina quais delas se conhecem, 
#           retorna uma lista de convidados que conhecem no mínimo N outros
#           que também irão à festa.
# Autor: Rodrigo e Alexandre
# Data: 30/01/2025
# Duração: 
#  - para resolver 60/100  asos de teste: 18min
#  - para resolver 99/100 casos de teste: 4h18min 
#  - para resolver 100/100 casos de teste: MAIS DE 8 MIL
################################################################################

# OBS: Baita exercício sem alma. 
#      De início, calculamos apenas as pessoas que conheciam N ou mais pessoas 
#      da lista dos convidados, mas, na verdade, era preciso ir filtrando essas
#      listas mais e mais. 

while True:
    qtdPessoas, qtdRelacoes, qtdMinConhecidos = [int(_) for _ in input().split()]
    if qtdPessoas == 0:
        break
    
    relacoes = dict()
    for numeroPessoa in range(1, qtdPessoas+1):
        relacoes[numeroPessoa] = set()
    
    for _ in range(qtdRelacoes):
        numPessoa1, numPessoa2 = [int(_) for _ in input().split()]
        relacoes[numPessoa1].add(numPessoa2)
        relacoes[numPessoa2].add(numPessoa1)
            
    pessoasQualificadas = []
    for pessoa in range(1, qtdPessoas+1):
        if len(relacoes[pessoa]) >= qtdMinConhecidos:
            pessoasQualificadas.append(pessoa)
    
    while True:
        novaLista = []
        for pessoa in range(1, qtdPessoas+1):
            conhecidosQualificados = [p for p in relacoes[pessoa] if p in pessoasQualificadas]
            if len(conhecidosQualificados) >= qtdMinConhecidos:
                novaLista.append(pessoa)
        
        if len(novaLista) == len(pessoasQualificadas):
            break
        
        pessoasQualificadas = novaLista    
        
    for pessoa in pessoasQualificadas:
        print(pessoa)   