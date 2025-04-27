x, y = [int(i) for i in input().split()]

def validaEntrada(x,y):
    if x < 1 or x > 100:
        return False

    if y < 1 or y > 100:
        return False

    if x == y:
       return False
    
    return True

if validaEntrada(x,y):

    # x, y = min(x, y), max(x, y)
    if x < y:
        print(f"{x} {y}")
        print(f"{y} {x}")
        print(f"{y} {-x}")
        print(f"{x} {-y}")
        print(f"{-x} {-y}")
        print(f"{-y} {-x}")
        print(f"{-y} {x}")
        print(f"{-x} {y}")
    else: # x=5, y=1
        print(f"{x} {y}")
        print(f"{y} {x}")
        print(f"{y} {-x}")
        print(f"{x} {-y}")
        print(f"{-x} {-y}")
        print(f"{-y} {-x}")
        print(f"{-y} {x}")
        print(f"{-x} {y}")
    
else:
    print('ERRO')