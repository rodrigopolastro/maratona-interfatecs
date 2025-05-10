from collections import defaultdict

def tamanhoMenorCaminho(aluno1, aluno2):
    # print(alunosAnteriores)
    passos = 0
    posicao = aluno2
    while posicao != aluno1:
        passos+=1
        posicao = alunosAnteriores[posicao]
    return passos

conexoes = defaultdict(set)
qtdConexoes = int(input())
for _ in range(qtdConexoes):
    aluno1, aluno2 = input().split()
    conexoes[aluno1].add(aluno2)
    conexoes[aluno2].add(aluno1)

hifen = input()
while True:
    aluno1, aluno2 = input().split()
    if aluno1 == aluno2 == '*':
        break
    
    proximosAlunos = list()
    alunosAnteriores = dict()
    proximosAlunos.append(aluno1)
    alunosAnteriores[aluno1] = None
    distancia = 0

    while len(proximosAlunos) > 0:
        alunoAtual = proximosAlunos.pop(0)
        if alunoAtual == aluno2:
            distancia = tamanhoMenorCaminho(aluno1, aluno2)
            # print(aluno1, aluno2)
            # a = input()
            break

        amigos = conexoes[alunoAtual]
        for proximoAluno in amigos:
            if proximoAluno in alunosAnteriores:
                continue

            alunosAnteriores[proximoAluno] = alunoAtual
            proximosAlunos.append(proximoAluno)

    if distancia > 0:
        print(f"{aluno1}-{aluno2} = {distancia}")
    else:
        print(f"{aluno1}-{aluno2} = sem conexao")


    
