MAX_TIME = 100000
dados_equipes = []
classificados = []

entradas = input().split(' ')
vagas       = int(entradas[0])
qtd_fatecs  = int(entradas[1])
qtd_equipes = int(entradas[2])

for i in range(0, qtd_equipes):
  entradas = input().split(' ')
  id_fatec           = int(entradas[0])
  id_equipe          = int(entradas[1])
  problemas_feitos   = int(entradas[2])
  tempo_gasto        = int(entradas[3])


  pontuacao = problemas_feitos * MAX_TIME - tempo_gasto
  equipe = []
  equipe.append(id_fatec)
  equipe.append(id_equipe)
  equipe.append(pontuacao)

  dados_equipes.append(equipe)

dados_equipes.sort()
print(dados_equipes)

# cont = 0
# for i in range(0, qtd_fatecs):
#   if dados_equipes[cont][0] == i+1:
#     maior_pontuacao = -1
#     melhor_equipe = 0
#     while dados_equipes[cont][0] == i+1:
#       if dados_equipes[cont][2] > maior_pontuacao:
#         maior_pontuacao = dados_equipes[cont][2]
#         melhor_equipe = dados_equipes[cont][1]
#       cont += 1
#     classificados.append(melhor_equipe)

# fatec_atual = 1
# maior_pontuacao = -1
# melhor_equipe = None
# for i in range(0, qtd_equipes):
#   if dados_equipes[i+1][0] and dados_equipes[i+1][0] != fatec_atual:
#     classificados.append(melhor_equipe)
#     print("classificados updated")
#     print(classificados)
#     maior_pontuacao = -1
#     melhor_equipe = None
#     fatec_atual += 1 
#     print(f"FATEC ATUAL: {fatec_atual}")
  
#   if dados_equipes[i][2] > maior_pontuacao:
#     maior_pontuacao = dados_equipes[i][2]
#     melhor_equipe = dados_equipes[i][1]
#     print(f"melhor equipe updated: {melhor_equipe}")
#   # else:
# ids_fatecs_equipes = []
# for equipe in dados_equipes:

index_equipe = 0
for id_fatec in range(0, qtd_fatecs):
  maior_pontuacao = -1
  melhor_equipe = None
  index_melhor_equipe = None
  if dados_equipes[index_equipe][0] - 1  == id_fatec:
    while dados_equipes[index_equipe][0] - 1 == id_fatec:
      if dados_equipes[index_equipe][2] > maior_pontuacao:
        melhor_equipe   = dados_equipes[index_equipe][1]
        maior_pontuacao = dados_equipes[index_equipe][2]
        index_melhor_equipe = index_equipe
      if index_equipe < len(dados_equipes) - 1:
        index_equipe += 1
      else:
        break

    classificados.append(melhor_equipe)
    dados_equipes.pop(index_melhor_equipe)

for equipe in dados_equipes:
  equipe.reverse()

dados_equipes.sort()

vagas_restantes = vagas - qtd_fatecs
for i in range(0, vagas_restantes):
  classificados.append(dados_equipes[i][1])

print(classificados)