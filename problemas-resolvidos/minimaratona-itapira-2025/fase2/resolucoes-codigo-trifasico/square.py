resp = 0
proibidos = [x for x in range(5,102,4)]
for r in range(1,int(input())+1,2):
    if r == 1:
        resp += 0
    else:
        if(r in proibidos):
            pass
        else:
            resp+= (r*2) + ((r-2) * 2) - 2 
print(resp)