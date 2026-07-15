entrada = input()

qtde = len(entrada)
imprimiu = False
for i in range(qtde):
    if qtde % 2 == 1 and i == qtde / 2:
        print("SIM")
        imprimiu = True
        break

    if entrada[i] != entrada[-1-i]:
        print("NAO")
        imprimiu = True
        break

if not imprimiu:
    print("SIM")