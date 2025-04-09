import collections

string = input()

counter = collections.Counter(string)
pares = 0
impares = 0
for valor in counter.values():
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1


if len(string) % 2 == 0:
    if pares == len(counter.values()):
        print('VERDADEIRO')
    else:
        print('FALSO')
else:
    if impares == 1:
        print('VERDADEIRO')
    else:
        print('FALSO')
