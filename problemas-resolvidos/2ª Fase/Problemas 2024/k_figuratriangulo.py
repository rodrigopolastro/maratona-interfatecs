piramide = 9
entrada = int(input())
dici = {
    1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I'
}
if entrada%9 == 0:
    print(f"{entrada//piramide}I")
else:
    print(f"{entrada//piramide+1}{dici[entrada%9]}")