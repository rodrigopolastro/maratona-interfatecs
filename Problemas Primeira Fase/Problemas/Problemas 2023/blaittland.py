def main():
  tamanho_lista = input()
  str_final = list(input())
  str_atual = sorted(str_final) 
  
  mudancas = {}
  for letra in str_atual:
    mudancas[letra] = 0

  # # a ideia é ir alterando a string ordenada até ela se tornar
  # # a final e depois contar quantas alterações foram feitas

  for letra in str_final:
    pos_atual  = str_atual.index(letra)
    pos_final  = str_final.index(letra)
    diferenca = pos_final - pos_atual
    if diferenca == 0:
      pass
    
    if diferenca < 0:
      diferenca = -diferenca

      if diferenca > 5:
        print("A Database Systems student read a book.")
        quit()

      mudancas[letra] += diferenca
      str_atual.pop(pos_atual)
      str_atual.insert(pos_atual - diferenca, letra) #volta pra posicao original

  qtd_mudancas = 0
  for i in mudancas.values():
    qtd_mudancas += i
  print(qtd_mudancas)

main()
