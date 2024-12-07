entrada = input().split(' ')
carrinho = int(entrada[0])
produtos = int(entrada[1])
a,b,c = 0,1,2
dados = []
for i in range(produtos):
    dados.append(int(input()))
dados.sort()
while True:
    try:
        if carrinho+dados[a]+dados[b]+dados[c] == 200:
            print('fretegratis')
            break
        elif carrinho +dados[a]+dados[a+1]+dados[a+2] > 200:
            print('fretepago')
            break
        elif carrinho+dados[a]+dados[b]+dados[len(dados)-1]<200:
            raise IndexError
        elif a == len(dados) - 3:
            print('fretepago')
            break
        elif carrinho + dados[a]+dados[b]+dados[c] > 200:
            b+=1
            c =b+1

        else:
            c+=1
        
    except IndexError as e:
        
        a +=1 
        b = a + 1
        c = b + 1
