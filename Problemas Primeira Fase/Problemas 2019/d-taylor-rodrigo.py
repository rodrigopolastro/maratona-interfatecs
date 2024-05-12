from math import factorial

x = int(input())

sum = 0
for n in range(0, 5): # ou é 6??
  r = x * 3.1415 / 180

  a = (-1) ** n 
  b = r ** (2*n)
  c = factorial(2*n)

  sum += a*b / c

decimal_part = sum - int(sum) 
decimal_part = str(decimal_part)[2:] # remove o '0.'

# completa com zeros até 4 casas
while len(decimal_part) < 4:
  decimal_part = decimal_part + '0'

tres_casas_decimais = decimal_part[:3]
fourth_decimal = int(decimal_part[3])
if fourth_decimal > 6:
  tres_casas_decimais = int(tres_casas_decimais) + 1
  tres_casas_decimais = str(tres_casas_decimais)

final_number = str(int(sum)) + '.' + tres_casas_decimais
print(final_number)