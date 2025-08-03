jogadores , papel, comeca = [int(x) for x in input().split()]

jogRemovidos = 0
ponteiro = comeca
queimada = papel  * 2
listaJog = [_ for _ in range(jogadores)]

while True:
    queimada -= 1
    ponteiro -= 1
    if ponteiro < 0:
        ponteiro = len(listaJog) - 1
    if queimada == 0:
        listaJog.pop(ponteiro)
        jogRemovidos += 1
        queimada = (papel * 2) + (jogRemovidos * 2)
        if ponteiro > len(listaJog) - 1:
            ponteiro = 0
    if len(listaJog ) == 1:
        break
print(listaJog[0]) 