################################################################################
# Objetivo: Determinar quais 'quantum gates' (uma porta binária) vão estar abertos 
#           após a criação de N quantum gates sabendo que um novo criado altera,
#           o estado dos seus múltiplos
# OBS > problema muito mal explicado pois é muito ambiguo para o output 1, 
# basicamente o output tem que ser todos quadrados perfeitos, então o input 10 tem de output 1 4 9 
# Autor: Alexandre / Rodrigo
# Data: ??/04/2024
# Duração: ??
################################################################################

# OBS: Essa é a versão otimizada da solução, feita depois que percemos que a saída
#      sempre será a lista de quadrados perfeitos de 1 a n. Isso acontece pois 
#      somente quadrados perfeitos possuem um número ímpar de divisores, enquanto os 
#      demais inteiros possuem um número par.

def main():
  respostas = []

  n = 1
  while n != 0:
    n = int(input())
    linha = []
    for i in range(1, n):
      if i * i <= n:
        linha.append(str(i*i))

    respostas.append(linha)
   
  for i in respostas:
    print(" ".join(i).strip())

main()