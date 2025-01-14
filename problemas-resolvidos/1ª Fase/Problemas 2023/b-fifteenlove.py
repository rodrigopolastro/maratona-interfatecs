# OBJETIVO: Determinar placar do jogo de acordo com sequencia de pontuação
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
def outroJogador(numero):
    if numero == 1:
        return 0
    return 1
def ganhaGame(vencedor):
    global jogadorSacando
    global TieBreak
    games[vencedor] += 1
    if games[vencedor] == 6 or games[vencedor] == 7:
        if games[vencedor] - games[outroJogador(vencedor)] >= 2:
            sets[vencedor] += 1
            if sets[vencedor] == 3: 
                if sets[0] == 3:
                    print(f"{sets[0]}({games[0]})[GAME]"+         "-" +f"{sets[1]}({games[1]})[{pontos[1]}]")
                    quit()
                else:
                    print(f"{sets[0]}({games[0]})[{pontos[0]}]"+  "-" +f"{sets[1]}({games[1]})[GAME]")
                    quit()
            games[vencedor] = 0
            games[outroJogador(vencedor)] = 0
        elif games[outroJogador(vencedor)] == 6:
            TieBreak = True
    pontos[vencedor] = 0
    pontos[outroJogador(vencedor)] = 0  
    jogadorSacando = outroJogador(jogadorSacando) 
numeroPontos = int(input())
entradaPontos = input()
loop = 0          
for ponto in entradaPontos:
    pontos[jogadorSacando] += int(ponto == 'W')
    pontos[outroJogador(jogadorSacando)] += int(ponto != 'W')
    if TieBreak:    
        if pontos[jogadorSacando] >= 7 and pontos[jogadorSacando] - pontos[outroJogador(jogadorSacando)] >= 2:
            ganhaGame(jogadorSacando) 
            TieBreak = False
        elif pontos[outroJogador(jogadorSacando)] >= 7 and pontos[outroJogador(jogadorSacando)] - pontos[jogadorSacando] >= 2:
            ganhaGame(outroJogador(jogadorSacando))
            TieBreak = False
    else:
        #voltou o jogo para "deuce"
        if pontos[jogadorSacando] == pontos[outroJogador(jogadorSacando)] == 4: 
            pontos[jogadorSacando] -= 1
            pontos[outroJogador(jogadorSacando)] -= 1

        elif pontos[jogadorSacando] >= 4 and pontos[jogadorSacando] - pontos[outroJogador(jogadorSacando)] >= 2:
            ganhaGame(jogadorSacando) 
            
        elif pontos[outroJogador(jogadorSacando)] >= 4 and pontos[outroJogador(jogadorSacando)] - pontos[jogadorSacando] >= 2:
            ganhaGame(outroJogador(jogadorSacando))  
print(f"{sets[0]}({games[0]})[{SEQUENCIA_PONTOS[pontos[0]]}]"+ "-" +f"{sets[1]}({games[1]})[{SEQUENCIA_PONTOS[pontos[1]]}]")

