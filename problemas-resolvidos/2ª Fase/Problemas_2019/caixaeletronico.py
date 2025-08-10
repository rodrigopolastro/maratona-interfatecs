bandejaA = [int(x) for x in input().split()]  # .append("A")
bandejaA.append("A")
bandejaB = [int(x) for x in input().split()]  # .append("B")
bandejaB.append("B")
bandejaC = [int(x) for x in input().split()]  # .append("C")
bandejaC.append("C")

LB = [bandejaA, bandejaB, bandejaC]
listaBandejas = sorted(LB, key=lambda x: -x[0])

qtdeSaques = int(input())

for s in range(qtdeSaques):
    valorSaque = int(input())
    range1 = valorSaque // listaBandejas[0][0]
    range2 = valorSaque // listaBandejas[1][0]
    range3 = valorSaque // listaBandejas[2][0]
    continuar = True
    for a in range(range1, -1, -1):
        if continuar:
            for b in range(range2, -1, -1):
                if continuar:
                    for c in range(range3, -1, -1):
                        if continuar:
                            if listaBandejas[0][0] * a + listaBandejas[1][0] * b + listaBandejas[2][0] * c == valorSaque and a <= listaBandejas[0][1] and b <= listaBandejas[1][1] and c <= listaBandejas[2][1]:

                                continuar = False
                                listaBandejas[0][1] -= a
                                listaBandejas[1][1] -= b
                                listaBandejas[2][1] -= c


orderarImprimir = sorted(listaBandejas, key=lambda x: x[2])

for bandeja in orderarImprimir:
    print(f"na bandeja {bandeja[2]} restaram {bandeja[1]} notas")
