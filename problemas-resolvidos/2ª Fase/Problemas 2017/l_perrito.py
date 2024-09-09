# alexandre 08/09   20:04  - 20:10
def main():
    entrada = input().split(' ')
    raio = float(entrada[0])
    metros = int(entrada[1])
    perimetro = 2*3.1415*raio
    print(int(metros//perimetro))
main()