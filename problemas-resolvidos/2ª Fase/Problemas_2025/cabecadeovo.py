inicio, fim = [int(x) for x in input().split()]

def somar(n):
    n = str(n)
    n = [int(x) for x in n]
    
    return sum(n)


ind = 0
maior = 0
for number in  range(fim//10,fim+1):
    resultado = somar(number)
    if somar(number) > maior:
        # print("MAIOR ENC")
        # print(somar(number))
        maior = resultado
        ind = number
        
        
        
print(ind)