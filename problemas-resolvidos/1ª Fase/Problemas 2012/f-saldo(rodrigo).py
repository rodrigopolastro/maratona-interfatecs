################################################################################
# Objetivo: 
# Autor: Rodrigo
# Data: 28/01/2025
# Duração: inicio: 20:00
################################################################################

# A partir de um conjunto de lançamentos ocorridos na
# conta corrente, e considerando o saldo inicial da conta no período, será possível determinar o
# saldo ao final de cada dia. Depois basta determinar a média do período, que é a média
# aritmética simples dos saldos diários.

# há lançamentos de crédito e débito

# o saldo final do dia D é dado pelo saldo da
# conta no final do dia D-1 (ou seja, o dia anterior) mais a soma dos créditos do dia D menos a
# soma dos débitos desse dia D.
contCasosTeste = 0
while True:
    contCasosTeste += 1
    saldoAcumulado = 0.0
    saldoAtual = 0.0
    diaLancamentoAnterior = 1
    
    casoTeste = input().split()
    duracaoPeriodo, qtdLancamentos, saldoInicial = int(casoTeste[0]), int(casoTeste[1]), float(casoTeste[2])
    if duracaoPeriodo == 0:
        break
    
    diaAtual = 1
    saldoAtual = saldoInicial
    for indexLancamento in range(qtdLancamentos):
      
        lancamento = input().split()
        diaLancamento, tipoLancamento, valor = int(lancamento[0]), str(lancamento[1]), float(lancamento[2])
        
        while diaAtual < diaLancamento:
            saldoAcumulado += saldoAtual
            diaAtual += 1
            
        if tipoLancamento == 'C':
            saldoAtual += valor
        else:
            saldoAtual -= valor
            
        if indexLancamento == qtdLancamentos-1:
            saldoAcumulado += (duracaoPeriodo - diaLancamento + 1) * saldoAtual
       
    print(f"Caso {contCasosTeste}: {saldoAcumulado/duracaoPeriodo:.2f}")       
        
