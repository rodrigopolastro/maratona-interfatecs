# qtd = int(input())
# mapa = {}

# # ler
# for _ in range(qtd):
#     entrada = input()
#     a, b = entrada.strip().split(' ')
#     mapa[a] = b

# # procurar ciclo
# n = 0
# tardia = 'usar injecao tardia'

# classes = list(mapa.keys())

# for classe_atual in classes:
#     for classe in classes:
#         deps = []
#         dep = mapa[classe]

#         if dep in deps and dep == classe_atual:
#             print(tardia)
#             exit(0)
        
#         deps.append(dep)
    
# print('ok')

qtd = int(input())
mapa = dict()
for i in range(qtd):
    a,b = input().split()
    if a in mapa.keys():
        mapa[a].append(b)
        continue
    mapa[a] = [b]
livres = []
def livre(mapa:set):
    global livres
    mod = False
    for chave,valor in mapa.items():
        for val in valor:
            if val not in mapa.keys():
                livres.append(val)
                mod = True
    return mod
i = 0
while i < 20000:    
    if not livre(mapa):
        print("usar injecao tardia")
        exit(0)    
    i += 1

print('ok')