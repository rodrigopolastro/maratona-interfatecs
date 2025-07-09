from math import sqrt


def main():
    while True:
        entrada = int(input())
        if entrada == 0:
            break
        else:
            if sqrt(entrada) != int(sqrt(entrada)):
                print("PERA AI... TA LIDANDO ERRADO!")
            else:
                elevado = sqrt(entrada)
                print(int(2 * elevado - 1))
                    
        
        
        
main()