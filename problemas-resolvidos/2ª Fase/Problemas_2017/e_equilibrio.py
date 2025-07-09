valores = {
    " ": 1,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 13,
    "o": 12,
    "p": 11,
    "q": 10,
    "r": 9,
    "s": 8,
    "t": 7,
    "u": 6,
    "v": 5,
    "w": 4,
    "x": 3,
    "y": 2,
    "z": 1,
    "0": 1,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

menor_diferenca = None
pos_menor_diferenca = []

string = input().lower()
# string = "String para teste1".lower()
lista_valores = []
for char in string:
    lista_valores.append(valores[char])
ponteiro = 0

if len(lista_valores) == 2:

    if lista_valores[0] > 2 * lista_valores[1]:
        print('1')
        ponteiro = 1
    elif lista_valores[1] > 2 * lista_valores[0]:
        print('2')
        ponteiro = 1

soma_total = sum(lista_valores)
if ponteiro == 0:
    for i in range(len(lista_valores)-1):

        soma_esq = sum(lista_valores[:i+1])
        soma_dir = sum(lista_valores[i+1:])
        diferenca = soma_esq - soma_dir
        # print(soma_esq, ' - ', soma_dir)

        if diferenca < 0: diferenca = -diferenca
        if menor_diferenca == None or diferenca < menor_diferenca:
            menor_diferenca = diferenca
            pos_menor_diferenca = [i+1, i+1+1]

        if len(lista_valores) > 2 and i == len(lista_valores)-2: break
        soma_esq = sum(lista_valores[:i+1])
        soma_dir = sum(lista_valores[i+1+1:]) 
        diferenca = soma_esq - soma_dir

        if diferenca < 0: diferenca = -diferenca
        if menor_diferenca == None or diferenca < menor_diferenca:
            menor_diferenca = diferenca
            pos_menor_diferenca = [i+1+1]

    if len(pos_menor_diferenca) == 1:
        print(pos_menor_diferenca[0])
    else:
        print(f"{pos_menor_diferenca[0]},{pos_menor_diferenca[1]}")
