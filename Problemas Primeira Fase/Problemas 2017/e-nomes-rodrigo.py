respostas = []

nome_pai = input()
q = int(input())

for i in range(0, q):
  nome = input()
  if len(nome) >= 4 and nome[:4] == nome_pai[:4]:
    respostas.append("VERIFICAR")
  else:
    respostas.append("NORMAL")

for resposta in respostas:  
  print(resposta)