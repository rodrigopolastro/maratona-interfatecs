estaiadas,trelicadas,orcamento = [int(x) for x in input().split()]

combinacoes = list()
for i in range(0,orcamento // estaiadas +1 ):
    if (orcamento - (i * estaiadas)) % trelicadas == 0:
        
        print(i,(orcamento - (i * estaiadas)) // trelicadas)
        exit()
        
        
print("IMPOSSIVEL")