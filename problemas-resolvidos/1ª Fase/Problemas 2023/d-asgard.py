################################################################################
# Objetivo: determinar trocas de botijão de gás em quantidade Y, entre X empresas 
#           ao longo de Z dias e outra considerando que:
#           -> 1° o número minimo para trocas muda conforme o input do usuario na primeira linha
#           -> 2° viagens só podem acontecer quando forem bilaterais, ou seja, não pode haver troca apenas de uma empresa para outra
#             , precisa que a outra empresa faça pelo menos 1 troca também
# Autor: Alexandre
# Data: ??/04/2024
# Duração: ??
################################################################################

def main():
  respostas = []
  temTroca = 0
  linha = input().split(" ")
  nEmpr   = int(linha[0])
  qPadrao = int(linha[1])
  nDias   = int(input())
  # matriz vazia
  matriz = list()
  for i in range(0, nEmpr):
    linha = list()
    for j in range(0, nEmpr):
      linha.append(0)
    matriz.append(linha)
  # leitura dos dados
  qtdLeituras = (nEmpr * nEmpr - nEmpr) + 1 
  for i in range(0, nDias):
    for j in range(0, qtdLeituras):
      linha = input().split(" ") 
      if j != 0:  
        emp1 = int(linha[0])
        emp2 = int(linha[1])
        botijoes = int(linha[2])
        matriz[emp1-1][emp2-1] += botijoes
    respostas.append(f"Final dia {i+1}")
    for emp1 in range(0, nEmpr):
      for emp2 in range(0, nEmpr):
        if matriz[emp1][emp2] >= qPadrao and matriz[emp2][emp1] >= qPadrao:
          temTroca = 1
          v1 = matriz[emp1][emp2] // qPadrao
          v2 = matriz[emp2][emp1] // qPadrao
          matriz[emp1][emp2] %= qPadrao
          matriz[emp2][emp1] %= qPadrao
          respostas.append(f"  Trocas entre {emp1+1}({v1}v) e {emp2+1}({v2}v)")
    if temTroca == 0:
      respostas.append("  Sem trocas")
    temTroca = 0   
  for i in respostas:
    print(i)  
main()
