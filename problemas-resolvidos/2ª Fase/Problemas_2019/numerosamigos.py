sequencia , primeiroNumero = [int(x) for x in input().split()]

def quantidadeDivisores(numero):
    return [x for x in range(1,numero) if numero % x == 0]

soma1 = primeiroNumero

for _ in range(sequencia):
    soma1 = sum(quantidadeDivisores(soma1))
    
if primeiroNumero == soma1:
    print('sim')
else:
    print('nao')


    