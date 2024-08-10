from math import sin, cos

PI = 3.1415
def radianos(graus):
  radianos = PI*graus / 180
  return radianos

entrada = input().split(' ')
n      = int(entrada[0])
angulo = float(entrada[1])
angulo = radianos(angulo)

for i in range(n):
  coords = input().split(' ')
  x = float(coords[0])
  y = float(coords[1])
  
  novo_x = cos(angulo)*x - sin(angulo)*y
  novo_y = sin(angulo)*x + cos(angulo)*y


  print(f"{novo_x:.2f} {novo_y:.2f}")

