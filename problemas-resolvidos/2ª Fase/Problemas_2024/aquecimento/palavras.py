entrada = input().lower().split(' ')
from collections import Counter

a = Counter(entrada[0])
b = Counter(entrada[1])

if a == b:
    print('S')
else:
    print('N')