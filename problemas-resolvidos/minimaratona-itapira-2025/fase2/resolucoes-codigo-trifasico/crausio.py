linhas, colunas, bateria = [int(_) for _ in input().split()]
linhaCrausio, colunaCrausio = [int(_) for _ in input().split()]
caminho = input()[:bateria]
batidas = 0

for mov in caminho:
    if mov == "C":
        if linhaCrausio == 1:
            batidas += 1
        else:
            linhaCrausio-=1

    elif mov == "B":
        if linhaCrausio == linhas:
            batidas += 1
        else:
            linhaCrausio+=1 
            
    elif mov == "E":
        if colunaCrausio == 1:
            batidas += 1
        else:
            colunaCrausio-=1

    elif mov == "D":
        if colunaCrausio == colunas:
            batidas += 1
        else:
            colunaCrausio+=1

print(linhaCrausio, colunaCrausio, batidas)
