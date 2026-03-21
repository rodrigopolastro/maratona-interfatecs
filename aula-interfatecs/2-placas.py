# Exercício M da 1ª fase de 2013

n = int(input()) # qtd d casos de teste

def nerdOuNao(string):
    for chr in string:
        if chr not in '10iIoO':
            return False
    return True

for _ in range(n):
    if(nerdOuNao(input())):
        print("NERD!")
    else:
        print("Normal")

## Etapa 1: revisão
### Executar a lógica sem looping, funcionamento do "in"

## Etapa 2: looping e função
### Adicionar looping e facilidade de uso de uma definição da função
