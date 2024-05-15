MAX_TIME = 100000

dados_equipes = {}
classificadas = []
equipes_restantes = []


def encontra_equipe(pontuacao):
  for equipe in equipes_restantes:
    if equipe["pontuacao"] == pontuacao:
      return equipe["id_equipe"]

entradas = input().split(' ')
vagas       = int(entradas[0])
qtd_fatecs  = int(entradas[1])
qtd_equipes = int(entradas[2])

for i in range(0, qtd_equipes):
  entradas = input().split(' ')
  id_fatec           = int(entradas[0])
  id_equipe          = entradas[1]
  problemas_feitos   = int(entradas[2])
  tempo_gasto        = int(entradas[3])

  equipe = {}
  pontuacao = problemas_feitos * MAX_TIME - tempo_gasto
  equipe["id_equipe"] = id_equipe
  equipe["pontuacao"] = pontuacao

  if not dados_equipes.get(id_fatec):
    dados_equipes[id_fatec] = []
  dados_equipes[id_fatec].append(equipe)

print(dados_equipes)
print(dados_equipes.keys())
# classifica a melhor equipe de cada fatec
for fatec in dados_equipes.keys():
  print(f"EQUIPES DA FATEC {fatec}:")
  maior_pontuacao = -1
  melhor_equipe_fatec = 0
  for equipe in dados_equipes[fatec]:
    print(equipe)
    equipes_restantes.append(equipe)
    if equipe["pontuacao"] > maior_pontuacao:
      maior_pontuacao = equipe["pontuacao"]
      melhor_equipe_fatec = equipe["id_equipe"]
  
  classificadas.append(int(melhor_equipe_fatec))

pontuacoes = []
for equipe in equipes_restantes:
  if int(equipe["id_equipe"]) not in classificadas:
    # print(f"classifcada entreas restantes: {equipe[id_equipe]}")
    pontuacoes.append(equipe["pontuacao"])

pontuacoes.sort()
pontuacoes.reverse()
vagas_restantes = vagas - qtd_fatecs

for pontuacao in pontuacoes[:vagas_restantes]:
  equipe_classificada = encontra_equipe(pontuacao)
  classificadas.append(int(equipe_classificada))

classificadas.sort()

resposta = ''
for i in classificadas:
  if i != classificadas[-1]:
    resposta += str(i) + ', '
  else:
    resposta += str(i) + '.'

print(resposta)
