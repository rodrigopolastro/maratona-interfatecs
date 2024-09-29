from math import sqrt

entrada = input().split(' ')

a, b, c = float(entrada[0]), float(entrada[1]), float(entrada[2])

p = (a + b + c)/2

area = sqrt(p * (p-a) * (p-b) * (p-c))

print(f"{area:.2f}")


