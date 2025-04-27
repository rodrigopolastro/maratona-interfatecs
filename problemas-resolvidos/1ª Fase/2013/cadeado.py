#3:18 - 3:38
def avancarCima(num,obj):
    ordem = '0123456789'
    quantidadeMudancas = 0 
    index = ordem.index(num)
    for _ in range(index+1,index+11):
        quantidadeMudancas +=1
        if ordem[_%10] == obj:
            return quantidadeMudancas
       
def avancarBaixo(num,obj):
    ordem = '9876543210'
    quantidadeMudancas = 0 
    index = ordem.index(num)
    for _ in range(index+1,index+11):
        quantidadeMudancas +=1
        if ordem[_%10] == obj:
            return quantidadeMudancas
        
        
while True:
    entrada = input().strip()
    if entrada == '0':
        break
    numLetras,senha,atual = [x for x in entrada.split()]
    resposta = []
    for _ in range(int(numLetras)):
        if atual[_] == senha[_]:
            resposta.append('0')
        else:
            if avancarCima(atual[_],senha[_]) <= avancarBaixo(atual[_],senha[_]):
                resposta.append('1'*avancarCima(atual[_],senha[_]))
            else:
                resposta.append('-1'*avancarBaixo(atual[_],senha[_]))
    print(*resposta)