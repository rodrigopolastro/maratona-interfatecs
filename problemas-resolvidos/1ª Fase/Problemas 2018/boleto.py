# 7:11 - 7:43
# Alexandre
adimplente = 0
inadimplente = 0

def estaVencido(vencimento, pagamento):
   if int(vencimento[4:6]) < int(pagamento[4:6]):
      return True
   if int(vencimento[2:4]) < int(pagamento[2:4]):
      return True
   elif int(vencimento[2:4]) > int(pagamento[2:4]):
      return False
   if int(vencimento[0:2]) < int(pagamento[0:2]):
      return True
   return False

try:
    while True:
        sequenciaBoleto = input()
        dataVencimento = sequenciaBoleto[4:10]
        valorInteiro = int(sequenciaBoleto[10:16])
        valorDecimal = int(sequenciaBoleto[16:18])
        valorTotal = float(f"{valorInteiro}.{valorDecimal}")
        # print(valorTotal)
        dataPagamento = sequenciaBoleto[22:28]
        # print(dataVencimento)
        # print(dataPagamento)
        if estaVencido(dataVencimento,dataPagamento):
            # print("VENCIDO")
            inadimplente += valorTotal  
        else:
            # print("NAO VENCIDO")
            adimplente += valorTotal


except EOFError:
    print(f"{adimplente:.2f}-ADIMPLENTE")
    print(f"{inadimplente:.2f}-INADIMPLENTE")