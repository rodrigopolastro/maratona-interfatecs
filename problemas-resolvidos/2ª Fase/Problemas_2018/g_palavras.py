#6 minutos - rodrigo
palavra1, palavra2 = input().split()
if sorted(palavra1.lower()) == sorted(palavra2.lower()):
    print('S')
else:
    print('N')