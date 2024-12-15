listaJogadores = []
QtdeJogadores = int(input())
for jogadores in range(QtdeJogadores):
    listaJogadores.append([input(),0])
rodadas = int(input())
for rodada in range(rodadas):
    totalNaMao = sum(list(map(int,input().split(' '))))
    tentativaJogadores = list(map(int,input().split(' ')))
    PonteiroParaMaoDoVencedor = 0
    for indexMaoJogador in range(len(tentativaJogadores)):
        if tentativaJogadores[indexMaoJogador] == totalNaMao:
            PonteiroParaMaoDoVencedor = indexMaoJogador
            listaJogadores[PonteiroParaMaoDoVencedor][1]+=1
            break
resultado = sorted(listaJogadores,key=lambda x: x[1],reverse=True)
if resultado[0][1] == resultado[1][1]:
    print('EMPATE')
else:
    print(f"{resultado[0][0]} GANHOU")

