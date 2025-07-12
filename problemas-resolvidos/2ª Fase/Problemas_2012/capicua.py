#inicio 8:58   fim 9:01
from math import sqrt
def main():
    while True:
        numeroAnalisar = int(input())
        if numeroAnalisar == 0:
            break
        if sqrt(numeroAnalisar) == int(sqrt(numeroAnalisar)) and str(numeroAnalisar) == str(numeroAnalisar)[::-1]:
            print("S")
        else:
            print("N")
        
    
    
    
    
    
    
main()