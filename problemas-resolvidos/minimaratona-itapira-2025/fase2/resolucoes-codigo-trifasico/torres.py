discos = int(input())
entrada = input().replace(' ', '')
movimentosFeitos = int(entrada, base=2)
qtdTotal = 2**discos - 1
print(qtdTotal - movimentosFeitos)