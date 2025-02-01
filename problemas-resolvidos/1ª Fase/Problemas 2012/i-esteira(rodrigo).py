################################################################################
# Objetivo: Dada a duração inicial da atividade e a velocidade inicial em uma 
#           esteira, calcular a distancia total percorrida e a velocidade média 
#           desenvolvida. 
# 
#           O detalhe é que a esteira em questão sempre divide a duracao da 
#           atividade em 32 "etapas" representadas cada uma por uma coluna de 
#           um grafico, e varia a velocidade nessas colunas com uma coluna baixa 
#           representando a velocidade inicial e uma coluna alta represntando a 
#           velocidade increentada de 3hm/h.
# Autor: Rodrigo
# Data: 29/01/2025
# Duração: 25min (rodou de primeira paeee)
################################################################################

QUANTIDADE_COLUNAS_GRAFICO = 32
qtdCasosTeste = int(input())

for _ in range(qtdCasosTeste):
    atividade = input().split()
    duracaoTotalHoras, velocidadeInicial = int(atividade[0])/60, float(atividade[1])
    duracaoColunaGrafico = duracaoTotalHoras / QUANTIDADE_COLUNAS_GRAFICO
    
    graficoEsteira = input()
    tempoVelocidadeBaixa = duracaoColunaGrafico * graficoEsteira.count('b')
    tempoVelocidadeAlta = duracaoColunaGrafico * graficoEsteira.count('A')
    
    distanciaPercorrida = (tempoVelocidadeBaixa * velocidadeInicial) + (tempoVelocidadeAlta * (velocidadeInicial+3))

    velocidadeMedia = distanciaPercorrida / duracaoTotalHoras
    print(round(distanciaPercorrida, 1), round(velocidadeMedia, 1))