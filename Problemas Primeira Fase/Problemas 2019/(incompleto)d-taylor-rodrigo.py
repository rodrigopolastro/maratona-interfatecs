from math import factorial
# from math import ceil

x = int(input())

sum = 0
for n in range(0, 5): # ou é 6??
  r = x * 3.1415 / 180

  a = (-1) ** n 
  b = r ** (2*n)
  c = factorial(2*n)

  sum += a*b / c



# avoid exceptions when number has less than 4 decimal numbers
try: 
  decimal_part = sum - int(sum) 
  fourth_decimal = str(decimal_part)[3 + 2] # +2 => skip '0.'
  if int(fourth_decimal) > 6:
    sum += 0.001

    integer_digits = len(str(int(sum)))

    # full_number = integer + '.' + 3 decimal_places
    decimal_places = integer_digits + 1 + 3 
    sum = str(sum)[:decimal_places]
    print(sum)
    # exit()
  else:
    print(f"{sum:.3f}") #QUE MERLINNNNNNNNNNNNN
    
except:
  print(f"{sum:.3f}")