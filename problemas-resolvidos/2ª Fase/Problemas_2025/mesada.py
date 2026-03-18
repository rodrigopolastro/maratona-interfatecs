numfilhos,mesada,categorias = [int(x) for x in input().split()]

maximoValores = [30,20,10]

matCat = [ [0 for i in range(categorias)] for x in range(numfilhos)]


quebrar = False
for categoria in range(categorias):
    if quebrar == True:
        break
    encontrouMax = False
    for maximo in maximoValores:
        if maximo * numfilhos <= mesada:
            encontrouMax = True
            for f in range(numfilhos):
                matCat[f][categoria] = maximo
            mesada -= maximo * numfilhos
            break
    if not encontrouMax or (mesada != 0 and categoria == categorias -1):
        
        # print(matCat)
        # input()
        for cat in range(categorias):
            if matCat[-1][cat] == 30:
                continue
            else:
                mesada += matCat[-1][cat]
                matCat[-1][cat] = 0
                # print('???')
                # print(mesada)
                # if mesada == 30:
                #     matCat[-1][cat] = 30
                # el
                if mesada >= 30:
                    matCat[-1][cat] = 30
                    if cat != categorias -1:
                        matCat[-1][cat+1] = mesada % 30
                else:
                    matCat[-1][cat] = mesada % 30
                quebrar = True
                break
                    
for c in matCat:
    print(*c)
            