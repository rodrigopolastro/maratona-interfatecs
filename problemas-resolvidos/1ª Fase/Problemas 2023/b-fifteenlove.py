################################################################################
# Objetivo: Determinar placar do jogo de tênis de acordo com sequencia de pontuação
# Autor: Rodrigo e Alexandre
# Data: 14/01/2025
# Duração: 3h+
################################################################################

# REGRAS
# - ganha a partida quem fizer 3 sets
# - ganha um set quem fizer 6 games
# - ganha um game quem fizer a sequência [0 - 15 - 30 - 40 - GAME]
#   - se empatar em 40, quem fizer dois seguidos ganha (fica com ADV)
# se chega a 6 a 6 games, tem um tie-break
#   - no tie-break, quem fizer 7 pontos ganha (2 pontos de diferença)
#   - no tie-break os pontos são sequenciais (1 a 7)
# SAQUES
# - cada game um jogador saca
# - o W e L do caso de teste representa ponto do jogador que saca ou do outro (resp.)
# - no tie-break os saques alternam a cada dois pontos, começando por quem recebeu no jogo anterior

SEQUENCIA_PONTOS = ['0', '15', '30', '40', 'ADV']
jogadorSacando = 0
pontos = [ 0 , 0 ]
games = [ 0 , 0 ]
sets = [ 0 , 0 ]
TieBreak = False
jogadorQueSacaAposTiebreak = None
pontosNoTieBreak = 0

def outroJogador(numero):
    if numero == 1:
        return 0
    return 1

def ganhaGame(vencedor):
    global jogadorSacando
    global TieBreak
    global pontosNoTieBreak
    global jogadorQueSacaAposTiebreak
    games[vencedor] += 1

    if TieBreak == True:
        TieBreak = False
        jogadorSacando = jogadorQueSacaAposTiebreak
    else:
        jogadorSacando = outroJogador(jogadorSacando)

    if games[vencedor] == 6 and games[vencedor] - games[outroJogador(vencedor)] >= 2 or games[vencedor] == 7:
        sets[vencedor] += 1
        if sets[vencedor] == 3:
            if TieBreak:
                pontosJog1 = pontos[0]
                pontosJog2 = pontos[1]
            else:
                if pontos[0] <= 4:
                    pontosJog1 = SEQUENCIA_PONTOS[pontos[0]]
                elif pontos[1] <= 4:
                    pontosJog2 = SEQUENCIA_PONTOS[pontos[1]]

            if sets[0] == 3:

                print(f"{sets[0]}({games[0]})[GAME]"+          "-" +f"{sets[1]}({games[1]})[{pontosJog2}]")
                quit()
            else:
                print(f"{sets[0]}({games[0]})[{pontosJog1}]"+  "-" +f"{sets[1]}({games[1]})[GAME]")
                quit()
        games[vencedor] = 0
        games[outroJogador(vencedor)] = 0
    elif games[vencedor] == games[outroJogador(vencedor)] == 6:
        TieBreak = True
        pontosNoTieBreak = 0
        jogadorQueSacaAposTiebreak = outroJogador(jogadorSacando)

    pontos[vencedor] = 0
    pontos[outroJogador(vencedor)] = 0

numeroPontos = int(input())
entradaPontos = input()

for ponto in entradaPontos:
    pontos[jogadorSacando] += int(ponto == 'W')
    pontos[outroJogador(jogadorSacando)] += int(ponto != 'W')

    if TieBreak:
        pontosNoTieBreak += 1

        if pontos[jogadorSacando] >= 7 and pontos[jogadorSacando] - pontos[outroJogador(jogadorSacando)] >= 2:
            ganhaGame(jogadorSacando)
        elif pontos[outroJogador(jogadorSacando)] >= 7 and pontos[outroJogador(jogadorSacando)] - pontos[jogadorSacando] >= 2:
            ganhaGame(outroJogador(jogadorSacando))
        elif pontosNoTieBreak == 1 :
            jogadorSacando = outroJogador(jogadorSacando)
        elif (pontosNoTieBreak+1) % 2 == 0:
            jogadorSacando = outroJogador(jogadorSacando)
    else:
        #voltou o jogo para "deuce"
        if pontos[jogadorSacando] == pontos[outroJogador(jogadorSacando)] == 4  :
            pontos[jogadorSacando] -= 1
            pontos[outroJogador(jogadorSacando)] -= 1

        elif pontos[jogadorSacando] >= 4 and pontos[jogadorSacando] - pontos[outroJogador(jogadorSacando)] >= 2:
            ganhaGame(jogadorSacando)

        elif pontos[outroJogador(jogadorSacando)] >= 4 and pontos[outroJogador(jogadorSacando)] - pontos[jogadorSacando] >= 2:
            ganhaGame(outroJogador(jogadorSacando))

if TieBreak:
    print(f"{sets[0]}({games[0]})[{pontos[0]}]"+ "-" +f"{sets[1]}({games[1]})[{pontos[1]}]")
else:
    print(f"{sets[0]}({games[0]})[{SEQUENCIA_PONTOS[pontos[0]]}]"+ "-" +f"{sets[1]}({games[1]})[{SEQUENCIA_PONTOS[pontos[1]]}]")

