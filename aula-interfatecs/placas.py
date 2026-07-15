def eh_placa_normal(placa):
    for caracter in placa:
        if caracter not in 'OI10':
            return True
    return False

numero_placas = int(input())

for n in range(numero_placas):
    placa = input()

    if eh_placa_normal(placa):
        print("Normal")
    else:
        print("NERD!")
