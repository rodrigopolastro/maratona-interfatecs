
from math import sqrt,isqrt,ceil,floor,pow

INTERVALOS = [1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000, 285311670611, 8916100448256, 302875106592253, 11112006825558016, 437893890380859392, 18446744073709551616, 827240261886336827392, 39346408075296541507584, 1978419655660313627328512]
RAIZES_INTERVALOS = [i for i in range(1, 20+1)]

def encontra_intervalo_inicial(numero):
    for i in range(len(INTERVALOS)):
        if INTERVALOS[i] > numero:
            maior = RAIZES_INTERVALOS[i]
            menor = RAIZES_INTERVALOS[i-1]
            return (menor, maior)

def converteMinutos(m):
    # print('convertendo para ', m)
    # m,s,ms = 0,0,0
    # minutos = minutos * 1000 * 60
    # resposta = ""
    # resposta = str(minutos//1000//60)
    # resposta += ":"
    # resposta += str(minutos//1000%60).ljust(2,'0')
    # resposta += ":"
    # resposta += str(minutos%1000).ljust(3,'0')
    minutos = int(m)
    segundos = (abs(minutos - m)*60)
    
    
    decimal = m - minutos
    ms = (decimal * 60 * 1000) % 1000
    # ms = (minutos - m) % 1000
    # print('ms: ', ms)
    resposta = f"{minutos}:{str(int(segundos)).rjust(2,"0")}:{"%03d" % ms}"
    return resposta


indexTentar = -1
tentar = range(1000000, 2000000)
while True:
    # indexTentar += 1
    # nd=tentar[indexTentar]
    nd = int(input())
    # nd = 7
    if nd == 0:
        break
    
    if nd in INTERVALOS:
        index = INTERVALOS.index(nd)
        print(converteMinutos(RAIZES_INTERVALOS[index]))
    else:
    
    # if sqrt(nd) == isqrt(nd):
    #     print(converteMinutos(isqrt(nd)))
    # else:
    #     diferenca = 1000
    #     local = nd
        # while diferenca >= 0.001:
        #     a = floor(sqrt(local))
        #     b = ceil(sqrt(local))
        #     t = (a+b) / 2
        #     diferenca = abs(local - pow(t,t))
        #     local = pow(t,t)
        menor, maior = encontra_intervalo_inicial(nd)
        # print('menor,maiorinicial> ', menor, maior)
        diferenca = 1000
        while True:
            meio = (menor + maior) / 2
            # print('meio: ', meio)
            tentativa = pow(meio, meio)
            # print('tentativa autal: ', tentativa)
            diferenca = abs(nd - tentativa)
            if diferenca < 0.001:
                print(converteMinutos(meio))
                break
            if tentativa > nd:
                menor, maior = menor, meio
            elif tentativa < nd:
                menor, maior = meio, maior
        
        
        # maior = meio
    #     print(converteMinutos(local))
    
    
# while True:
#     numero  = int(input())
#     print(encontra_intervalo_inicial(numero))

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 15
# 27
# 30
# 0