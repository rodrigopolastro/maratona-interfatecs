# 1:44 - 1:57
# xande
casosTeste = int(input())
CT = []
for _ in range(casosTeste):
    entrada = input().split()
    entrada.pop(0)
    entrada = " ".join(entrada)
    CT.append(entrada)

def principal(lista):
    valorConvertido = [int(x) for x in lista.split()]
    MediaA = sum([x ** 2 for x in valorConvertido]) / sum(valorConvertido)
    mediaB = sum([x**2 for x in valorConvertido if x <= MediaA]) / sum([x for x in valorConvertido if x <= MediaA])
    MA = [str(x) for x in valorConvertido if x > MediaA ]
    MB = [str(x) for x in valorConvertido if x <= MediaA and x>mediaB]
    MC = [str(x) for x in valorConvertido if x<= mediaB]
    return(MA,MB,MC)
for num in range(len(CT)):
    resp = principal(CT[num])
    print(f"Caso {num+1}")
    print(f"A: {" ".join(resp[0])}")
    print(f"B: {" ".join(resp[1])}")
    print(f"C: {" ".join(resp[2])}")
    if num != len(CT) - 1:
        print()
