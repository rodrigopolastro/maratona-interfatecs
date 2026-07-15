

PAPEL = 'O'
PEDRA = '*'
TESOURA = 'V'

pontos_beatriz = 0
pontos_artur = 0


while True:
    
    entrada_dados = input()
    
    if(entrada_dados == '- -'):
        break
    
    lista = entrada_dados.split()
    jogada_beatriz = lista[0]
    jogada_artur = lista[1]

    if jogada_beatriz == PAPEL:
        if jogada_artur == PEDRA:
            pontos_beatriz = pontos_beatriz + 1
        elif jogada_artur == TESOURA:
            pontos_artur += 1
    elif jogada_beatriz ==  PEDRA :
        if jogada_artur == TESOURA:
            pontos_beatriz = pontos_beatriz + 1
        elif jogada_artur == PAPEL:
            pontos_artur += 1   
    elif jogada_beatriz ==  TESOURA :
        if jogada_artur == PAPEL:
            pontos_beatriz = pontos_beatriz + 1
        elif jogada_artur == PEDRA:
            pontos_artur += 1           
    
    
if pontos_beatriz > pontos_artur:
    print("BEATRIZ WIN")
elif pontos_artur > pontos_beatriz:
    print("ARTUR WIN")
else:
    print("TIE")
    