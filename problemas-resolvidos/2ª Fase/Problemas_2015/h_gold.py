#inicio 7:47


from math import sqrt, ceil
def isPrime(number):
    if number == 2:
        return True
    
    if number == 1 or number % 2 == 0:
        return False
    
    for divisor in range(3, ceil(sqrt(number))+1, 2):
        if number % divisor == 0:
            return False
        
    return True



    

def main():
    while True:
        entradaUsuario = int(input())
        if entradaUsuario == 0:
            break
        
        if entradaUsuario % 2 == 1:
            print("erro")
        else:
            listaPrimos = [2]
            for n in range(3,entradaUsuario+1,2):
                if isPrime(n):
                    listaPrimos.append(n)
            # print(listaPrimos)
            print(pegarNumeros(listaPrimos,entradaUsuario))
    
    pass
    
    
    


def pegarNumeros(listaPrimos,objetivo):
    if objetivo % 2 == 1: return "erro"
    
    e,d = 0,len(listaPrimos)-1
    
    while True:
        soma = listaPrimos[e] + listaPrimos[d]
        soma1 = listaPrimos[e] + listaPrimos[e]
        soma2 = listaPrimos[d] + listaPrimos[d]
        if soma < objetivo:
            e +=1
        elif soma > objetivo:
            d -=1
        elif soma == objetivo:
            return f"{listaPrimos[e]} {listaPrimos[d]}" 
        elif soma1 == objetivo:
            return f"{listaPrimos[e]} {listaPrimos[e]}" 
        elif soma2 == objetivo:
            return f"{listaPrimos[d]} {listaPrimos[d]}" 
        
    
            
    

main()
    