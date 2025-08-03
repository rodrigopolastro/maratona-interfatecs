#inicio 13:05 rodrigo - 13:17

situacoes = {
    'A': 1,
    'O': 2,
    'R': 3,
    'N': 4
}
candidatos = list()

qtdCandidatos = int(input())
for _ in range(qtdCandidatos):
    posicaoFolha, situacao, nome = input().split(';')
    numeroSituacao = situacoes[situacao]
    candidatos.append((numeroSituacao, nome, posicaoFolha))
candidatosOrdemAtual = sorted(candidatos, key=lambda c: c[2])
candidatosNovaOrdem = sorted(candidatos, key=lambda c: (c[0], c[1]))

qtdMudancas = 0
for i in range(qtdCandidatos):
    if candidatosOrdemAtual[i][1] != candidatosNovaOrdem[i][1]:
        qtdMudancas = qtdMudancas+1
print(qtdMudancas)
