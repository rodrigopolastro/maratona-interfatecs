regioes = {
  's': 0,
  'e': 0,
  'c': 0,
  'd': 0,
  'i': 0
}
sequencia_regioes = 'sss'+'ecd'+'ecd'+'ecd'+'ecd'+'iii' 

n = int(input())
cont_posicao = 0

#cada usuário possui 6 linhas de dados
for i in range(n*6):
  linha = input().split(' ')
  #cada linha de dado possui 3 valores
  for posicao in linha:
    if posicao == '1':
      regiao = sequencia_regioes[cont_posicao]
      regioes[regiao] += 1
    cont_posicao += 1
    if cont_posicao == 6*3:
      cont_posicao = 0

regiao_mais_olhada = None
qtd_olhadas = -1
for regiao in regioes:
  if regioes[regiao] > qtd_olhadas:
    qtd_olhadas = regioes[regiao]
    regiao_mais_olhada = regiao
  
nomes_completos = {
  's': 'superior',
  'e': 'esquerda',
  'c': 'centro',
  'd': 'direita',
  'i': 'inferior'
}

resposta = nomes_completos[regiao_mais_olhada]
print(resposta)