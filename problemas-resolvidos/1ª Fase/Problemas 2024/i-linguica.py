qtdeNumeros = int(input())
arvoreReta = [None]
for numero in range(qtdeNumeros):
    arvoreReta.append(int(input()))
if arvoreReta[1] < arvoreReta[2] and arvoreReta[1] < arvoreReta[3]:
    padrao = 1 # crescente   
elif arvoreReta[1] > arvoreReta[2] and arvoreReta[1] > arvoreReta[3]:
    padrao = 2 # decrescente
else:
    padrao = 0
if padrao == 0:
    print(padrao)
else:
    for indexes in range(1,len(arvoreReta)+1):
        try:
            if padrao == 1:
                if arvoreReta[indexes] > arvoreReta[indexes * 2] or arvoreReta[indexes] > arvoreReta[(indexes * 2)+1]:
                    padrao = 0
                    break
            # erro muito estranho com 'if padrao == 1 and arvoreReta[indexes] > arvoreReta[indexes * 2] or arvoreReta[indexes] > arvoreReta[(indexes * 2)+1]:'
            # mesmo que padrao equivale a 2 ele eentra nesse loop, deve ser algum erro local
            elif padrao == 2:
                if arvoreReta[indexes] < arvoreReta[indexes * 2] or arvoreReta[indexes] < arvoreReta[(indexes * 2)+1]:
                    padrao = 0
                    break
        except:
            pass
    print(padrao)