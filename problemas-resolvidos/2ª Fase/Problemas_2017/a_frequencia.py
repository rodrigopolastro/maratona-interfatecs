# Resolvido por: Rodrigo Polastro
# Data: 08/09/2024
# Início: 18:50
# Fim: 19:50 (Sim, eu sou um animal e demorei 1h nesse por causa de algo estúpido)

from math import ceil

entrada = input().split(' ')
dias_letivos = int(entrada[0])
dias_frequentados = int(entrada[1])
dias_restantes = int(entrada[2])

frequencia_maxima = (dias_frequentados + dias_restantes) / dias_letivos

if frequencia_maxima < 0.75:
    print('sem chance')
elif frequencia_maxima <= 0.77:
    print('soh um milagre')
else:
    frequencia_atual = dias_frequentados / dias_letivos
    if frequencia_atual >= 0.75:
        print(f"tranquilo pode faltar {dias_restantes} dia(s)")
    else:   
        dias_obrigatorios = ceil(dias_letivos * 0.75) - dias_frequentados
        faltas_possiveis = dias_restantes - dias_obrigatorios
        print(f"tranquilo pode faltar {faltas_possiveis} dia(s)")