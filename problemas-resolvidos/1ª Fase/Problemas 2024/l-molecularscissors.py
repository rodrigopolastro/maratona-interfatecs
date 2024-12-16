palavraOriginal = ""
while palavraOriginal != "EOF":
    palavraOriginal = input().upper()
    # 1 - A // 2 - G // 3 - C // 4 - T
    cod_reverso = palavraOriginal.replace('A','1').replace('G','2').replace('C','3').replace('T','4').replace('4','A').replace('2','C').replace('3','G').replace('1','T')

    ponteiro1 = 0
    ponteiro2 = ponteiro1 + 1
    maiorPalavra = 0
    resultado = tuple() # meio desnecessário

    while True:
        if ponteiro2 > len(palavraOriginal):
            break
        if cod_reverso[ponteiro1:ponteiro2][::-1] in palavraOriginal:
            if len(cod_reverso[ponteiro1:ponteiro2]) > maiorPalavra:
                maiorPalavra = len(cod_reverso[ponteiro1:ponteiro2])
                resultado = (ponteiro1+1,ponteiro2)
                
            ponteiro2+=1
        else:
            ponteiro1 +=1 
            ponteiro2 = ponteiro1+3
        
    if maiorPalavra < 3:
        print('false')
    else:
        print(resultado[0],maiorPalavra)    
        
