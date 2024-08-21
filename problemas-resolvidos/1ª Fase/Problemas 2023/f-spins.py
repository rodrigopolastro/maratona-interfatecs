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