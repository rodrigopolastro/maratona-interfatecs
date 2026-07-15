# rodrigo - inicio: 11:20; fim: 11:50 - duração: 30 minutos
from math import sqrt, ceil

primos = dict()

def gera_partes_numero(numero):
    numero_str = str(numero)
    partes = []

    for tamanho_parte in range(1, len(numero_str)+1):
        partes.append(int(numero_str[0:tamanho_parte]))

    return partes

def is_primo(number) -> bool:
    primo_conhecido = primos.get(number, None)
    if primo_conhecido is not None:
        return primo_conhecido

    if number == 2:
        primos[number] = True
        return True

    if number == 1 or number % 2 == 0:
        primos[number] = False
        return False

    for divisor in range(3, ceil(sqrt(number))+1, 2):
        if number % divisor == 0:
            primos[number] = False
            return False

    primos[number] = True
    return True

def is_super_primo(numero):
    partes_numero = gera_partes_numero(numero)
    for parte in partes_numero:
        if not is_primo(parte):
            return False

    return True

qtd_digitos = int(input())

inicio_loop = 10 ** (qtd_digitos-1)
fim_loop = 10 ** qtd_digitos

for numero in range(inicio_loop, fim_loop):
    if is_super_primo(numero):
        print(numero)