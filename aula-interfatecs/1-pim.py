# Exercício de J da 2ªfase de 2023

entrada = input() # explica o input()
numero_maximo = int(entrada) # explica pq tem que converter para int

resposta = ''
lista_numeros = range(numero_maximo) # gera lista de números

for numero_atual in lista_numeros:
    numero_atual = numero_atual + 1
    resultado = numero_atual % 4

    if resultado == 0:
        resposta = resposta + 'pim' + ' '
    else:
        resposta = resposta + str(numero_atual) + ' '

print(resposta.strip())

## Etapa 1: Onboarding
### Vamos começar explicar começando como mostrar dados na tela e
### obter dados do usuário com Python

## Etapa 2: Baby-steps
### Demonstrar passo a passo a construção em pegar esses dados
### e mostrar o resultado final lógico (sem loop)

## Etapa 3: Looping
### Demonstrar a utilização de loop for (fixo), o funcionamento do range() e concatenar a resposta

## Etapa 4: Pegadinha
### Demonstrar esse código rodando sem o strip que é algumas pegadinhas típicas do boca
### Demonstrar usando um caracter visível como "!" ou "😊"
