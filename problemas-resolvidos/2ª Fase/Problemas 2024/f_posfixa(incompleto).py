dicionario = {
    '+' : 1,
    '-' : 1,
    '/' : 2,
    '*' : 2,
    '^' : 3,
}

def forstring(string):
    ordem_pri = []
    letras = []
    operadores = []
    i = 0
    while i < len(string):
        
        if string[i] == '(':
            
            letras.append(string[i+1])
            ordem_pri.append(dicionario[string[i+2]]+5)
            operadores.append(string[i+2])
            letras.append(string[i+3])
            i+=5
        
        elif string[i] in dicionario.keys():
            ordem_pri.append(dicionario[string[i]])
            operadores.append(string[i])
            i+=1
        else:
            letras.append(string[i])
            i+=1
    # print(ordem_pri)
    # print(letras)
    # print(operadores)
    if ordem_pri == sorted(ordem_pri):
        print(f"{''.join(letras)}{''.join(reversed(operadores))}")
    elif ordem_pri == list(reversed(sorted(ordem_pri))):
        retornar = ''.join(letras[0:2])
        letras.pop(0)
        letras.pop(0)
        for i in range(len(letras)):
            retornar+=operadores[i]
            retornar+=letras[i] 
        retornar+=operadores[-1]
        print(retornar)
    else:
        while ')' in letras or '(' in letras:
            for i in letras:
                if i == ')' or i == '(':
                    letras.remove(i)
        comeco = letras[0]
        letras.pop(0)
        
            
        # for i in range(len(ordem_pri)):
        i = 0
        while i < len(ordem_pri):
            caminho = 0
            # print(i, ' ', len(ordem_pri))
            # i+=1
            if i < len(ordem_pri):
                caminho = 1
                if ordem_pri[i] > ordem_pri[i+1]:
                    comeco+=letras[i]+operadores[i]
                    # i-=1
                    letras.pop(0)
                    operadores.pop(0)
                    ordem_pri.remove(ordem_pri[i])
                    # i-=1
                    
                    # print(operadores)
                    # print(letras)
                    # print(ordem_pri)
                else:
                # i += 1
                    ordem_pri.insert(-1,ordem_pri[0])
                    ordem_pri.pop()
            else:
                # i += 1
                ordem_pri.insert(-1,ordem_pri[0])
                ordem_pri.pop()
                while True:
                   
                    if '^' in operadores:
                        comeco+='^'
                        operadores.remove('^')
                    elif '*' in operadores or '/' in operadores:
                        for i in operadores:
                            if i == '*' or i =='/':
                                comeco+=i
                                operadores.remove(i)
                                break
                    else:
                        comeco+=''.join(operadores)
                        print(comeco)
                        return
                
                    
            if caminho == 1:
                # i+=1
                try:
                    comeco+=letras[i]
                    letras.pop(0)
                    i-=1
                except:
                    if ordem_pri == sorted(ordem_pri):
                        comeco+=''.join(reversed(operadores))
                    else:
                        comeco+= ''.join(operadores)
                    print(comeco)
                    return
                i += 1
            else:
                i+=1
                pass
                
        print(comeco)          
        
while True:
    entrada = input()
    if entrada == '.':
        break
    else:
        forstring(entrada)
            