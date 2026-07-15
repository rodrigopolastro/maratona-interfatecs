di, cons, it = input().split()
di = float(di)
cons = float(cons)
it = int(it)
dt = di
for i in range(it-1):
    dt = dt + 2*(di*cons)
    di = di*cons
print(f"Total distance: {dt:.2f}")
