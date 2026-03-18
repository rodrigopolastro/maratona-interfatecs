
from string import ascii_uppercase

def ordem(t: str) -> int:
    return ascii_uppercase.index(t)

def encontra_cifra(texto: str) -> str:
    dois = texto[len(texto)-2:]
    a, b = ordem(dois[0]), ordem(dois[1])

    if b - a == 1:
        return 'SPQR'

    return 'AVE'

def encontra_deslocamento(texto: str, cifra: str) -> int:
    n_cifra = len(cifra)
    diferencial = texto[-n_cifra]
    a, b = ordem(cifra[0]), ordem(diferencial)
    return abs(a - b)

def descrifra(entrada: str) -> str:
    if len(entrada) <= 2:
        return entrada
    
    cifra = encontra_cifra(entrada)
    deslo = encontra_deslocamento(entrada, cifra)
    resultado = ""

    for i, letra in enumerate(entrada):
        if letra not in ascii_uppercase:
            resultado += letra
            continue
        ordem = ascii_uppercase.index(letra)
        posi = (ordem - deslo)        
        resultado += ascii_uppercase[posi]

    return resultado

while True:
    entrada = input().strip()
    if entrada == '***':
        break
    print(descrifra(entrada))

# print(ord('A'))
# print(ord("Z"))
# alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# def detDesc(ch1,ch2):
#     return ord(ch2)%26 - ord(ch1)%26
# def converter(palavra,deslocamento):
#     resp = ""
#     for p in palavra:
#         if p in alfabeto:
#             v = ord(p) + deslocamento
#             if v < 65:
#                 c = chr(v+26)
#             elif v > 90:
#                 c = chr(v-26)
#             else:
#                 c = chr(v)
#             resp += c
#         else:
#             resp+=p
#     if deslocamento == 1 or deslocamento == -1:
#         resp+= 'AVE'
#     else:
#         resp+= 'SPQR'
#     return resp
        
        
# while True:
#     entrada = input()
#     if entrada == '***':
#         break
#     else:
#         desloc = detDesc(entrada[-2],entrada[-1])
#         print(desloc)
#         print(converter(entrada,desloc))
    


