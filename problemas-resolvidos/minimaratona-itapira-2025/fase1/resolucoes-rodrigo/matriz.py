a, b, c, d = [int(i) for i in input().split()]

maximo = max(a,b,c,d)

a = a*maximo
b = b*maximo
c = c*maximo
d = d*maximo

print(a,b)
print(c,d)