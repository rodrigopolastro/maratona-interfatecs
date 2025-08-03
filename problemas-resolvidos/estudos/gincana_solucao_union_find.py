# # Exercício "Gincana" da OBI de 2011
# # Link no neps.academy: https://neps.academy/br/exercise/309

#IMPLEMENTAÇÃO COM UNION FIND
def find(aluno):
    if superioresDeAlunos[aluno] == aluno:
        return aluno
    
    liderEquipe = find(superioresDeAlunos[aluno])
    superioresDeAlunos[aluno] = liderEquipe
    return liderEquipe


qtdAlunos, qtdAmizades = [int(_) for _ in input().split()]

superioresDeAlunos = [i for i in range(qtdAlunos)]
qtdTimes = qtdAlunos
for _ in range(qtdAmizades):
    aluno1, aluno2 = [int(_)-1 for _ in input().split()]
    liderEquipeAluno1 = find(aluno1)
    liderEquipeAluno2 = find(aluno2)
    if liderEquipeAluno1 != liderEquipeAluno2:
        superioresDeAlunos[liderEquipeAluno2] = find(liderEquipeAluno1)
        qtdTimes = qtdTimes -1     

print(qtdTimes)