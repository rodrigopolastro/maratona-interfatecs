
numero_palavras = int(input())


for n in range(numero_palavras):
    palavra = input()

    resposta_numerica = ""

    for caractere in palavra:
        if caractere in 'ABC':
            resposta_numerica += "2"
        if caractere in 'DEF':
            resposta_numerica += "3"
        if caractere in 'GHI':
            resposta_numerica += "4"
        if caractere in 'JKL':
            resposta_numerica += "5"
        if caractere in 'MNO':
            resposta_numerica += "6"
        if caractere in 'PQRS':
            resposta_numerica += "7"
        if caractere in 'TUV':
            resposta_numerica += "8"
        if caractere in 'WXYZ':
            resposta_numerica += "9"
        if caractere in '.':
            resposta_numerica += '0'

    print(resposta_numerica)
