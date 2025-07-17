################################################################################
# Objetivo: 
# ->  Determinar o enésimo número triangular
# Comentários: 
# ->  O problema mais fácil da prova, sem dúvidas.
# Autor: Rodrigo
# Data: 16/07/2025
# Duração: 5m
################################################################################

while True:
    n = int(input())
    if n == 0:
        break
    print(int(n * (n+1) / 2))

