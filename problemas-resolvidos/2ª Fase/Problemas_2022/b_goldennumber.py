import decimal

def aplica(soma_atual):
    return 1 + 1/soma_atual

n = int(input())

soma = 1
for _ in range(n):
    soma = aplica(soma)

# Pode ser que haja um problema de precisão aqui na hora de exibir com 15 casas decimais,
# pois, no exemplo do enunciado, n = 3 produz "1.66666662693", mas meu código produz "1.666666666666667"
print(f"{soma:.15f}")
