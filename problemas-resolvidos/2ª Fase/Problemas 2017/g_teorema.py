seq_fibonacci = []

def gera_seq_fibonacci_ate_x(x):
	a = 1
	b = 1

	while b <= x:
		seq_fibonacci.append(b)
		a, b = b, a
		b = a + b

def maior_fib_menor_que_x(x):
    if x > seq_fibonacci[-1]:
        return seq_fibonacci[-1]
    
    for i in range(len(seq_fibonacci)):
        if seq_fibonacci[i] == x:
            return seq_fibonacci[i]
        elif seq_fibonacci[i] > x:
            return seq_fibonacci[i-1]
    
def imprime_lista(lista):
    print('(', end='')
    for i, numero in enumerate(lista, start=1):
        if i == 1:
            print(numero, end='')
        else:
            print(f"+{numero}", end='')
    print(')')
    
def main():
    n = int(input())
    if n == 0 or n == 1:
        print(f"({n})")
        return

    gera_seq_fibonacci_ate_x(n)

    seq_zeckendorf = []
    soma = 0
    while soma < n:
        maior = maior_fib_menor_que_x(n - soma)
        seq_zeckendorf.append(maior)
        soma = sum(seq_zeckendorf)

    imprime_lista(seq_zeckendorf)
    
main()
