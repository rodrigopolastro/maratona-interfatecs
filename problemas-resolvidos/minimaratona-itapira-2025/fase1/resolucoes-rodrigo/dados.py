import collections

numeros = [int(i) for i in input().split()]

counter = collections.Counter(numeros)
keys = list(counter.keys())
keys.sort()

for key in keys:
    print(f"{int(key)} {int(counter[key])}")