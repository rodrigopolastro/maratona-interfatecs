# incompleta / falha (decodificação ok)(codificacao falha)
#feita em outro dia 
import string
lista_codificar = string.ascii_lowercase+string.ascii_uppercase+string.digits

dicionario = {}
contador =0
for i in string.ascii_lowercase:
    dicionario[i] = contador
    contador+=1
for i in string.ascii_uppercase:
    dicionario[i]=contador
    contador+=1
for i in string.digits:
    dicionario[i] = contador
    contador+=1
def decodificar(palavra:str):
    potencia = len(palavra)-1
    retornar = 0
    for letra in palavra:
        retornar += dicionario[letra]*62**potencia
        potencia -=1
    return retornar

def codificar(numero:int):
    BASE = 62
    url = ''
    while numero != 0:
        url+=lista_codificar[numero%62]
        numero = numero // 62
        # url+=
    return url[::-1]
    # CONVERTER PARA BASE 62

        
def main():
    entrada = input().split(' ')
    if entrada[0]=='C':
        print(codificar(int(entrada[1])))
    else:
        print(decodificar(entrada[1]))
main()
   
    
