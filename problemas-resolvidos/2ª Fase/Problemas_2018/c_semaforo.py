a, b, c, d, y = [int(x) for x in input().split()]
h, m, s = [int(x) for x in input().split()]

segTotal = (h*60*60) + (m*60) + s
ciclo = (a+y)+(b+y)+(c+y)+(d+y)

sobra = segTotal % ciclo

if sobra == 0:
    print("D AMARELO")
else:
    if sobra <= a:
        print("A VERDE")
    elif sobra <= a + y:
        print("A AMARELO")
    elif sobra <= a + y + b:
        print("B VERDE")
    elif sobra <= a + y + b + y:
        print("B AMARELO")
    elif sobra <= a + y + b + y + c:
        print("C VERDE")
    elif sobra <= a + y + b + y + c + y:
        print("C AMARELO")
    elif sobra <= a + y + b + y + c + y + d:
        print("D VERDE")
    elif sobra <= a + y + b + y + c + y + d + y:
        print("D AMARELO")
