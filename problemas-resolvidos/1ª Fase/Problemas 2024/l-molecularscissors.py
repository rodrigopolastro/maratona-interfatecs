palavraOriginal = input().upper()
# 1 - A // 2 - G // 3 - C // 4 - T
cod_reverso = palavraOriginal.replace('A','1').replace('G','2').replace('C','3').replace('T','4').replace('4','A').replace('2','C').replace('3','G').replace('1','T')

ponteiro1 = 0
ponteiro2 = ponteiro1 + 3
maiorPalavra = 0
resultado = tuple()

# erro ao caso de teste AAGCTCAA, porém verificando manualmente não
# me parece que o meu codigo esteja errado e sim o caso de teste, então
# parte para o próximo tópico que pode ser que eu não tenha entendido corretamente
# porém ao caso de teste AAGCTCAA gera um 'complementary' que possui
# um palindromo de 4 ao invés de 3, vou verificar esse dado com outra pessoa
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
    print(resultado[0],resultado[1])    
        
    