tabelaHash = {
    'A':'2','B':'2','C':'2',
    'D':'3','E':'3','F':'3',
    'G':'4','H':'4','I':'4',
    'J':'5','K':'5','L':'5',
    'M':'6','N':'6','O':'6',
    'P':'7','Q':'7','R':'7','S':'7',
    'T':'8','U':'8','V':'8',
    'X':'9','Y':'9','Z':'9',
    '.':'0',
}
palavras = int(input())
respostas = [] # apenas para o output ficar agrupado e mais facil de conferir
for palavra in range(palavras):
    palavraEscrever = input()
    palavraNumero = ''
    for letra in palavraEscrever:
        palavraNumero+=tabelaHash[letra]
    respostas.append(palavraNumero)
for resposta in respostas:
    print(resposta)
        

    