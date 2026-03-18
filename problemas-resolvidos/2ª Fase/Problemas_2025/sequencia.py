entrada = int(input())
arr = [1]
ne = []

for r in range(entrada - 1):
    anterior = arr[0]
    c = 1
    for i in range(1, len(arr)):
        n = arr[i]
        if n != anterior:
            ne.extend([c, anterior])
            c = 1
            anterior = n
        else:
            c += 1
    if c >= 1:
        ne.extend([c, anterior])

    arr = ne
    ne = []

print(''.join([str(i) for i in arr]))

