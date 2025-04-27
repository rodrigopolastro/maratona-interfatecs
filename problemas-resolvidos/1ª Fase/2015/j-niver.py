################################################################################
# Objetivo: Dada uma lista de datas de aniversário e o aniversário do malaquias, 
#           determinar se há alguma pessoa nasceu no mesmo dia que ele 
# 
# Autor: Rodrigo
# Data: 14/03/2025
# Duração: 11min
################################################################################

while True:
    encontrou = False
    dia_malaquias, mes_malaquias = [int(_) for _ in input().split()]
    if dia_malaquias == mes_malaquias == 0:
        break
    
    qtd_colegas = int(input())
    for _ in range(qtd_colegas):
        dia_colega, mes_colega = [int(_) for _ in input().split()]
        if dia_colega == dia_malaquias and mes_colega == mes_malaquias:
            encontrou = True
            
    if encontrou:
        print('S')
    else:
        print('N')