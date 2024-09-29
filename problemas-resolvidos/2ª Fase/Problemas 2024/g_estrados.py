qtd_projetos = int(input())
for _ in range(qtd_projetos):
    largura_estrado, qtd_ripas, largura_ripa = list(map(int, input().split(' ')))
    
    espaco_ripas = qtd_ripas * largura_ripa
    espacamento_total = largura_estrado - espaco_ripas
    espacamento_ripas = espacamento_total / (qtd_ripas - 1)
    
    if espacamento_ripas < 10:
        print('projeto superdimensionado')
    elif espacamento_ripas <= 20:
        print('projeto ok')
    else:
        print('projeto subdimensionado')