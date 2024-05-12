first_hour = 99
first_minute = 99
last_hour = -99
first_minute = -99

n = int(input())
for i in range(0, n):
  line = input().split(" ")

  he = int(line[0])
  me = int(line[1])
  hs = int(line[2])
  ms = int(line[3])

  if he < first_hour:
    first_hour = he
    first_minute = me
  elif he == first_hour:
    if me < first_minute:
      first_hour = he
      first_minute = me

  if hs > last_hour:
    last_hour = hs
    last_minute = ms
  elif hs == last_hour:
    if ms > last_minute:
      last_hour = hs
      last_minute = ms

hours = last_hour - first_hour
minutes = last_minute - first_minute
answer = hours*60 + minutes

print(answer)
