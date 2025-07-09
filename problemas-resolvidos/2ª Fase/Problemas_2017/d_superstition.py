def fib(n):   
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a
        b += a
    return b

n = int(input()) 
if n == 1 or n == 2:
    result = n+1
else:
    result = fib(2791) % (10**9 + 7)

print(result)