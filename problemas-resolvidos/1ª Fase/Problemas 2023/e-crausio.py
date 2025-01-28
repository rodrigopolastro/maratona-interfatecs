################################################################################
# Objetivo: Determinar a posição final de um robô se movimentando em uma matriz 
#           a partir da sua sequência de movimentos
# Autor: Rodrigo
# Data: ??/??/2024
# Duração: ?
################################################################################

def main():
  batidas = 0

  string = input().split(" ")
  l = int(string[0])
  c = int(string[1]) 
  b = int(string[2]) 

  string = input().split(" ")
  linha = int(string[0])
  coluna = int(string[1]) 

  comandos = input() 

  for i in range(0, b):
    comando = comandos[i]
    if comando == "C": 
      if linha != 1: 
        linha -= 1
      else:
        batidas += 1
    elif comando == "B":
      if linha != l:
        linha += 1
      else:
        batidas+=1   
    elif comando == "D":
      if coluna != c:
        coluna += 1
      else:
        batidas+=1     
    elif comando == "E":
      if coluna != 1:
        coluna -= 1
      else:
        batidas+=1   

  print(f"{linha} {coluna} {batidas}")

main()