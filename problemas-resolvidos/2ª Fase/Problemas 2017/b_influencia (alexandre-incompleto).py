entrada = input().split(' ')
linhas = int(entrada[0]) # quantas linhas de cadeira tem a sala 
colunas = int(entrada[1]) #quantas colunas de cadeira tem a sala

sala_binario = [] # variavel responsavel por atribuir estado de 'aliciamento' do aluno
for i in range(linhas):# monta matriz binárias com o inteiro 0
    linha = list(map(int,list('0'*colunas)))
    sala_binario.append(linha)
sala_influencia = [] # variavel responsavel pelo armazenamento da matriz que contem os números de suas respectivas influencias
posicao_luiz = list(map(int,input().split(' ')))
posicao_luiz[0]-=1 # correcao de indexes para o posicionamento de luiz
posicao_luiz[1]-=1 # correcao de indexes para o posicionamento de luiz
for linhas_cadeiras in range(linhas):# monta a matriz de influencia convertido de string para inteiro
    sala_influencia.append(list(map(int,input().split(' ')))) 
sala_binario[posicao_luiz[0]][posicao_luiz[1]] = 1 # muda a posicao do luiz para 1 na matriz binária
# def is_aside(posicao_objetivo:tuple,posicao_comparada:tuple):
#  if posicao_objetivo[0] == posicao_comparada[0]+1 or posicao_comparada[0] and posicao_objetivo[0] == posicao_comparada[0] or posicao_comparada[0]+1:
#   return True
#  else:
#   return False
# """
# 1 2 3   00  01 02
# 4 5 6   10  11 12
# 7 8 9   20  21 22

# """
print(posicao_luiz)
for cadeira_linha in range(linhas):
    for cadeira_coluna in range(colunas):
     ,   # print(is_aside(posicao_luiz,(cadeira_linha,cadeira_coluna)))
        

