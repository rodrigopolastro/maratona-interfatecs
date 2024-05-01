mudancas = {}
mudancas["a"] = 3
mudancas["b"] = 5

# mudancas.values
# values = list(mudancas.values)
soma = 0
# print(type(mudancas))
# teste = mudancas.values()
# print(teste)
# print(type(mudancas.values))
# print(type(mudancas.keys))

for i in mudancas.values():
  soma += i
  # print(i)

print(soma)
# print(mudancas)