# 19:40 - 20:00 (perdi 10 minuitos para achar um espaço a mais na hora de printar)

qtdSenhas = int(input())
senhas = set(input().split())
qtdFuncionarios = int(input())
senhasFuncionarios = input().split()

senhasEntregues = set()
almocaram = invalidas = repetidas = 0

for senhaFuncionario in senhasFuncionarios:
    if senhaFuncionario in senhasEntregues:
        repetidas += 1
    elif senhaFuncionario not in senhas:
        invalidas += 1
    else:
        almocaram += 1
        
    senhasEntregues.add(senhaFuncionario)
    
print(almocaram, 'A')
print(invalidas, 'I')
print(repetidas, 'R'),