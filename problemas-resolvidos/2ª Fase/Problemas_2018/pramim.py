turno, rodadas = input().split()
v, a = 0, 0

for i in range(int(rodadas)):
    valor = int(input())
    if turno == 'V':
        v += valor
        turno = 'A'
    elif turno == 'A':
        a += valor
        turno = 'V'
    else:
        break

print(f" VOCE: {v} AMIGO: {a}")
