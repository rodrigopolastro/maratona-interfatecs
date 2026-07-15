colunas, linhas = map(int, input().split())
matriz = list()

def is_matriz_simetrica():
    # simetria vertical

    limite_linhas = int(linhas/2) if linhas % 2 == 0 else int((linhas+1)/2)
    limite_colunas = colunas
    for i in range(limite_linhas):
        for j in range(limite_colunas):
            peca_atual = matriz[i][j]
            
            simetria_vertical = matriz[linhas-i-1][j]
            if peca_atual != simetria_vertical:
                return False
            
    # simetria horizontal
    limite_linhas = linhas
    limite_colunas = int(colunas/2) if colunas % 2 == 0 else int((colunas+1)/2)
    for i in range(limite_linhas):
        for j in range(limite_colunas):
            peca_atual = matriz[i][j]
            
            simetria_horizontal = matriz[i][colunas-j-1]
            if peca_atual != simetria_horizontal:
                return False

    return True

for _ in range(linhas):
    linha = input().split()
    matriz.append(linha)

if is_matriz_simetrica():
    print("PODE SER VERDADEIRA")
else:
    print("CERTAMENTE FALSA")