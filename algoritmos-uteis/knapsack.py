"""
Knapsack - melhor combinação de itens - existem algumas variações desse algoritmo mas em suma vai estar aqui os principais
* 0/1 knapsack - Se resume no famoso algoritmo da mochila, tenho itens de diferentes valores em um espaço determinado, qual melhor combinação de
* itens onde eu levo o maior valor sem repetir os itens? uma variante de programação que existe é 0/1 com 'backtraking' que é voltar quais itens
* foram escolhido

* Unbouded Knapsack - o mesmo de 0/1 com o diferencial que, não restringimos a pegar apenas um, podemos pegar ilimitado, e assim como o 0/1
* temos tecnica de backtracking dele tambem

"""



#Fixado valor fixado
def knapsack_1_0_SEM_BACKTRACKING():
    
    capacidadeBolsa = 10 
    peso_itens = [2,3,5,7]
    valores_itens = [3,5,10,13]
    
    bolsa = [
        [0 for _ in range(capacidadeBolsa+1)] for x in range(len(peso_itens) +1)
    ]
    
    for i in range(1,len(peso_itens)+1):        # precisamos percorrer todos os itens, começamos do 1 para ficar mais fácil o algoritmo
        for j in range(1,capacidadeBolsa+1):    # não tem necessidade de começar com espaço 0, não vai caber nada,
                                                # a não ser que exista itens com 0 de peso mas não vai ser o caso dos problemas de knapsack
                                                # então já começamos do 1
            if j - peso_itens[i-1] >= 0: # o item cabe
                # precisamos ver agora se é mais vantajoso pegar ou não pegar
                bolsa[i][j] = max(
                    bolsa[i-1][j] , # não pegar
                    valores_itens[i-1] + bolsa[i-1][j - peso_itens[i-1]]) # pegar e somar com a melhor combinação do item anterior
            else: #se não cabe, pegamos a melhor combinação que deu com o item anterior
                bolsa[i][j] = bolsa[i-1][j]
    melhorItem = bolsa[-1][-1] # a maior soma vai ser o ultimo item da bolsa, que é onde ele validou todos os itens e todas capacidades
    print(melhorItem)







def knapsack_1_0_COM_BACKTRACKING():
    # usa a mesma estrutura do knapsack, então desse comentário até o próximo é uma copia da lógica acima
    
    capacidadeBolsa = 10 
    peso_itens = [2,3,5,7]
    valores_itens = [3,5,10,13]
    bolsa = [
        [0 for _ in range(capacidadeBolsa+1)] for x in range(len(peso_itens) +1)
    ]
    for i in range(1,len(peso_itens)+1):    
        for j in range(1,capacidadeBolsa+1):
            if j - peso_itens[i-1] >= 0: 
                bolsa[i][j] = max(
                    bolsa[i-1][j] ,
                    valores_itens[i-1] + bolsa[i-1][j - peso_itens[i-1]])
            else:
                bolsa[i][j] = bolsa[i-1][j]
    melhorItem = bolsa[-1][-1]
    
    # fim do algoritmo principal
    # agora vem o diferencial do backtracking
    # calma, esqueci como fazer o backtracking, ter q reaprender e outrora termino isso, mas basicamente é voltando valores

    CapacidadeDisponivel = capacidadeBolsa # mesmo valor, só estou reatribuindo para ficar claro que é o mesmo valor
    





def knapsack_unbouded():
    capacidadeBolsa = 20 
    peso_itens = [2,3,5,7]
    valores_itens = [3,5,10,13]
    dp = [0 for _ in range(capacidadeBolsa+1)] 
    
        
    for j in range(1, capacidadeBolsa+1):  
        for i in range(len(peso_itens)):   
            if j - peso_itens[i] >= 0:
                dp[j] = max(dp[j] , valores_itens[i] + dp[j - peso_itens[i]])
    print(max(dp))
    
    
    
knapsack_unbouded()