#inicio 7:47


def isPrime(number):
    if number == 2: return True
    if number == 3: return True
    if number % 2 == 0 : return False
    divisores = 1
    for n in range(3,number+2): # como casos só vai até 1.000.000, nao estou me preocupando mt com performance
        if n == number:
            divisores +=1
            break
        if n > number:
            break
        if number%n == 0:
            divisores +=1
    if divisores == 2:
        return True
    else:
        return False
    

def main():
    while True:
        entradaUsuario = int(input())
        if entradaUsuario == 0:
            break
        
        listaPrimos = []
        for n in range(2,entradaUsuario+1):
            if isPrime(n):
                listaPrimos.append(n)
        
        print(pegarNumeros(listaPrimos,entradaUsuario))
    
    pass
    
    
    


def pegarNumeros(listaPrimos,objetivo):
    if objetivo % 2 == 1: return "erro"
    for i in listaPrimos:
        for j in listaPrimos:
            if i + j == objetivo:
                return f"{i} {j}"
    return "erro"

main()
    