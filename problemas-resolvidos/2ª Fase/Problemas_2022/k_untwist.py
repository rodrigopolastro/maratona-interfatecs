from string import ascii_lowercase

matriz = dict()
# def cifra_letra(letra):
#     if letra == 'a':
#         return 1

#     if letra == 'b':
#         return 2

#     # ...

# def criptografa_letra(
#     codigo_letra,
#     chave,
#     tamanho_texto,
#     posicao_letra
# ):
#     (((chave * posicao_letra) % tamanho_texto) - posicao_letra) % 28

    # letra = texto_base[i]

    # codigo_letra = cifra_letra(letra)
    # x = cifra_letra(letra)




    # return (texto_base[(k * i) % n] - i) % 28

# codigo_cifrado = criptografa_letra(
#     [1],
#     5,
#     0
# )

# print(codigo_cifrado)

# chave, mensagem_cifrada = input().split()

# chave = 5

# mensagem_cifrada = 'cs.'

# tamanho_mensagem = len(mensagem_cifrada)

# res = criptografa_letra(
#     codigo_letra,
#     chave,
#     posicao_letra
# )

# print(res)


# codigo_base[i] -> cifra_letra()

# texto_base = ['c', 'a', 't']

# codigo_base = [3, 1, 20]

# codigo_cifrado = [3, 19, 27]

# 'a' -> 1 -> 19 -> 's'


CARACTERES = '-' + ascii_lowercase + '.'

def letra_para_codigo(letra):
    for i in range(len(CARACTERES)):
        if CARACTERES[i] == letra:
            return i

def gera_codigo_base(string):
    codigo_base = list()

    for letra in string:
        codigo = letra_para_codigo(letra)

        codigo_base.append(codigo)

    return codigo_base

def codigo_criptografado(
    codigo_base,
    posicao_letra,
    chave,
):
    tamanho_string = len(codigo_base)

    return (codigo_base[(chave * posicao_letra) % tamanho_string] - posicao_letra) % 28
    # código-cifrado[i] = (código-base[ki mod n] - i) mod 28
    # return 19

def codigo_para_letra(codigo_letra_criptografado):
    if codigo_letra_criptografado == 0:
        return '-'

    if codigo_letra_criptografado == 27:
        return '.'

    return ascii_lowercase[codigo_letra_criptografado-1]

def caminho_completo(
    codigo_base,
    posicao_letra,
    chave,
):
    codigo = codigo_criptografado(codigo_base, posicao_letra, chave)

    letra_cifrada = codigo_para_letra(codigo)

    return letra_cifrada

# def gera_matriz_consulta(string):
#     codigo_base = gera_codigo_base(string)

#     for caractere in CARACTERES:
#         caractere_criptografado = caminho_completo(
#             codigo_base,
#             ,
#             chave
#         )

#         matriz[caractere_criptografado] = caractere

#     return matriz


# print(letra_para_codigo('-'))
# print(letra_para_codigo('.'))
# for letra in ascii_lowercase:

CHAVE = 5
string = 'aaaaa'

# print(gera_matriz_consulta(string))

n = len(string)


codigo_base = gera_codigo_base(string)

for i in range(n):

    print(caminho_completo(codigo_base, i, CHAVE))

    # print(letra, ' -> ', codigo, ' -> ', letra_cifrada)