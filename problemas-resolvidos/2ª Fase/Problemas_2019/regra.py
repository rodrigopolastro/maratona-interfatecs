from collections import defaultdict

T = int(input())
S = float(input())
C = float(input())

palavras = [input().strip().upper() for _ in range(T)]
palavras_sets = [set(p) for p in palavras]

freq_letra = defaultdict(int)
for pset in palavras_sets:
    for letra in pset:
        freq_letra[letra] += 1

freq_par = defaultdict(int)

for pset in palavras_sets:
    for a in pset:
        for b in pset:
            if a != b:
                dupla = (a, b)
                freq_par[dupla] += 1

resultado = []
total_palavras = T

for (a,b), sup_count in freq_par.items():
    suporte = sup_count / total_palavras
    if suporte < S:
        continue
    confiança = sup_count / freq_letra[a]
    if confiança < C:
        continue
    resultado.append((a, b, confiança, suporte))

resultado.sort(key=lambda x: (x[0], x[1]))

if not resultado:
    print("nada foi encontrado\n")
else:
    for a, b, conf, sup in resultado:
        print(f"({a}, {b}) [{conf:.3f}, {sup:.3f}]")
    print()

