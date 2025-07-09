#alexandre 08/09 19:16 - 20:02
def completar(numero_bin:str,particao:int):

    numero_bin = list(numero_bin)
    numero_bin.insert(0,'0')
    while len(numero_bin)%particao != 0:
        numero_bin.insert(0,'0')
    
    
    return ''.join(numero_bin) 
def xor(first:str,second:str):
    retornar = ''
    for i in range(len(first)):
        if first[i] == second[i]:
            retornar+='0'
        else:
            retornar+='1'
    return retornar
def main():
    entrada = input().split(' ')
    numero = int(entrada[0])
    particao = int(entrada[1])
    binario = bin(numero).removeprefix('0b')
    if len(binario)%particao != 0:
        binario = completar(binario,particao)
    lista = []
    
    local = ''
    contador = 0
    for i in range(0,len(binario)):
        local+=binario[i]
        contador +=1
        if contador/particao == 1:
            lista.append(local)
            local = ''
            contador = 0
    
    first = lista[0]
    lista.pop(0)
    for i in lista:
        first = xor(first,i)
    print(int(first,2))
        
  
main()