################################################################################
# Problema: Problema E da 1ª fase de 2023
# Objetivo: Determinar a posição final de um robô se movimentando em uma matriz
#           a partir da sua sequência de movimentos
################################################################################

batidas = 0

entrada1 = input().split(' ')
quantidade_linhas = int(entrada1[0])
quantidade_colunas = int(entrada1[1])
bateria_restante = int(entrada1[2])

entrada2 = input().split(' ')
linha_atual = int(entrada2[0])
coluna_atual = int(entrada2[1])

comandos = input()

for comando in comandos:
    if bateria_restante == 0:
        break

    if comando == "C":
        if linha_atual != 1:
            linha_atual -= 1
        else:
            batidas += 1
    elif comando == "B":
        if linha_atual != quantidade_linhas:
            linha_atual += 1
        else:
            batidas += 1
    elif comando == "D":
        if coluna_atual != quantidade_colunas:
            coluna_atual += 1
        else:
            batidas += 1
    elif comando == "E":
        if coluna_atual != 1:
            coluna_atual -= 1
        else:
            batidas += 1

    bateria_restante -= 1

print(f"{linha_atual} {coluna_atual} {batidas}")