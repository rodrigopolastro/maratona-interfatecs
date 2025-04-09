qtdNum , tipo = input().lower().split()
import string
minusculas = string.ascii_lowercase
maiusculas = string.ascii_uppercase
resposta = ''
for _ in range(0,int(qtdNum)):
    if tipo == 'maiusculas': 
        print('.'*(24-(_-1)) + maiusculas[0:_+1])
    else:
        print('.'*(24-(_-1)) +minusculas[0:_+1])

