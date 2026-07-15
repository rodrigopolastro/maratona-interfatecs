################################################################################
# Objetivo:
#
# Autor: Rodrigo
# Data: 13/05/2026
# Duração: inicio: 17:13
################################################################################
IDADE_HELLEN = 26
IDADE_IAN = 29

55

while True:
    dia = int(input())
    if dia == 0:
        break

    if dia == 98:
        print('IAN BIRTHDAY, GO OUT FOR DINNER')
        continue


    if dia == 99:
        print('HELLEN BIRTHDAY, GO OUT FOR DANCING')
        continue

    mes = int(input())

    if (dia + mes + IDADE_HELLEN + IDADE_IAN) % 2 == 0:
        print('WATCH SERIES')
    else:
        print('WATCH MOVIE')
59