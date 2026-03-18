# qtdJogadores, passo = [int(_) for _ in input().split()]
# jogadores = [i for i in range(1, qtdJogadores+1)]

# ponteiro = 0
# movimentosPonteiro = 0
# jogadoresRestantes = qtdJogadores

# while jogadoresRestantes > 1:
#     ponteiro += 1
#     print('ponteiro: ', ponteiro)
#     print('restantes', jogadoresRestantes)
#     movimentosPonteiro += 1
#     if ponteiro > jogadoresRestantes:
#         ponteiro = 0
#     if movimentosPonteiro == passo:
#         movimentosPonteiro = 0
#         jogadores.pop(ponteiro-1)
#         jogadoresRestantes -= 1
#         # ponteiro += 1
#     print(jogadores)
        
    
    # if ponteiro > jogadoresRestantes:
    
    
    
    
jogadores,queimada = [int(x) for x in input().split()]


jogadores = [i for i in range(1,jogadores)]
ponteiro = 0
queimou = 0
while len(jogadores) != 1:
    print(ponteiro)
    print(queimou)
    
    ponteiro +=1
    queimou +=1 
    if ponteiro >= len(jogadores):
        ponteiro = 0
    if queimou+1 == queimada:
        
        jogadores.pop(ponteiro)
        # ponteiro -= 1
        # if ponteiro < 0:
        #     ponteiro = len(jogadores)-1
        queimou = 0
        
print(jogadores[0])
        