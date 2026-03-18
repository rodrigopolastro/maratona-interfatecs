jog,pas = [int(x) for x in input().split()]

jogadores = [ i for i in range(1,jog+1)]

ponteiro = -1
movimentou = 0
while len(jogadores) != 1:
    movimentou +=1
    ponteiro +=1
    if ponteiro >= len(jogadores):
        ponteiro = 0
    if movimentou == pas:
        # print(ponteiro)
        # print(jogadores)
        removido = jogadores.pop(ponteiro)
        # print(removido)
        movimentou = 0
        ponteiro -=1
print(jogadores[0])