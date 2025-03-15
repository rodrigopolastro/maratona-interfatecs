casosteste = int(input())
for _ in range(casosteste):
    matriz = int(input())
    total = matriz * matriz
    qtd_0 = 0
    qtd_n_0 = matriz + (matriz-1) + (matriz-1)
    qtd_0 = total - qtd_n_0
    if qtd_0 > qtd_n_0:
        print(f"S {qtd_0}")
    else:
        print(f"N {qtd_0}")
        
# 1:27 - 1:40 