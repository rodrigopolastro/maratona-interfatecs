n = int(input())
seq = input().split(' ')

sum = 0
for i in range(n):
    # converter para binário
    if seq[i] == '1':
        exp = n - i - 1
        sum += pow(2, exp)

total = pow(2, n) - 1
answer = total - sum

print(answer)