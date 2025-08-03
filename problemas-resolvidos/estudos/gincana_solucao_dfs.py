from collections import defaultdict

amizades = defaultdict(list)
alunosAvaliados = set()

def dfs(aluno):
    if aluno in alunosAvaliados:
        return
    alunosAvaliados.add(aluno)
    amigosAluno = amizades[aluno]
    for amigo in amigosAluno:
        dfs(amigo)

def main():
    qtdAlunos, qtdAmizades = [int(_) for _ in input().split()]

    for _ in range(qtdAmizades):
        aluno1, aluno2 = [int(_) for _ in input().split()]
        amizades[aluno1].append(aluno2)
        amizades[aluno2].append(aluno1)
        
    qtdTimes = 0
    for aluno in range(1, qtdAlunos+1):
        if aluno not in alunosAvaliados:
            dfs(aluno)
            qtdTimes = qtdTimes + 1
            
    print(qtdTimes)

if __name__ == "__main__":
    main()
