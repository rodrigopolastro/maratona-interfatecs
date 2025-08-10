def retornarPrioridade(cor:str):
    cor = cor.lower()
    if cor == 'vermelho':
        return 5
    if cor == 'laranja':
        return 4
    if cor == 'amarelo':
        return 3
    if cor == 'verde':
        return 2
    return 1

listaPacientes = []

try:
    while True:
        dado = input()
        if dado == 'beep':
            if len(listaPacientes) > 0:
                print(listaPacientes.pop(0)[0])
        else:
            dadoSplit = dado.split()
            listaPacientes.append((dadoSplit[0],retornarPrioridade(dadoSplit[1])))
            listaPacientes.sort(key= lambda x : -x[1])
except EOFError:
    pass