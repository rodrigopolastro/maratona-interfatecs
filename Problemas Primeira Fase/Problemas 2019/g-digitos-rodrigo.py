numeros_testados = [False] * 100000
primos = []

def ePrimo(numero):
  numeros_testados[numero-1] = True

  if numero == 1: 
    return False
  
  if numero == 2:
    return True

  for primo in primos:
    if numero % primo == 0:
      return False
    
  return True

n = int(input())
for caso in range(1, n+1):
  num_digitos = [0] * 10  
  intervalo = input().split(' ')
  inicio = int(intervalo[0])
  fim    = int(intervalo[1])

  for numero in range(inicio, fim+1):
    if not numeros_testados[numero-1]:
      if ePrimo(numero):
        primos.append(numero)
      
  for primo in primos:
    primo_str = str(primo)
    if primo >= inicio and primo <= fim:
      for i in range(0, 9+1):
        ocorrencias = primo_str.count(str(i))
        num_digitos[i] += ocorrencias

  print(f"INTERVALO {caso}")
  for digito in range(0, 9+1):
    print(f"{digito}: {num_digitos[digito]}")





  

