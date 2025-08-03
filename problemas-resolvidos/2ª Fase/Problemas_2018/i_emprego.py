ed = [] # entradaDados
try:
    while True:
        en = input()
        if en == '' or en == '\n':
            raise EOFError
        dados = en.split()
        ed.append((dados[0],int(dados[1])))
except EOFError:
    qtd = len(ed)
    if qtd == 1:
        print(ed[0][0],ed[0][1])
    elif qtd == 2:
        print(ed[1][0],ed[1][1])
    elif qtd == 3:
        if ed[1][1] > ed[0][1]:
            print(ed[1][0],ed[1][1])
        else:
            print(ed[2][0],ed[2][1])
    elif qtd == 4:
        terc = ed[2][1]
        prim = ed[0][1]
        seg = ed[1][1]
        if terc > prim and terc > seg:
            print(ed[2][0],ed[2][1])
        else:
            print(ed[3][0],ed[3][1])
    else:
        PorcTotal = 0
        PorcPerItem = 100 / len(ed)
        maiorItem = 0
        achouMaior = False
        for cand in ed:
            # print(PorcTotal)
            # print(cand[1])
            if PorcTotal < 37:
                maiorItem = max(maiorItem,cand[1])
                PorcTotal += PorcPerItem
            else:
                if maiorItem < cand[1]:
                    print(cand[0],cand[1])
                    achouMaior = True
                    break
                
        if not achouMaior:
            print(ed[-1][0],ed[-1][1])