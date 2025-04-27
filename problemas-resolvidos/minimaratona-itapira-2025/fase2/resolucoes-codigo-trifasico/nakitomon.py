qtdCartas = int(input())
cartasD = []
cartasS = []
pontD = 0
pontS = 0
pontE = 0
for _ in range(qtdCartas):
    cartasD.append(input())
for _ in range(qtdCartas):
    cartasS.append(input())
def procJogo(danete,silvio):
    global pontD
    global pontS
    global pontE
    danI = [int(x) for x in danete.split()]
    silI = [int(x) for x in silvio.split()]
    for _ in range(4):
        if danI[_] > silI[_] or silI[_] > danI[_]:
            if danI[_] > silI[_]:
                pontD +=1
                return
            else:
                pontS +=1
                return
        else:
            pass
    pontE +=1 

for _ in range(qtdCartas):
    procJogo(cartasD[_],cartasS[_])
print(f"danette venceu: {pontD}")
print(f"silvio venceu: {pontS}")
print(f"empates: {pontE}")