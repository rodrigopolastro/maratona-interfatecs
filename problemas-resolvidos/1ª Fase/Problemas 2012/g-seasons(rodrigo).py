################################################################################
# Objetivo: Determinar estação do ano de datas informadas
# Autor: Rodrigo
# Data: 27/01/2025
# Duração: 22 min
################################################################################

# Spring = March 21st -> June 20th         = 21/03 -> 20/06
# Summer = June 21st -> September 22nd     = 21/06 -> 22/09
# Autumn = September 23rd -> December 20th = 23/09 -> 20/12
# Winter = December 21st -> March 20th     = 21/12 -> 20/03

PRIMAVERA = ["00/03/21", "00/06/20"]
VERAO = ["00/06/21", "00/09/22"]
OUTONO = ["00/09/23", "00/12/20"]
INVERNO = ["00/12/21", "01/03/20"]

numeroInputs = int(input())
for _ in range(numeroInputs):
    entrada = input().split()
    dia, mes = entrada[0], entrada[1]
    if len(dia) == 1:
        dia = "0" + dia
    if len(mes) == 1:
        mes = "0" + mes
        
    ANO = "00"
    data = f"{ANO}/{mes}/{dia}"
    # print(data)
    # print(data)
    
    if PRIMAVERA[0] <= data <= PRIMAVERA[1]:
        print("spring")
    elif VERAO[0] <= data <= VERAO[1]:
        print("summer")
    elif OUTONO[0] <= data <= OUTONO[1]:
        print("autumn")
    else:
        print("winter")
    
    