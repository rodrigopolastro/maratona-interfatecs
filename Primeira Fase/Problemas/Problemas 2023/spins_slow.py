def main():
  respostas = []

  n = 1
  while n != 0:
    n = int(input())
    bits = [False] * n 
    for i in range(1, n+1):
      multiplicador = 1
      while True:
        posicao = i * multiplicador - 1
        if posicao > n - 1:
          break
        
        bits[posicao] = not bits[posicao]
        multiplicador += 1
    
    linha = []
    for i in range(0, n):
      if bits[i] == True:
        linha.append(str(i+1))
        
    respostas.append(linha)

  for i in respostas:
    print(" ".join(i).strip())
    
main()