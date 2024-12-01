import string

ordem = string.ascii_uppercase+string.ascii_lowercase

output = [['*']]

quantidadeCampos = int(input())

def preencher(index):
    fillLetter = ordem[index]
    colunaSuperior = [fillLetter for i in range(len(output)+2)]
    colunaInferior = [fillLetter for i in range(len(output)+2)]
    for linhas in output:
        linhas.insert(0,fillLetter)
        linhas.append(fillLetter)
    output.insert(0,colunaSuperior)
    output.append(colunaInferior)
    
for i in range(quantidadeCampos-1,-1,-1):
    preencher(i)
for i in output:
    print(*i)