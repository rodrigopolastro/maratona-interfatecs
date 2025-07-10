# inicio: 19:55
# Data: 09/04/2025
# Objetivo: 
# O problema consiste em encontrar a menor sequência de rotações que devem ser 
# realizadas para cada  dígito do cadeado para que no final a configuração do 
# cadeado seja igual a da senha. Caso haja um empate no número de rotações 
# (o mesmo número de rotações tanto para cima quanto para baixo), a rotação 
# para cima deve ser escolhida.

while True:
    entrada = input().split()
    qtdDigitos =  int(entrada[0])
    if qtdDigitos == 0:
        break
    senhaFinal, senhaInicial = entrada[1], entrada[2]
    
    strDiferencas = ''
    for i in range(qtdDigitos):
        diferenca = int(senhaFinal[i]) - int(senhaInicial[i])
        if diferenca >= 6:
            diferenca = -(10 - diferenca)
        elif diferenca <= -6:
            diferenca = 10 + diferenca
            
        #sempre prioriza movimentos apra cima, conforme enunciado
        if diferenca == -5:
            diferenca = 5 
            
        if diferenca > 0:    
            strDiferencas += '1' * diferenca
        elif diferenca < 0:
            strDiferencas += '-1' * abs(diferenca)
        else:
            strDiferencas += '0'

        if i != qtdDigitos-1:
            strDiferencas += ' '
        
    print(strDiferencas)