# 1-> algoritmos 2-> boas praticas 3-> desempenho 4->fluxograma 5-> interpretacao de enunciados 6-> sintaxe de linguagem
# nomes exibidos em ordem alfabetica porém o input será em inscricoes
LIMITE_VAGAS = int(input())
Mapping = {
    1 : [], #algoritmos
    2 : [], #'boasPraticas'
    3:[],#'desempenho'
    4:[],#'fluxograma'
    5:[],#'interpretacao'
    6:[],#'sintaxe'
    0:[],#'ficaParaProxima'
}
MappingCategorias = {
    1 : 'ALGORITMOS',
    2 : 'BOAS PRATICAS',
    3 : 'DESEMPENHO',
    4 : 'FLUXOGRAMAS',
    5 : 'INTERPRETACAO DE ENUNCIADOS',
    6 : 'SINTAXE DA LINGUAGEM',
    0 : 'FIXA PARA A PROXIMA!',
}

for i in range(5):
    entrada = input().split(' ',1)
    categorias = entrada[1].split(" ")
    for numeroCategoria in categorias:
        if len(Mapping[int(numeroCategoria)])<LIMITE_VAGAS:
            Mapping[int(numeroCategoria)].append(entrada[0])
        else:
            if entrada[0] in Mapping[int(numeroCategoria)]:
                pass
            else:
                Mapping[0].append(entrada[0])
Mapping[1]=sorted(Mapping[1])
Mapping[2]=sorted(Mapping[2])
Mapping[3]=sorted(Mapping[3])
Mapping[4]=sorted(Mapping[4])
Mapping[5]=sorted(Mapping[5])
Mapping[6]=sorted(Mapping[6])
for categoria in Mapping.keys():
    if categoria == 0 and len(Mapping[categoria]) == 0:
        continue
    else:
        print('-'*30)
        print(MappingCategorias[categoria])
        print('-'*30)
        listaAlunos = Mapping[categoria]
        for nome in listaAlunos:
            print(nome)
    if len(Mapping[0]) == 0 and categoria == 0:
        break
    elif len(Mapping[0]) == 0 and categoria == 6:
        break
    else:
        print()
        
    