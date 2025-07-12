# inicio 8:00 fim 8:40
def converterParaSegundos(horaE: str, minutoE: str, horaS: str, minutoS):
    horaEntradaInteiro = int(horaE)
    minutoEntradaInteiro = int(minutoE)
    horaSaidaInteiro = int(horaS)
    minutoSaidaInteiro = int(minutoS)
    retornoEntrada = 0
    retornoEntrada += (int(horaEntradaInteiro) * 60 * 60)
    retornoEntrada += (int(minutoEntradaInteiro) * 60)

    retornoSaida = 0
    retornoSaida += (int(horaSaidaInteiro) * 60 * 60)
    retornoSaida += (int(minutoSaidaInteiro) * 60)

    if retornoSaida < retornoEntrada:
        retornoSaida += (24 * 60 * 60)
    return (retornoEntrada, retornoSaida)


def main():
    while True:

        vagas, professores = [int(x) for x in input().split()]
        if vagas == 0 and professores == 0:
            break
        naoEstacionaramNaFatec = 0
        entradaFormatada = []
        estacionamento = []
        for x in range(professores):
            x = input().split()
            tempos = converterParaSegundos(x[0], x[1], x[2], x[3])
            entradaFormatada.append((x, tempos[0], tempos[1]))
        entradaFormatada = list(sorted(entradaFormatada, key=lambda x: x[1]))
        for dado in entradaFormatada:
            aremover = []
            for temposaida in estacionamento[::-1]:
                if dado[1] > temposaida:
                    aremover.append(temposaida)

            for item in aremover:
                estacionamento.remove(item)
                vagas += 1

            if vagas > 0:
                estacionamento.append(dado[2])
                vagas -= 1
            else:
                naoEstacionaramNaFatec += 1

        print(naoEstacionaramNaFatec)


main()
