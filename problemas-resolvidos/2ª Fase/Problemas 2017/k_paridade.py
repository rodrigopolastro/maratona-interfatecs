# alexandre 08/09    19:12 - 19:15
def quantidade_impar(linha:str):
    contador = 0
    for i in linha:
        if int(i) % 2 == 1:
            contador+=1
    return contador
def quantidade_par(linha:str):
    contador = 0
    for i in linha:
        if int(i)%2 == 0:
            contador +=1
    return contador


def main():
    numero = input()
    print(f'{len(numero)}{quantidade_par(numero)}{quantidade_impar(numero)}')
main()