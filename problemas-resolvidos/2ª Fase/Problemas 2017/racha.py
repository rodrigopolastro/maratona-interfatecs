def procurar_horizontalmente(palavra,cartela):
    for linha in range(len(cartela)):
        for letra in range(len(linha)):
            if cartela[linha][letra] == palavra[0]:
                try:
                    if cartela[linha][letra:letra-len(palavra):-1] == palavra:
                        return True
                    return False
                except:
                    try:
                        if cartela[linha][letra:letra+len(palavra)] == palavra  == palavra:
                            return True
                        return False
                    except:
                        return False
                        


def main():
    cartela = int(input())
    matriz_cartela = []
    for i in range(cartela):
       matriz_cartela.append(list(input()))
    procurar_palavras = []   
    procurar = int(input())
    for i in range(procurar):
        procurar_palavras.append(input())
    print(*matriz_cartela)
main()