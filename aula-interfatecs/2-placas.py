# 1:22 - 1:24
# xande
n = int(input()) # qtd d casos de teste

def nerdOuNao(string):
    for chr in string:
        if chr not in '10iIoO':
            return False
    return True    
    
for _ in range(n):
    if(nerdOuNao(input())):
        print("NERD!")
    else:
        print("Normal")