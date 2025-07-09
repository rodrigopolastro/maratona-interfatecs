from string import ascii_lowercase, ascii_uppercase


# ALFABETO = "............xxxxxxxxxxxOOOOOOOOO□□□□□□□□□□□□■■■■■■■■" => essa versão é bem mais chave, pprt
ALFABETO = ascii_uppercase + ascii_lowercase
num_camadas, num_linhas = 0, 0

def imprime_matriz(matriz):
    for i in range(num_linhas):
        for j in range(num_linhas):
            if j > 0: print(' ', end='')
            print(matriz[i][j], end='')
        print("\n") 

# def main():
num_camadas = int(input())
num_linhas = num_camadas*2 + 1
letras = ALFABETO[:num_camadas] + '*'

matriz = list()
for i in range(num_linhas):
    linha = [''] * num_linhas
    matriz.append(linha) 
    
for camada in range(num_camadas+1):
    letra = letras[camada]
    
    # Primeira e última linhas da letra
    for coluna in range(camada,num_linhas - camada):
        matriz[camada][coluna] = letra
        matriz[num_linhas-camada - 1][coluna] = letra
    
    # "Paredes" verticais da camada da letra
    for linha in range(camada+1, num_linhas - camada - 1):
        matriz[linha][camada] = letra
        matriz[linha][num_linhas-camada-1] = letra
            
imprime_matriz(matriz)
            
# main()
  
