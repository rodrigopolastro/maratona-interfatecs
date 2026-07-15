################################################################################
# Objetivo:
#
# Autor: Rodrigo
# Data: 13/05/2026
# Duração: 25 minutos
################################################################################
 
try:
    while True:
        comandos = list()
        entrada = input()
        if not entrada:
            break

        for dado in entrada.split('<'):
            if not dado:
                continue
            valor  = dado.split('>')
            comando = valor[0]
            parametro = None
            if len(valor) > 1:
                parametro = valor[1]
            comandos.append([comando, parametro])

        cadeia = ''
        saida = ''
        for comando_parametro in comandos:
            comando, parametro = comando_parametro
            if comando == 'I':
                letra = parametro
                cadeia = cadeia + letra
            elif comando == 'A':
                if len(cadeia) > 0:
                    cadeia = cadeia[:len(cadeia)-1] # remove o último caractere
            elif comando == 'L':
                ultima_letra = cadeia[-1]
                cadeia = cadeia + ultima_letra
            elif comando == 'IS':
                saida = saida + cadeia
            elif comando == 'II':
                saida = saida + cadeia[::-1]
            elif comando == 'IN':
                inicio_impressao = int(parametro)
                saida = saida + cadeia[inicio_impressao-1:]
            elif comando == 'IL':
                qtd = int(parametro)
                for _ in range(qtd):
                    saida = saida + cadeia
        print(saida)
except EOFError:
    pass