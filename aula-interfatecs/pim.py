numero_maximo = int(input())
resposta = ''

lista_numeros = range(numero_maximo)

for numero in lista_numeros:
    numero = numero + 1
    resultado = numero % 4
    if resultado == 0:
        resposta = resposta + "pim "
    else:
        resposta = resposta + str(numero) + " "

print(resposta.strip())
