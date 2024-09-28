numero_influenciados = 0
influenciados = []

def influencia_redor(linha, coluna):
    for inc_linha in [-1, 0, 1]:
        for inc_coluna in [-1, 0, 1]:
            alvo = [linha+inc_linha, coluna+inc_coluna]
            if 0 <= alvo[0] <= linhas_sala-1 and 0 <= alvo[1] <= colunas_sala-1:
                if not sala_de_aula[alvo[0]][alvo[1]]["foi_influenciado"] and sala_de_aula[linha][coluna]["nivel_influencia"] > sala_de_aula[alvo[0]][alvo[1]]["nivel_influencia"]:
                    sala_de_aula[alvo[0]][alvo[1]]["foi_influenciado"] = True
                    influenciados.append([alvo[0]+1, alvo[1]+1])
                    global numero_influenciados
                    numero_influenciados += 1 

linhas_sala, colunas_sala = list(map(int,input().split(' ')))
quantidade_alunos = linhas_sala * colunas_sala

sala_de_aula = []
for _ in range(linhas_sala):
    linha = [
        {
        "foi_analisado": False,
        "foi_influenciado": False,
        "nivel_influencia": 0
        } for _ in range(colunas_sala)
    ]
    sala_de_aula.append(linha)

linha_luiz, coluna_luiz = list(map(int,input().split(' ')))
sala_de_aula[linha_luiz-1][coluna_luiz-1]["foi_influenciado"] = True
numero_influenciados = 1
influenciados.append([linha_luiz, coluna_luiz])

#le nivel de influencia de cada aluno da sala
for linha in range(linhas_sala): 
    colunas = list(map(int, input().split(' ')))
    for coluna, nivel_influencia in enumerate(colunas):
        sala_de_aula[linha][coluna]["nivel_influencia"] = int(nivel_influencia)

continuar_busca = True
while continuar_busca:
    continuar_busca = False
    for linha in range(linhas_sala):
        for coluna in range(colunas_sala):
            
            if sala_de_aula[linha][coluna]["foi_influenciado"]:
                if not sala_de_aula[linha][coluna]["foi_analisado"]:
                    continuar_busca = True
                sala_de_aula[linha][coluna]["foi_analisado"] = True 
                influencia_redor(linha, coluna)     
                 
if numero_influenciados > quantidade_alunos/2:
    print(numero_influenciados, ' maioria')
else:
    print(numero_influenciados)   