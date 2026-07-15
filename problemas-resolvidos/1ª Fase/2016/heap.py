import math

while True:
    try:
        entrada = input()
        if not entrada:
            exit()
        valores = list(map(int,entrada.split()))
        valores = valores[1:]

        nenhum = 0
        def compHeap(n, v):
            if n + v == 0:
                return False

        def verificaHeap(lista =[], nivel = 0, heap = 0):
            global nenhum
            
            if heap == 999:
                return 999
            
            lim = (2**nivel-1)+2**nivel
            if len(valores)<lim:
                lim = len(valores)
            nLista = valores[2**nivel-1:lim]
            if nivel == 0:
                return verificaHeap(nLista, nivel+1, heap)
            else:
                for n in range(len(nLista)):
                    if nLista[n]>nLista[math.ceil((n+1)/2)]:
                        nHeap = -1
                    else:
                        nHeap = 1
                    if compHeap(nHeap,  heap):
                        return 999
                    heap = nHeap
                if lim == len(valores):
                    return heap
                return verificaHeap(nLista, nivel+1, heap)
        # nenhum = 0
        verifica = verificaHeap()
        if (verifica == 999):
            print("nada")
        elif (verifica == 1):
            print("max")
        else:
            print("min") 
    except EOFError:
        pass