my_answers = []
correct_answers = []

in_files_lines  = []
out_files_lines = []

NUMBER_OF_FILES = 15

import math
def main(test_input):
  # v = int(input())
  v = int(test_input)

  if v <= 107:
    margem = v + 7
  else:
    margem = v * 1.07

  # print(math.ceil(margem))
  # print(round(margem))
  
  # answer = math.ceil(margem) 
  answer = round(margem)
  return answer

for i in range(1, NUMBER_OF_FILES+1):
  if i < 10: i = "0" + str(i)

  with open(f"input/{i}", 'r') as in_file:
    lines = in_file.readlines()
    lines = [line.strip() for line in lines]
    in_files_lines.append(lines)

  with open(f"output/{i}", 'r') as out_file:
    lines = out_file.readlines()
    lines = [line.strip() for line in lines]
    out_files_lines.append(lines)

for file_lines in in_files_lines:
  for line in file_lines:
    my_answers.append(main(line))

for file_lines in out_files_lines:
  for line in file_lines:
    correct_answers.append(line)   

for i in range(1, NUMBER_OF_FILES):
  a = str(my_answers[i])
  b = str(correct_answers[i])
  if a == b:
    print(f"Test {i} passed!")
  else:
    print(f"Test {i} failed! ({a} VS {b})")
