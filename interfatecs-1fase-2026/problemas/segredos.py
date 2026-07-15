entr = []
sai = []
regrasEH = []
regrasNH= []
nCasos = int(input())
for i in range(nCasos):
    regras = input("").split(";")
    for regra in regras:
        r = regra.split(" ")
        if len(r)>3:
            regrasNH.append(r[0]+":"+r[-1])
        else:
            regrasEH.append(r[0]+":"+r[-1])
for i in range(nCasos):
    deci = input().split(":")
    keys = deci[1].split(";")
    i = -1
    while True:
        i+=1
        if(i == len(keys)):
            entr.append(deci[0])
            sai.append(ppp)
            break
        if ((deci[0]+":"+keys[i]) in regrasNH):
            pass
        elif((deci[0]+":"+keys[i]) in regrasNH):
            entr.append(deci[0])
            sai.append(keys[i])
            break
        else:
            ppp = keys[i]
frase = input("").split(" ")
res = ""
for palavra in frase:
    res += sai[int(entr.index(palavra))] + " "
print(res.strip())