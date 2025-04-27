n = int(input())
resp = []
for _ in range(n):
    resp.append(int(input()))
np = resp.count(1)
npi = len(resp) - np
if npi % 2 == 0:
    print('par')
else:
    print('impar')