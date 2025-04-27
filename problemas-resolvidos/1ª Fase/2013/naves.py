# 4:43 
# xande
while True:
    entrada = input()
    if entrada == '-1':
        break
    entrada = entrada.split()
    x = int(entrada.pop(0))
    y = int(entrada.pop(0))
    z = int(entrada.pop(0))
    objetivo = x + y + z
    qtdN = entrada.pop(0)
    resp = []
    for _ in range(int(qtdN)):
        xn = int(entrada.pop(0))
        yn = int(entrada.pop(0))
        zn = int(entrada.pop(0))
        # √((x2 – x1)² + (y2 – y1)²)
        difX = (x - xn)**2
        difY = (y - yn)**2
        difZ = (z - zn)**2
        resp.append((_, ( difX+ difY + difZ) ** 0.5 ))
    resp = sorted(resp, key= lambda x: (x[1] ,x[0]))
    rf = ''
    for r in resp:
        rf += str(r[0]) + ' '
    print("resposta ",resp)
    print("objetivo",objetivo)
    print(rf.strip())
