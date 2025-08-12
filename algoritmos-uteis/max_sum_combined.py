def max_sum_combined_with_elements(arr):
    n = len(arr)

    # === 1. Kadane (subarray contínuo) ===
    max_kadane = arr[0]
    atual = arr[0]
    start = end = temp_start = 0

    for i in range(1, n):
        if arr[i] > atual + arr[i]:
            atual = arr[i]
            temp_start = i
        else:
            atual += arr[i]

        if atual > max_kadane:
            max_kadane = atual
            start = temp_start
            end = i

    kadane_result = arr[start:end + 1]

    # === 2. Saltos (de x em x) ===
    max_step = float('-inf')
    best_sequence = []

    for x in range(1, n):
        for offset in range(x):
            soma = 0
            temp_seq = []
            i = offset
            while i < n:
                soma += arr[i]
                temp_seq.append(arr[i])

                if soma > max_step:
                    max_step = soma
                    best_sequence = temp_seq.copy()

                if soma < 0:
                    soma = 0
                    temp_seq = []

                i += x

    # === Comparar os dois ===
    if max_kadane >= max_step:
        return max_kadane, kadane_result
    else:
        return max_step, best_sequence
    
    
    
    
    
    
    
    
    
arr = [2, 4, -5, 6, 2, 4, 6, -7, 10, -5, 20, -4, 6]
soma, elementos = max_sum_combined_with_elements(arr)

print("Maior soma possível:", soma)
print("Elementos usados:", elementos)