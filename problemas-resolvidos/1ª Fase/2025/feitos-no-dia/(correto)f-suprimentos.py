# anterior = 0
# cargasFaltantes = 0

# n = int(input())

# for _ in range(n):
#     valor = int(input())
#     atual = anterior + valor
#     if atual < 0:
#         cargasFaltantes += abs(atual)
#         atual += cargasFaltantes
#     anterior = atual

# print(cargasFaltantes)

qtd = int(input())
armazenar = []
for _ in range(qtd):
    armazenar.append(int(input()))

qtdMinima = 0
somatotalatual = 0
for x in armazenar:
    somatotalatual += x
    if somatotalatual < 0:
        qtdMinima += abs(somatotalatual)
        somatotalatual =0
print(qtdMinima)

