componentes = int(input())
ent = []
for _ in range(componentes):
    ent.append(input().split(maxsplit=4))
tamPix = int(input())

altura,largura = 0,0
for c in ent:
    altura += int(c[0])
    if c[2] == 'MATCHPARENT' or c[2] == 'WRAPCONTENT':
        # print('entrou\nlarg = ',largura,'\ntamanho = ',len(c[4]) * tamPix)
        largura = max(largura,len(c[4]) * tamPix)
    else:
        largura = max(largura,int(c[2]))
    
print(altura)
# print(largura)
for r in ent:
    if largura == 0:
        print(0,0)
    else:
        if r[1] == 'A':
            tamanho = int(r[2])
            if largura - tamanho > 0:
                # print('tamanho: ',tamanho)
                
                if r[3] == 'D':
                    # print('caso 1')
                    print(int(largura - tamanho), 0 )
                elif r[3] == 'E':
                    # print('caso 2')
                    print(0,int(largura - tamanho))
                else:
                    # print('caso 3')
                    print(int((largura-tamanho)/2),int((largura-tamanho)/2))
            else:
                print(0,0)
        elif r[2] == 'MATCHPARENT':
            # print('caso 4')
            print(0,0)
        else:
            # wrapcontent
            tamanhoComp = tamPix * len(r[4])
            # print('tamanhoComp = ',tamanhoComp)
            if tamanhoComp >= largura:
                print(0,0)
            else:
                if r[3] == 'D':
                    # print('caso 5')
                    print(int(largura - tamanhoComp), 0 )
                elif r[3] == 'E':
                    # print('caso 6')
                    print(0,int(largura - tamanhoComp))
                else:
                    # print('caso 7')
                    print(int((largura-tamanhoComp)/2),int((largura-tamanhoComp)/2))
            
        