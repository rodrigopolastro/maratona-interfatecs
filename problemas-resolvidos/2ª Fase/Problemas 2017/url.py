# incompleta / falha (decodificação ok)(codificacao falha)
import string
lista_codificar = [i for i in string.ascii_lowercase]
lista_codificar = [i for i in string.ascii_uppercase]

dicionario = {}
contador =0
for i in string.ascii_lowercase:
    dicionario[i] = contador
    contador+=1
for i in string.ascii_uppercase:
    dicionario[i]=contador
    contador+=1
numeros = list('0123456789')
lista_codificar = [i for i in numeros]
for i in numeros:
    dicionario[i]=contador
    contador+=1
def decodificar(palavra:str):
    potencia = len(palavra)-1
    retornar = 0
    for letra in palavra:
        retornar += dicionario[letra]*62**potencia
        potencia -=1
    return retornar

def codificar(numero:int):
    max_pow = 6
    contador = 0
    lista = []
    while True:
        if numero == 0:
            break
        elif (62**max_pow)-1 == numero:
            return 1
        elif 62**max_pow <= numero:
            contador += 1
            numero -= 62**max_pow
            continue
        elif contador == 0:
            max_pow -=1
        else:
            lista.append(f'{contador}x62**{max_pow}')
            contador = 0
            max_pow -=1

    print(lista)

        
        
codificar(125)
   
    
