################################################################################
# Exercício: Scoreboard Classificatória
# Objetivo:
# -> Gerar relatório de times classificados para a final do Interfatecs segundo 
#    critérios definidos
# Comentários:
# -> exercício majoritariamente de manipulação de listas. a coisa mais importante
#    é organizar o código para não criar conflitos entre os critérios de classificação
#    e se preocupar em ordenar os times do jeito correto
# Autor: Rodrigo e Almir
# Data: 07/08/2025
# Duração: 1h15
################################################################################

times = list()
classificados = list()

def eliminaTimesSemExerc(times):
    retorno = list()
    for time in times:
        if time[2] == 0:
            retorno.append(time)
    return retorno

def getMelhoresTimesFatecSede(times, fatecSede, qtdVagas):
    timesFatecSede = list(filter(lambda f: f[1] == fatecSede, times))
    if len(timesFatecSede) == 0:
        return []
    #ordenado por qtdProblemas crescente e tempoGasto descrescente
    timesFatecSede.sort(key=lambda t: (-t[2], t[3])) 
    return timesFatecSede[:qtdVagas]

def getMelhoresCadaFatec(times):
    melhores = list()
    fatesAvaliadas = set()
    times.sort(key=lambda t: (-t[2], t[3]))
    while len(times) > 0:
        melhor = times[0]
        fatecMelhorTime = melhor[1]
        melhores.append(melhor)
        fatesAvaliadas.add(fatecMelhorTime)
        times = [t for t in times if t[1] != fatecMelhorTime]
        
    return melhores
fatecSede = input()
qtdVagas, qtdVagasExtrasSede = [int(_) for _ in input().split()]
qtdVagasSede = qtdVagasExtrasSede+1
qtdVagasRestantes = qtdVagas
qtdTimes = int(input())
for _ in range(qtdTimes):
    entrada = input().split('|')
    nomeTime = entrada[0]
    nomeFatec = entrada[1]
    qtdProblemasFeitos = int(entrada[2])
    tempoTotal  = int(entrada[3])
    times.append((nomeTime, nomeFatec, qtdProblemasFeitos, tempoTotal))
    
eliminados = eliminaTimesSemExerc(times)
timesRestantes = [t for t in times if t not in eliminados]

melhoresTimesFatecSede = getMelhoresTimesFatecSede(timesRestantes, fatecSede, qtdVagasSede)
qtdClassificadosFatecSede = len(melhoresTimesFatecSede)
if qtdClassificadosFatecSede > 0:
    for time in melhoresTimesFatecSede:
        classificados.append(time)
        qtdVagasRestantes -= 1

melhoresCadaFatec = getMelhoresCadaFatec(timesRestantes)
for m in melhoresCadaFatec:
    if m not in classificados:
        classificados.append(m)
        qtdVagasRestantes -= 1     

timesRestantes = [t for t in timesRestantes if t not in classificados]
timesRestantes.sort(key=lambda t: (-t[2], t[3]))    
remover = []
for i in range(qtdVagasRestantes):
    classificados.append(timesRestantes[i])
    remover.append(i)
    
for _ in remover[::-1]:
    timesRestantes.pop(_)

# classificados.sort(key=lambda t: (-t[2], t[3])) 
# timesRestantes.sort(key=lambda t: (-t[2], t[3])) 

print('Classificados para a Final')
for t in sorted(classificados, key=lambda c: (c[0])):
    print(f"{t[0]} - {t[1]} ({t[2]},{t[3]})")
print()
    
print('Lista de Espera')
for t in sorted(timesRestantes, key=lambda t: (-t[2], t[3])):
    print(f"{t[0]} - {t[1]} ({t[2]},{t[3]})")
print()
    
print('Desclassificados')
for t in sorted(eliminados, key=lambda e: e[0]):
    print(f"{t[0]} - {t[1]} ({t[2]},{t[3]})")
print()    

print('Apuracao concluida!')