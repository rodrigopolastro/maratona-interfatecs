nomeP = []
idP = []
pointP = []
def caminho(idF):
    res = "\\"+nomeP[idP.index(idF)]
    if(pointP[idP.index(idF)] == 0):
        return res
    else:
        res = caminho(pointP[idP.index(idF)])+res
        return res
nPastas = int(input())
for i in range(nPastas):
    pasta = input().split()
    idP.append(int(pasta.pop(0)))
    pointP.append(int(pasta.pop()))
    nome_pasta =  ' '.join(pasta)
    nomeP.append(nome_pasta)

nSearch = int(input())
for i in range(nSearch):
    caminhos = []
    pesq = input()
    for id in idP:
        idT = idP.index(id)
        if pesq in nomeP[idT]:
            caminhos.append(caminho(id))
    if caminhos == []:
        print("NOT FOUND")
    else:
        caminhos.sort()
        for cam in caminhos:
            print(cam)