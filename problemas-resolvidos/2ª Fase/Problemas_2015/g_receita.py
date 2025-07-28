################################################################################
# Objetivo:
#
# Autor: Rodrigo 
# Data: 23/07/2025
# Duração: 20:16 - 21:00
################################################################################

from math import lcm, ceil

qtdCasos = int(input())
for i in range(qtdCasos):
    qtdRemedios = int(input())
    remedios = list()
    listaHoras = list()
    for _ in range(qtdRemedios):
        entrada = input().split()
        nomeRemedio = entrada[0]
        miligramasDose = int(entrada[1])
        horasEntreDose = int(entrada[2])
        miligramasCaixa = int(entrada[3])
        listaHoras.append(horasEntreDose)
        remedios.append((
            nomeRemedio,
            miligramasDose,
            horasEntreDose,
            miligramasCaixa
        ))
    mmcHoras = lcm(*listaHoras)
    totalDias = ceil(mmcHoras / 24)
    print('Total de dias =', totalDias)
    remediosOrdenados = sorted(remedios, key=lambda x: x[0])
    for remedio in remediosOrdenados:
        # remedio = remedios[nomeRemedio]
        nomeRemedio = remedio[0]
        qtdDosesRemedio = int(mmcHoras / remedio[2] + 1)
        totalMiligramasRemedio = remedio[1] * qtdDosesRemedio
        totalCaixasRemedio = ceil(totalMiligramasRemedio / remedio[3])
        print(f"{nomeRemedio} {totalMiligramasRemedio} {totalCaixasRemedio}")
        
    
    
    # print('Caso ' + i+1 + ':')
    

