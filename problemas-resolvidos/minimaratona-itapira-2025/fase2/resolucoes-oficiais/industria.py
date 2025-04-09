try:
    while True:
        entrada = input()
        if not entrada:
            break
        qtdInicial, passo = [int(_) for _ in entrada.split()]
        qtdRestante = qtdInicial
        posAtual = 0
        garrafas = [1 for i in range(qtdInicial)]
        while qtdRestante > 1:
            cont = 0
            while cont < passo:
                posAtual = (posAtual + 1) % qtdInicial
                if garrafas[posAtual-1] == 1:
                    cont+=1
            garrafas[posAtual-1] = 0
            qtdRestante-=1
        print(garrafas.index(1)+1)
except EOFError:
    pass
