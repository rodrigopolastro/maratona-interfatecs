from math import sqrt, tan, radians

entrada = input().split()
xCanhao = float(entrada[0])
yCanhao = float(entrada[1])
anguloCanhao = float(entrada[2])
xAlvo = float(entrada[3])
yAlvo = float(entrada[4])
raioAlvo = float(entrada[5])

def distancia_reta_ponto(a, b, c, xPonto, yPonto):
    numerador = abs(a*xPonto + b*yPonto + c)
    denominador = sqrt(a**2 + b**2)
    
    return numerador/denominador



a = -tan(radians(anguloCanhao))
b = 1
c = tan(radians(anguloCanhao))*xCanhao - yCanhao
distancia_reta_alvo = distancia_reta_ponto(a, b, c, xAlvo, yAlvo)
print(distancia_reta_alvo)

if distancia_reta_alvo > raioAlvo:
    print('Não Atingido')
elif distancia_reta_alvo == 0:
    print('Atingido Fatalmente')
else:
    movimentar = raioAlvo - distancia_reta_alvo
    print('Atingido')
    print(f"{movimentar:.2f}")
#caso 1: 590.00 489.00 70.64 590.00 489.00 98.64
#caso 2: 981.00 285.00 238.54 1015.82 281.81 37.13
#caso 3: 131.00 206.00 162.88 763.00 484.00 7.74