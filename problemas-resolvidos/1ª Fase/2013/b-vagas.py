# inciio: (10min) (não pensei no caso de descartar negativos)
# 13/04

while True:
    comprimento = int(input())
    if comprimento == -1: break
    
    qtdCarros = (comprimento - 6) // 5
    print(max(0, qtdCarros))