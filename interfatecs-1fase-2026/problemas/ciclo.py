tempo_total = 0

qtd_dias, duracao_ciclo = map(int, input().split())
for _ in range(qtd_dias):
    ciclos_no_dia, minutos_refatoracao = map(int, input().split())
    total_dia = (ciclos_no_dia * duracao_ciclo) + minutos_refatoracao
    tempo_total += total_dia
print(f"Relatorio MCE: {tempo_total} minutos de esforco total")
