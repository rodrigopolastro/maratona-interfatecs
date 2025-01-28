################################################################################
# Objetivo: Determinar qual possivel sequencia numerica de um boleto com tecla defeituosa
# Autor: Alexandre
# Data: 27/01/2025
# Duração: 16 min
################################################################################
## inicio 9:44 / término: 10:00 

def contemApenasZeros(codigoBoleto:str):
    for caractere in codigoBoleto:
        if caractere != '0':
            return False
    return True
def refatoraZerosEsquerda(codigoboleto:str):
    if codigoboleto[0] == '0':
        codigoboleto = list(codigoboleto)
        itsLeftZero = True
        index = 0
        while True:
            if codigoboleto[index] == '0' and itsLeftZero:
                codigoboleto.pop(index)
            else:
                break
        return ''.join(codigoboleto)
                
    else:
        return codigoboleto
    
while True:
    teclaDefeituosa,codigoBoleto=input().split()
    if teclaDefeituosa == '0' and codigoBoleto == '0':
        break
    codigoBoleto = codigoBoleto.replace(teclaDefeituosa,'')
    if contemApenasZeros(codigoBoleto):
        print("0")
    else:
        print(refatoraZerosEsquerda(codigoBoleto))

