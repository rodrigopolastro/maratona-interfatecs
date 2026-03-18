# Exercício de J da 2ªfase de 2023

numero = input() # explica o input()
numero = int(numero) # explica pq tem que converter para int

resposta = ''
lista_numeros = range(numero) # gera lista de números
for numero_atual in lista_numeros:
    numero_atual = numero_atual + 1
    resultado = numero_atual % 4
    if resultado == 0:
        resposta = resposta + 'pim' + ' '
    else:
        resposta = resposta + str(numero_atual) + ' '
print(resposta.strip())

# 1

numero = input()
numero = int(input())

