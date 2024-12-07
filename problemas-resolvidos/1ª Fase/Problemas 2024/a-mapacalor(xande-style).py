LINHAS_POR_USUARIO  = 6
COLUNAS_POR_USUARIO = 3
regioes = {
  'superior': 0,
  'esquerda': 0,
  'centro': 0,
  'direita': 0,
  'inferior': 0
}
def encontra_regiao(linha, coluna):
  if linha == 0:
    return 'superior'
  if linha == 5:
    return 'inferior'
  if coluna == 0:
    return 'esquerda'
  if coluna == 1:
    return 'centro'
  if coluna == 2:
    return 'direita'
def main():
  n = int(input())
  regiao_mais_olhada = None
  qtd_olhadas =  0
  for usuario in range(n):
    for i in range(LINHAS_POR_USUARIO):
      leitura = input().split(' ')
      for j in range(COLUNAS_POR_USUARIO):
        if leitura[j] == '1':
          regiao_atual = encontra_regiao(i, j)
          regioes[regiao_atual] += 1
          if regioes[regiao_atual] > qtd_olhadas:
            qtd_olhadas = regioes[regiao_atual]
            regiao_mais_olhada = regiao_atual
  print(regiao_mais_olhada)
main()

