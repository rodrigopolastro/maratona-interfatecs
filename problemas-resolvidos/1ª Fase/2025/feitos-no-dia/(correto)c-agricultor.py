n = int(input())
for _ in range(n):
    t, u, p = map(float, input().split())

    if p == 1:
        print("NAO REGAR")
    elif t > 30 and u < 50:
        print("REGAR")
    else:
        print("NAO REGAR")