entradas = list(map(float, input().split()))

def calcula_retorno_investimento(aporte_mensal):
    final_mes_1 = aporte_mensal * 1.01
    final_mes_2 = (final_mes_1 + aporte_mensal) * 1.01
    final_mes_3 = (final_mes_2 + aporte_mensal) * 1.01
    return final_mes_3

def main():
    SALARIO_HORA_BRASIL = entradas[0]
    SALARIO_HORA_FORA = entradas[1]
    HORAS_NO_MES = entradas[2]
    PORCENTAGEM_GASTOS_BRASIL = entradas[3]
    PORCENTAGEM_GASTOS_FORA = entradas[4]
    TAXA_CAMBIO = entradas[5]

    # BRASIL
    salario_mensal_brasil = SALARIO_HORA_BRASIL * HORAS_NO_MES
    aporte_mensal_brasil = salario_mensal_brasil * (1 - PORCENTAGEM_GASTOS_BRASIL/100)
    saldo_investimento_brasil = calcula_retorno_investimento(aporte_mensal_brasil)

    # FORA
    salario_mensal_fora = SALARIO_HORA_FORA * HORAS_NO_MES
    aporte_mensal_fora = salario_mensal_fora * (1 - PORCENTAGEM_GASTOS_FORA/100)
    retorno_investimento_fora = calcula_retorno_investimento(aporte_mensal_fora)
    saldo_investimento_fora = retorno_investimento_fora * TAXA_CAMBIO

    print(f"{saldo_investimento_brasil:.2f}BR {saldo_investimento_fora:.2f}ES")

main()





