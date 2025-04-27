"""
até 107 margem de erro de 7 caso contrario 7%

"""
velocidade = int(input())
if velocidade <= 107:
    print(velocidade + 7)
else:
    print(round(velocidade + (velocidade * (7/100))))


    
