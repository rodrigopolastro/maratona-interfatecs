while True:
    k,n = 0,0
    ent = input().split()
    k = int(ent[0])
    n = int(ent[1])
    if( k == n == 0):
         break
    entrada = input().split()
    espera = 0
    for i in entrada:
         chegou = int(i)
         espera += chegou
         espera -= k
         if (espera < 0):
             espera = 0
    print(espera)
