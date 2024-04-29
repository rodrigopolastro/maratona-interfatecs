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



