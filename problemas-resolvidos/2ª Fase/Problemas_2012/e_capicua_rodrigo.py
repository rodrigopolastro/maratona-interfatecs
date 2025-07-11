from math import sqrt

while True:
    numero = int(input())
    if numero == 0:
        break
    if int(str(sqrt(numero)).split('.')[1]) == 0 and str(numero) == str(numero)[::-1]:
        print('S')
    else:
        print('N')