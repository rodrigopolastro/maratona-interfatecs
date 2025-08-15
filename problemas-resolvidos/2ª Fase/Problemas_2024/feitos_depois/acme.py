dadosEntrada = []
while True:
    tempoChegada, lote,tempoDemora = [int(x) for x in input().split()]
    if tempoChegada == lote == tempoDemora == 0:
        break
    dadosEntrada.append((tempoChegada,lote,tempoDemora))
    
    
dadosEntrada.sort(key= lambda x : (x[0],x[2]))

resposta = []

minutos = 0
estaProduzindoAlgo = False
cooldown = -1
# print(dadosEntrada)
# print(dadosEntrada)
primeiro = dadosEntrada.pop(0)
# print(primeiro)
estaProduzindoAlgo = True

cooldown = primeiro[2]
resposta.append((primeiro[1],primeiro[0],primeiro[2]))
while len(dadosEntrada) > 0:
    
    
    if not estaProduzindoAlgo:
        dadosEntrada.sort(key= lambda x : (x[2],x[0]))
        index = 0
        try:
            while True:
                if dadosEntrada[index][0] <= minutos:
                    # print(dadosEntrada[index])
                    # print(minutos)
                    estaProduzindoAlgo = True
                    cooldown = dadosEntrada[index][2]
                    fazendo = dadosEntrada.pop(index)
                    # print(fazendo)
                    resposta.append((fazendo[1],minutos,minutos + cooldown))
                    break
                index +=1
        except IndexError:
            pass
    minutos += 1
    cooldown -= 1
    
    if cooldown <= 0:
        estaProduzindoAlgo = False
    
    if len(dadosEntrada) == 0:
        break

for r in resposta:
    print(*r)
    
    
    
    
    
    
    
    