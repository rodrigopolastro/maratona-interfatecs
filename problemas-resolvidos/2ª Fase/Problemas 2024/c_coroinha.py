entrada = input().split(' ')

linhas = int(entrada[0])
colunas = int(entrada[1])
qtd_golpes_vento = int(entrada[2])
linha_destino = int(entrada[3])
coluna_destino = int(entrada[4])

linha_inicio, coluna_inicio = linha_destino, coluna_destino

direcoes_golpes_vento = input()
for direcao in direcoes_golpes_vento[::-1]:
    if direcao == 'C':
        linha_inicio += 1
    elif direcao == 'B':
        linha_inicio -= 1
    elif direcao == 'D':
        coluna_inicio -= 1
    elif direcao == 'E':
        coluna_inicio += 1
        
if 1 <= linha_inicio <= linhas and 1 <= coluna_inicio <= colunas:
    print(f"{linha_inicio} {coluna_inicio}")
else:
    print("-1 -1")
        