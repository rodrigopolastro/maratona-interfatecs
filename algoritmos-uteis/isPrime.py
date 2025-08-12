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