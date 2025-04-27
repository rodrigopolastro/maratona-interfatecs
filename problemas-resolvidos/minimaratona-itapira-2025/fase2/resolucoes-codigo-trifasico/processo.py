nct = int(input())
def definir(sequencia):
    G,E,A,D,T = [int(x) for x in sequencia.split()]

    if G == 1 and (A == 1 or D ==1):
        if T >= 3:
            return " deferido (comprovar 3 anos)"
        else:
            return " INDEFERIDO (exp)"
    if G == 1 and E == 1:
        if T>= 5:
            return " deferido (comprovar 5 anos)"
        else:
            return " INDEFERIDO (exp)"
    return " INDEFERIDO (acad)"
        

for _ in range (1,nct +1):
    print(f"Cand. {_}:{definir(input())}")
