dia_prova = input().split(' de ')
tempo = {
    'semana':7,
    'semanas':7,
    'dia':1,
    'dias':1,
    'mes':30,
    'meses':30
}
veterano = input().split(' ')
veterano = int(veterano[0])*tempo[veterano[1]]

ordem_meses=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
calouro = input().split(' de ')
meses_geral =[]
for i in range(12):
    fe = input().split(': ')
    meses_geral.append((fe[0],fe[1]))
calouro[1] = calouro[1][0:3]
dia_prova[1]=dia_prova[1][0:3]
dias = {
    'um':1,
    'dois':2,
    'tres':3,
    'quatro':4,
    'cinco':5,
    'seis':6,
    'sete':7,
    'oito':8,
    'nove':9,
    'dez':10,
    'onze':11,
    'doze':12,
    'treze':13,
    'quatorze':14,
    'quinze':15,
    'dezesseis':16,
    'dezessete':17,
    'dezoito':18,
    'dezenove':19,
    'vinte':20,
    'vinte e um':21,
    'vinte e dois':22,
    'vinte e tres':23,
    'vinte e quatro':24,
    'vinte e cinco':25,
    'vinte e seis':26,
    'vinte e sete':27,
    'vinte e oito':28,
    'vinte e nove':29,
    'trinta':30,
    'trinta e um':31,
}

dia_prova[0] = dias[dia_prova[0]]
calouro[0] = dias[calouro[0]]
prova = 0
calouro_dias = 0
novo_dicionario = {}
for i in ordem_meses:
    for j in meses_geral:
        if j[0] == i:
            novo_dicionario[i] = int(j[1])
            break
for i in novo_dicionario.keys():
    if i == dia_prova[1]:
        prova+=int(dia_prova[0])
        break
    else:
        prova+=novo_dicionario[i]
        
for i in novo_dicionario.keys():
    if i == calouro[1]:
        calouro_dias+=int(calouro[0])
        break
    else:
        calouro_dias+=novo_dicionario[i]

if calouro[0] > novo_dicionario[calouro[1]] or dia_prova[0] > novo_dicionario[dia_prova[1]]:
    print('data nao existe!')
elif calouro_dias >= prova:
    print('esta de brincadeira?')
elif calouro_dias >= 1 and (prova - calouro_dias) < veterano:
    print('olha a reprovacao chegando!')
elif prova - calouro_dias == veterano:
    print('que caloura ousada!')
else:
    print('jovem consciente!')