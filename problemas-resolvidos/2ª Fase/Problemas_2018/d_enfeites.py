enfeites = int(input())
entrada = []
for _ in range(enfeites):
    entrada.append(tuple([int(x) for x in input().split()]))
entrada = sorted(entrada,key=lambda x : (x[0],-x[1]))


for c in entrada:
    print(c[1])