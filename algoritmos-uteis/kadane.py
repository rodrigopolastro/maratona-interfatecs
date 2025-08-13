def kadane(arr):
    max_soma = atual = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > atual + arr[i]:
            atual = arr[i]
            temp_start = i
        else:
            atual += arr[i]

        if atual > max_soma:
            max_soma = atual
            start = temp_start
            end = i

    return max_soma, arr[start:end + 1]


# Exemplo
arr = [1, 2, 3, 5, 0, 0 ,0 ,0 ,0, 88, - 900]
soma, elementos = kadane(arr)

print("Maior soma possível:", soma)
print("Elementos do subarray:", elementos)