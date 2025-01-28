################################################################################
# Objetivo: formar uma piramide de letras conforme o input onde se tem dois parametros -> o numero  E  maiusculas ou minusculas 
# ex: 3 maiusculas
#.........................A
#........................AB
#.......................ABC
# Autor: Alexandre
# Data: ??/??/2024
# Duração: ??
################################################################################
def main():
  alfabeto = "abcdefghijklmnopqrstuvwxyz"

  string = input().split(" ")
  n = int(string[0])
  p = string[1]

  if p == "maiusculas":
    alfabeto = alfabeto.upper()
  
  for i in range(1, n+1):
    qtd_pontos = 26 - i
    pontos = list('.' * qtd_pontos)
    print(''.join(pontos) + alfabeto[0:i])

main()



