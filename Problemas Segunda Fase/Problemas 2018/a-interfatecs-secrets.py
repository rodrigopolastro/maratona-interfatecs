# # 1) Generate number for code
# # 2) Check if number is factorial (ultimate)
# # 3) Check if number is in the fibonacci sequence (premium)
# # 4) Check if number is prime (basic)
# # 5) Otherwise, print '!'

from math import factorial, sqrt

# the 'a' char has the ascii code 97
ASCII_CODE_OFFSET = 96

def calc_code_value(code):
    code_value = 0
    for i in range(len(code)):
        char_ascii_code = ord(code[i])
        if char_ascii_code > ASCII_CODE_OFFSET:
            numeric_value = int(char_ascii_code) - ASCII_CODE_OFFSET
        else: #it is a digit
            numeric_value = int(code[i])

        code_value += numeric_value * (i+1)
    return code_value

def is_factorial(number):
    n = 0
    factorial_n = 0
    while True:
        factorial_n = factorial(n)
        if factorial_n == number:
            return True
        if factorial_n > number:
            return False
    
        n += 1

def is_in_fibonacci_sequence(number):
    a = 1
    b = 1
    aux = 0
    while True:
        if b == number:
            return True
        if b > number:
            return False
        
        aux = a
        a = b
        b += aux 

def is_prime(number):
    if number == 1:
        return False
    
    if number % 2 == 0:
        return False
    
    for i in range(3, int(sqrt(number)), 2):
        if number % i == 0:
            return False    

    return True 

while True:
    # n = int(input())
    # if is_in_fibonacci_sequence(n):
    #     print('sim')
    # else:
    #     print('nao')

    code = input().strip()
    if not code:
        break

    code_value = calc_code_value(code)
    print(f"{code_value}: ", end='')

    if is_factorial(code_value):
        print('ultimate')
        continue
    if is_in_fibonacci_sequence(code_value):
        print('premium')
        continue
    if is_prime(code_value):
        print('basic')
        continue
    print('!')
