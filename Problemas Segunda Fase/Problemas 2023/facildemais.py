n = int(input())
for i in range(n): 
    posicao_primo = int(input())
    if posicao_primo == 1:
        n = n-1
resposta = 'par' if n % 2 == 0 else 'impar'
print(resposta)