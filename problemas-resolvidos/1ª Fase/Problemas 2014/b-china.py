# Resumo Questão:
# Um 'malabarista' de pratos chines quer saber se ele consegue deixar rodando X pratos ao mesmo tempo, porém ao aplicado certa 
# força, tem um tempo até que esse prato pare de girar, caia no chão e quebra, o desafio é criar um algoritmo vendo se é possivel
# ele girar todos os pratos do 'input' sem que nenhum quebre, se nenhum quebrar, printar Ok,
# caso quebre printar o segundo que quebrou e qual prato quebrou, caso mais de 1 prato quebre no mesmo segundo, tem que pegar o prato de menor número
# comeco: 19:00 - 05/02/2025 / término: 21 - 06/02/2025


def quebrou(dicionario: dict):
    for valor in dicionario.values():
        if valor <= 0:
            return True
    return False

def menoresQue0(valores:list):
    retornar = 0
    for valor in valores:
        if valor == 0:
            retornar+=1
    return retornar
def passandoTempo(dicionario: dict, tempoDecorrido=0):
    dicionarioCopia = dicionario.copy()
    for chave in dicionarioCopia.keys():
        dicionarioCopia[chave] -= tempoDecorrido

    if quebrou(dicionarioCopia):
        if menoresQue0(list(dicionarioCopia.values())) > 0:
            
            retornar = []
            for elemento in dicionarioCopia.keys():
                if dicionarioCopia[elemento] == 0:
                    retornar.append(elemento)
            retornar = sorted(retornar)
            # print(tempoDecorrido,retornar[0])
            return [True, f"{tempoDecorrido} {retornar[0]}"]

        else:
            
            for elemento in dicionarioCopia.keys():
                if dicionarioCopia[elemento] == 0:
                    # print(tempoDecorrido,elemento)

                    return [True, f"{tempoDecorrido} {elemento}"]
    return [False, None]


while True:
    varetas, segundos = [int(x) for x in input().split()]
    printarOk = True
    printarBroken = None
    if varetas == 0:
        break
    comeca = int(input())
    quantidade_pratos = int(input())
    comparacao = dict()
    tempoAtual = 0
    for _ in range(quantidade_pratos):
        prato, forca = [int(x) for x in input().split()]
        if _ == 0:
            if prato == comeca:
                pass
            else:
                tempoAtual += abs(prato-comeca) * segundos
            
        if comparacao.get(prato) == None:
            comparacao[prato] = tempoAtual +  (forca * 4)

        else:
            comparacao[prato] = forca * 4
        
        if printarOk:
                response = passandoTempo(comparacao, tempoAtual)
                if response[0]:
                    
                    printarOk = False
                    if response[1] != None and printarBroken == None:
                        printarBroken = response[1]

        for atual in range(tempoAtual, (tempoAtual + (forca * 2)  )):

            # tempoAtual += segundos
            if printarOk:
                response = passandoTempo(comparacao, atual)
                if response[0]:
                    
                    printarOk = False
                    if response[1] != None and printarBroken == None:
                        printarBroken = response[1]

        tempoAtual += forca * 2
        tempoAtual += segundos

    if printarOk:
        print("OK")
    else:
        print(printarBroken)

