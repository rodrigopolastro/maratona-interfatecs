# ENTRADA
primeira_linha = input().split(' ')
quantidade_linhas = int(primeira_linha[0]) # L
quantidade_colunas = int(primeira_linha[1]) # C
bateria = int(primeira_linha[2]) # B 3

segunda_linha = input().split(' ')
linha_atual = int(segunda_linha[0]) # X
coluna_atual = int(segunda_linha[1]) # Y

comandos = input() # R

batidas = 0

for comando in comandos:
    if bateria == 0:
        break

    if comando == 'C':
        if linha_atual == 1: #não pode na primeira
            batidas = batidas + 1
        else:
            linha_atual = linha_atual - 1

    elif comando == 'B':
        if linha_atual == quantidade_linhas: #não pode na última
            batidas = batidas + 1
        else:
            linha_atual = linha_atual + 1

    elif comando == 'E':
        if coluna_atual == 1:
            batidas = batidas + 1
        else:
            coluna_atual = coluna_atual - 1

    elif comando == 'D':
        if coluna_atual == quantidade_colunas:
            batidas = batidas + 1
        else:
            coluna_atual = coluna_atual + 1

    bateria = bateria - 1

print(f"{linha_atual} {coluna_atual} {batidas}")