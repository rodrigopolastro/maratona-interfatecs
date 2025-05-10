from math import sqrt, cos

PI = 3.14159265358979323846
def grausParaRad(angulo):
    return angulo * PI / 180

def lei_cossenos(a, b, angulo):
    return sqrt( a**2 + b**2 - 2*a*b*cos(angulo)) 

def areaTriangulo(a,b,c):
    p = (a+b+c)/2
    return sqrt(p * (p-a) * (p-b) * (p-c))

while True:
    a, b, anguloGraus = [float(_) for _ in input().split()]
    if a == b == anguloGraus:
        exit()
    anguloRad = grausParaRad(anguloGraus)
    c = lei_cossenos(a,b,anguloRad)
    print(f"{areaTriangulo(a,b,c):.4f}")

# print(lei_cossenos(3,4,grausParaRad(90))) 