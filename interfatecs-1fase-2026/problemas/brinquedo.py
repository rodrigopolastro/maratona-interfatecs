qtd_blocos, qtd_conjuntos = map(int, input().split())

soma_total = ((qtd_blocos + 1) * qtd_blocos) / 2 
if soma_total % qtd_conjuntos != 0:
    print("IMPOSSIVEL")
    exit()

soma_conjunto = int(soma_total / qtd_conjuntos)
if soma_conjunto < qtd_blocos:
    print("IMPOSSIVEL")
    exit()

print("POSSIVEL")