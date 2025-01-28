################################################################################
# Objetivo: Fazer um if baseado no enunciado. Muito tonto.
# Autor: Rodrigo e Alexandre
# Data: ??/??/2024
# Duração: ?
################################################################################

import math

def main():
  v = int(input())
  if v <= 107:
    margem = v + 7
  else:
    margem = v * 1.07
  
  print(math.ceil(margem))
  # print(round(margem))
  
main()