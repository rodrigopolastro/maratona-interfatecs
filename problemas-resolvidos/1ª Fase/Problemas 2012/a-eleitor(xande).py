################################################################################
# Objetivo: Determinar se um titulo de eleitor é valido, caso não seja deve exibir qual digito validador correto 
# OBS: botei o nome da variavel de CPF, porém só prestei atenção q não era CPF quando coloquei index que eu vi que tinha 12 digitos :p
# Autor: Alexandre
# Data: 27/01/2025
# Duração: 41min
################################################################################
# inicio - 9:02  / término - 9:43
"""
input ex -> 9999999999-99
regras 
feitas em 2 etapas

1° digito > 
    - multiplica o primeiro digito multiplicado por 9, soma pelo segundo multiplicado por 8 , soma pelo terceiro multiplicado por 7 e assim por diante nos primeiros 8 digitos
    - calcula o resto da divisão por 11 da soma acima
    - o 1° digito é dado por 11 - resto
        - SE o resto for 1 ou 0, deve verificar o nono e décimo digito do cpf se são iguais a 01 ou se invés disso o décimo digito é igual a 2
            - Caso seja, o 1° digito é o inverso do resto anteriormente calculado, se resto for 0 entao o 1° digito é 1 e se  for 1 o 1° digito é 0

2° digito >
    - multiplica o 9° digito por 4, o 10° digito por 3 e o primeiro digito verificador multiplicado por 2, a soma dessas multiplicacoes calcula o resto dessa divisão por 11
    - se esse resto for maior que 1 , o segundo digito verificador é dado pela subtração de 11 - resto
        -Se for igual a 0 ou 1, verificar se o nono e décimo dígitos do título são iguais a 01 ou se, em vez disso, o décimo dígito é igual a 2
        =Caso seja, DV2 é o inverso do resto anteriormente calculado:
            se resto for zero, DV2 = 1; se resto for um, DV2 = 0. Nos casos restantes, o
            segundo dígito verificador é igual a zero. 

"""


def PegarPrimeiroDigitoValidador(cpf : str):
    soma = 0
    for numero in range(8):
        soma += int(cpf[numero]) * (9 - numero)
    resto = soma % 11
    if resto <= 1:
        if cpf[8:10] == '01' or cpf[9] == '2':
            if resto == 0:
                return 1
            else:
                return 0
            
        else:
            return 0
            
    else:
        return 11 - resto

def PegarSegundoDigitoValidador(cpf : str , primeiroDigito : int):
    resto = ((int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (primeiroDigito * 2)) % 11
    if resto == 1 or resto == 0:
        if cpf[8:10] == '01' or cpf[9] == '2':
            if resto == 0:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 11 - resto
while True:
    cpf,digitoValidadorOriginal = input().split('-')
    if cpf == '0000000000' and digitoValidadorOriginal == '00':
        break
    cpf = list(cpf)
    while len(cpf) < 10:
        cpf.insert(0,'0')
    cpf = ''.join(cpf)        
    
    primeiroDigito = PegarPrimeiroDigitoValidador(cpf)
    segundoDigito = PegarSegundoDigitoValidador(cpf, primeiroDigito)

    if str(primeiroDigito)+str(segundoDigito) == digitoValidadorOriginal:
        print('correto')
    else:
        print(str(primeiroDigito)+str(segundoDigito))