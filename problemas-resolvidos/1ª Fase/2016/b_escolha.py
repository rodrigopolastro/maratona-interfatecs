# rodrigo; inicio: 09:10 - 9:17 - duração: 7 minutos

CONTAGEM = 31
while True:
    qtd_carros = int(input())
    if qtd_carros == -1:
        break

    if qtd_carros == CONTAGEM:
        print(qtd_carros)
    elif qtd_carros > CONTAGEM:
        print(CONTAGEM)
    else:
        print(CONTAGEM % qtd_carros)