import unicodedata

def removerA(texto):
    return ''.join(c for c in unicodedata.normalize('NFKD',texto) if unicodedata.category(c) != "Mn")


entrada = input()
entrada = removerA(entrada)
lenentrada = len(entrada)
novastring = ''
for ch in entrada:
    if ch != " ":
        novastring += ch
entrada = novastring
qtdImpar = 0
ltrs = set()
if lenentrada % 2 == 0:
    for ch in entrada:
        if entrada.count(ch) % 2 == 1:
            print("FALSO")
            quit()
    print("VERDADEIRO")
        
else:
    for ch in entrada:
        if entrada.count(ch) % 2 == 1:
            qtdImpar += 1
            ltrs.add(ch)
    if qtdImpar % 2 == 0 or len(ltrs) > 1:
        print("FALSO")
    else:
        print("VERDADEIRO")