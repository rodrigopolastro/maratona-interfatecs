################################################################################
# Objetivo: Simular uma roleta que sorteia nomes. A cada rodada, a roleta se 
#           movimenta N posições para um dos lados e elimina o nome em que parar.
#           Quando sobrar somente um nome, informar quem ganhou e a quantidade 
#           de rodadas.
# 
# Autor: Rodrigo
# Data: 14/03/2025
# Duração: 35min
################################################################################

def movimenta_lista_dir(lista_original):
    lista_movimentada = list()
    lista_movimentada.append(lista_original[-1])
    for elemento in lista_original[:-1]:
        lista_movimentada.append(elemento)

    return lista_movimentada

try:
    while True:
        qtd_participantes = int(input())
        participantes = input().split()
        movs_rodada = int(input())
        
        cont_rodadas = 0
        posicao_atual = 0
        # encerra quando sobrar só um parcipante
        while participantes.count(None) < qtd_participantes-1:
            cont_rodadas += 1
            posicao_atual = (posicao_atual + movs_rodada) % qtd_participantes
            if participantes[posicao_atual] != None:
                participantes[posicao_atual] = None
                participantes = movimenta_lista_dir(participantes)
        
        vencedor = [p for p in participantes if p != None][0]    
        print(f"apos {cont_rodadas} rodadas quem levou a bolada foi {vencedor}")
except EOFError:
    pass
