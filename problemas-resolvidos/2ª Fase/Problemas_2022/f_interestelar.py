dados = list()

n = int(input())

minimo, maximo = map(int, input().split())

for _ in range(n):
    valor = int(input())

    is_valor_valido = valor >= minimo and valor <= maximo

    dados.append(is_valor_valido)

while True:
    try:
        entrada = input()

        if entrada == '' or entrada is None:
            break

        inicio_intervalo, fim_intervalo = map(int, entrada.split())

        intervalo = dados[inicio_intervalo:fim_intervalo+1]

        print(intervalo.count(True))
    except EOFError:
        break
