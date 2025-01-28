################################################################################
# Objetivo: Imprimir resultado de somas em números romanos
# Autor: Rodrigo
# Data: 27/01/2025
# Duração: inicio 21:45 - 22:20
################################################################################


numeroInputs = int(input())
for _ in range(numeroInputs):
    valores = input().split()
    soma = int(valores[0]) + int(valores[1])
    
    if soma < 1 or soma > 3999:
        print('*****')
        continue
        
    numZeros = 4 - len(str(soma))
    somaStr = numZeros * "0" + str(soma)
    
    strFinal = ''
    
    m, c, d, u = [int(x) for x in list(somaStr)]
 
    strFinal += m * 'M'
    
    if c in [1,2,3]:
        strFinal += c * "C"    
    elif c == 4:
        strFinal += "CD"
    elif c == 5:
        strFinal += "D"
    elif c in [6, 7, 8]:
        strFinal += "D" + (c - 5) * "C"
    elif c == 9:
        strFinal += "CM" 
        
    if d in [1,2,3]:
        strFinal += d * "X"    
    elif d == 4:
        strFinal += "XL"
    elif d == 5:
        strFinal += "L"
    elif d in [6, 7, 8]:
        strFinal += "L" + (d - 5) * "X"
    elif d == 9:
        strFinal += "XC"  
        
    
    if u in [1,2,3]:
        strFinal += u * "I"    
    elif u == 4:
        strFinal += "IV"
    elif u == 5:
        strFinal += "V"
    elif u in [6, 7, 8]:
        strFinal += "V" + (u - 5) * "I"
    elif u == 9:
        strFinal += "IX"                                    
    
    print(strFinal)