perfis = int(input())
requerimentoPerfil = list(map(int,input().split(' ')))
cadastrados = int(input())
output = []
for i in range(cadastrados):
    cadastro = input().split(' ',1)
    menorDivisor = 0
    for index in range(len(cadastro[1].split(' '))):
        if index == 0:
            menorDivisor = int(cadastro[1].split(' ')[index]) // requerimentoPerfil[index]
        else:
            if int(cadastro[1].split(' ')[index]) // requerimentoPerfil[index] < menorDivisor:
                menorDivisor = int(cadastro[1].split(' ')[index]) // requerimentoPerfil[index]
    output.append(f"{cadastro[0]} {menorDivisor}")
for resposta in output:
    print(resposta)