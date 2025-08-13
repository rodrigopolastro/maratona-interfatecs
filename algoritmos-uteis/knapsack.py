# """
# Knapsack - melhor combinação de itens - existem algumas variações desse algoritmo mas em suma vai estar aqui os principais
# * 0/1 knapsack - Se resume no famoso algoritmo da mochila, tenho itens de diferentes valores em um espaço determinado, qual melhor combinação de
# * itens onde eu levo o maior valor sem repetir os itens? uma variante de programação que existe é 0/1 com 'backtraking' que é voltar quais itens
# * foram escolhido

# * Unbouded Knapsack - o mesmo de 0/1 com o diferencial que, não restringimos a pegar apenas um, podemos pegar ilimitado, e assim como o 0/1
# * temos tecnica de backtracking dele tambem

# """



# #Fixado valor fixado
# def knapsack_1_0_SEM_BACKTRACKING():
#     capacidadeBolsa = 10 
#     peso_itens = [2,3,5,7]
#     valores_itens = [3,5,10,13]
#     bolsa = [
#         [0 for _ in range(capacidadeBolsa+1)] for x in range(len(peso_itens) +1)
#     ]
#     for i in range(1,len(peso_itens)+1):        # precisamos percorrer todos os itens, começamos do 1 para ficar mais fácil o algoritmo
#         for j in range(1,capacidadeBolsa+1):    # não tem necessidade de começar com espaço 0, não vai caber nada,
#                                                 # a não ser que exista itens com 0 de peso mas não vai ser o caso dos problemas de knapsack
#                                                 # então já começamos do 1
#             if j - peso_itens[i-1] >= 0: # o item cabe
#                 # precisamos ver agora se é mais vantajoso pegar ou não pegar
#                 bolsa[i][j] = max(
#                     bolsa[i-1][j] , # não pegar
#                     valores_itens[i-1] + bolsa[i-1][j - peso_itens[i-1]]) # pegar e somar com a melhor combinação do item anterior
#             else: #se não cabe, pegamos a melhor combinação que deu com o item anterior
#                 bolsa[i][j] = bolsa[i-1][j]
#     melhorItem = bolsa[-1][-1] # a maior soma vai ser o ultimo item da bolsa, que é onde ele validou todos os itens e todas capacidades
#     print(melhorItem)







# def knapsack_1_0_COM_BACKTRACKING():
#     # usa a mesma estrutura do knapsack, então desse comentário até o próximo é uma copia da lógica acima
    
#     capacidadeBolsa = 10 
#     peso_itens = [2,3,5,7]
#     valores_itens = [3,5,10,13]
#     bolsa = [
#         [0 for _ in range(capacidadeBolsa+1)] for x in range(len(peso_itens) +1)
#     ]
#     for i in range(1,len(peso_itens)+1):    
#         for j in range(1,capacidadeBolsa+1):
#             if j - peso_itens[i-1] >= 0: 
#                 bolsa[i][j] = max(
#                     bolsa[i-1][j] ,
#                     valores_itens[i-1] + bolsa[i-1][j - peso_itens[i-1]])
#             else:
#                 bolsa[i][j] = bolsa[i-1][j]
#     melhorItem = bolsa[-1][-1]
    
#     # fim do algoritmo principal
#     # agora vem o diferencial do backtracking
#     # calma, esqueci como fazer o backtracking, ter q reaprender e outrora termino isso, mas basicamente é voltando valores

#     CapacidadeDisponivel = capacidadeBolsa # mesmo valor, só estou reatribuindo para ficar claro que é o mesmo valor
    





# def knapsack_unbouded():
#     capacidadeBolsa = 20 
#     peso_itens = [2,3,5,7]
#     valores_itens = [3,5,10,13]
#     dp = [0 for _ in range(capacidadeBolsa+1)] 
    
        
#     for j in range(1, capacidadeBolsa+1):  
#         for i in range(len(peso_itens)):   
#             if j - peso_itens[i] >= 0:
#                 dp[j] = max(dp[j] , valores_itens[i] + dp[j - peso_itens[i]])
#     print(max(dp))
    
    
    
# knapsack_unbouded()


""" CHAT GEPETO , CÓDIGO COM BACKTRACKING """

# KNAPSACK I/O -> pega maior valor otimizando pelo peso, apenas 1 único item de cada

# ===== ENTRADA =====
n = int(input("Número de itens: "))
capacidade = int(input("Capacidade da mochila: "))
pesos = list(map(int, input("Pesos: ").split()))
valores = list(map(int, input("Valores: ").split()))

dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

# ===== PREENCHIMENTO DA TABELA DP =====
for i in range(1, n + 1):
    for w in range(capacidade + 1):
        if pesos[i - 1] <= w:
            dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
        else:
            dp[i][w] = dp[i - 1][w]

# ===== BACKTRACKING PARA ENCONTRAR OS ITENS ESCOLHIDOS =====
w = capacidade
itens_escolhidos = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        itens_escolhidos.append(i - 1)  # salva o índice do item
        w -= pesos[i - 1]               # reduz a capacidade

# ===== SAÍDA =====
print("\nMelhor valor possível:", dp[n][capacidade])
print("Itens escolhidos (índices):", list(reversed(itens_escolhidos)))
print("Pesos escolhidos:", [pesos[i] for i in reversed(itens_escolhidos)])
print("Valores escolhidos:", [valores[i] for i in reversed(itens_escolhidos)])









# KNAPSACK UNBOUDED -> pega o maior valor que cabe naquela capacidade podendo pegar infinitos numeros
def knapsack_unbounded():
    capacidadeBolsa = 20
    peso_itens = [2, 3, 5, 7]
    valores_itens = [3, 5, 10, 13]
    dp = [0 for _ in range(capacidadeBolsa + 1)]
    escolha = [-1 for _ in range(capacidadeBolsa + 1)]  # pra guardar qual item foi escolhido em cada capacidade

    # Preenchendo dp e escolha
    for j in range(1, capacidadeBolsa + 1):
        for i in range(len(peso_itens)):
            if j - peso_itens[i] >= 0:
                val = valores_itens[i] + dp[j - peso_itens[i]]
                if val > dp[j]:
                    dp[j] = val
                    escolha[j] = i  # guarda o índice do item que melhorou o valor

    print("Valor máximo:", dp[capacidadeBolsa])

    # Backtracking para descobrir os itens usados
    j = capacidadeBolsa
    itens_usados = []
    while j > 0 and escolha[j] != -1:
        i = escolha[j]
        itens_usados.append(i)
        j -= peso_itens[i]

    print("Itens usados (índices):", itens_usados)
    print("Pesos dos itens usados:", [peso_itens[i] for i in itens_usados])
    print("Valores dos itens usados:", [valores_itens[i] for i in itens_usados])


knapsack_unbounded()




# bounded knapsack -> maior valor com determinado numeros de cada item
def bounded_knapsack(pesos, valores, quantidades, capacidade):
    n = len(pesos)
    # dp[i][w] = melhor valor usando itens 0..i-1 com capacidade w
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    
    # Para armazenar quantas unidades do item i foram usadas para dp[i][w]
    escolha = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        peso = pesos[i-1]
        valor = valores[i-1]
        max_q = quantidades[i-1]
        for w in range(capacidade + 1):
            dp[i][w] = dp[i-1][w]  # sem pegar o item i
            escolha[i][w] = 0
            # tentar pegar k unidades do item i
            for k in range(1, max_q + 1):
                if k * peso <= w:
                    val = dp[i-1][w - k*peso] + k*valor
                    if val > dp[i][w]:
                        dp[i][w] = val
                        escolha[i][w] = k  # quantidade escolhida do item i

    # Backtracking para recuperar os itens usados
    w = capacidade
    itens_usados = [0] * n
    for i in range(n, 0, -1):
        k = escolha[i][w]
        itens_usados[i-1] = k
        w -= k * pesos[i-1]

    print("Valor máximo:", dp[n][capacidade])
    print("Itens usados (quantidades):", itens_usados)


# Exemplo de uso
pesos = [2, 3, 4]
valores = [3, 4, 5]
quantidades = [3, 2, 1]
capacidade = 10

bounded_knapsack(pesos, valores, quantidades, capacidade)





# subset -> caso especial do knapsack, onde só importa o peso,  "É possível encher a mochila exatamente com peso W?"

def subset_sum_backtrack(nums, target, index=0, current_sum=0, subset=[]):
    # Se soma atual iguala o target, achamos uma solução
    if current_sum == target:
        print("Subset encontrado:", subset)
        return True
    # Se soma passar do target ou acabarem os números, volta
    if current_sum > target or index == len(nums):
        return False
    
    # Tenta incluir o número atual
    if subset_sum_backtrack(nums, target, index + 1, current_sum + nums[index], subset + [nums[index]]):
        return True
    
    # Tenta não incluir o número atual
    if subset_sum_backtrack(nums, target, index + 1, current_sum, subset):
        return True
    
    return False

# Exemplo de uso
nums = [3, 34, 4, 12, 5, 2]
target = 9

if not subset_sum_backtrack(nums, target):
    print("Nenhum subset encontrado que some", target)
    
    
    
    
    
    
    
    
# multi-dimensional knapsack -> se você tiver que considerar restriçoes (como peso) em duas ou mais dimensoes, então pense que para cada item você tem peso e volume, onde cada um tem seu armazenamento restrito etc

def multidimensional_knapsack(pesos, valores, capacidades):
    # pesos: lista de itens, cada item é uma lista com pesos por dimensão
    # valores: lista de valores dos itens
    # capacidades: lista das capacidades máximas por dimensão

    n = len(valores)
    d = len(capacidades)  # número de dimensões
    
    # Criar dp como d-dimensional dict para economizar memória
    # Usaremos um dict: chave = tupla das capacidades restantes
    dp = {}
    escolha = {}

    def solve(i, capacidades_rest):
        if i == n:
            return 0
        if (i, capacidades_rest) in dp:
            return dp[(i, capacidades_rest)]
        
        # Não pegar o item i
        max_val = solve(i + 1, capacidades_rest)
        escolha[(i, capacidades_rest)] = 0
        
        # Tentar pegar o item i, se couber
        pode_pegar = True
        novas_cap = []
        for dim in range(d):
            if pesos[i][dim] > capacidades_rest[dim]:
                pode_pegar = False
                break
            novas_cap.append(capacidades_rest[dim] - pesos[i][dim])
        
        if pode_pegar:
            val_com_item = valores[i] + solve(i + 1, tuple(novas_cap))
            if val_com_item > max_val:
                max_val = val_com_item
                escolha[(i, capacidades_rest)] = 1
        
        dp[(i, capacidades_rest)] = max_val
        return max_val
    
    valor_max = solve(0, tuple(capacidades))
    
    # Backtracking para descobrir itens escolhidos
    capac_rest = tuple(capacidades)
    itens_escolhidos = []
    for i in range(n):
        if escolha.get((i, capac_rest), 0) == 1:
            itens_escolhidos.append(i)
            capac_rest = tuple(capac_rest[dim] - pesos[i][dim] for dim in range(d))
    
    print("Valor máximo:", valor_max)
    print("Itens escolhidos:", itens_escolhidos)


# Exemplo de uso
pesos = [
    [2, 3],  # item 0: peso dimensão 1=2, dimensão 2=3
    [3, 4],
    [4, 2],
    [5, 3]
]
valores = [3, 4, 5, 6]
capacidades = [7, 7]

multidimensional_knapsack(pesos, valores, capacidades)





# fractional knapsack -> pode pegar valores quebrados como 0.3 , 1/2 etc..

def fractional_knapsack(pesos, valores, capacidade):
    n = len(pesos)
    itens = []
    
    # Criar lista com valor por peso e índices
    for i in range(n):
        itens.append((valores[i] / pesos[i], pesos[i], valores[i]))
    
    # Ordenar por valor/peso decrescente
    itens.sort(key=lambda x: x[0], reverse=True)
    
    valor_total = 0.0
    capacidade_restante = capacidade
    
    for vp, peso, valor in itens:
        if peso <= capacidade_restante:
            # Pega o item inteiro
            valor_total += valor
            capacidade_restante -= peso
        else:
            # Pega fração do item
            fração = capacidade_restante / peso
            valor_total += valor * fração
            capacidade_restante = 0
            break
    
    print("Valor máximo que pode ser levado:", valor_total)

# Exemplo
pesos = [10, 20, 30]
valores = [60, 100, 120]
capacidade = 50

fractional_knapsack(pesos, valores, capacidade)



















