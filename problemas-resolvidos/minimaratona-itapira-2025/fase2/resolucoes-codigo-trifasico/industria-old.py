qt,separ = [int(x) for x in input().split()]
respostas = []
for _ in range(1,qt+1,separ):
    respostas.append(_)

while True:
    remover = []
    if len(respostas) == 1:
        break
    if len(respostas) <= separ:
        respostas.pop(separ % len(respostas))
    else:
        for _ in range(separ, len(respostas), separ):
            remover.append(_)
        for indexRemover in remover[::-1]:
            respostas.pop(indexRemover)
print(respostas[0])
