class solution:
    def __init__(self,matriz,posicao):
        self.x = posicao[0]
        self.y = posicao[1]
        self.valor = matriz[self.x][self.y]
        self.ativo = False
        self.verificado = False
    def __repr__(self):
        if self.verificado == True and self.ativo==False:
            return "X\n"
        elif self.ativo == False:
            return f"O {self.valor}\n"
        return f"pos-x {self.x} , pos-y {self.y}, valor {self.valor},  ativo {self.ativo},  verificado {self.verificado}\n"
listaobjetos = []


input1 = list(map(int,input().split(" ")))
l = tuple(map(int,input().split(" ")))
p = (l[0]-1,l[1]-1)


fileiras,colunas = input1[0],input1[1]
M = []
for i in range(fileiras):
    M.append(list(map(int,input().split(' '))))
for i in range(len(M)):
    for j in range(len(M[0])):
        obj = solution(M,(i,j))
        listaobjetos.append(obj)
for obj in listaobjetos:
    if obj.x == p[0] and obj.y == p[1]:
        obj.ativo = True
        break
varredura = 1
tentar = []
VB = ""
while varredura != 0:
    tentar=[]
    varredura = 0
    for obj in listaobjetos:
        if obj.ativo == True and obj.verificado == False:
            obj.verificado = True
            varredura = 1
            VB = obj
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    tentar.append((obj.x+i,obj.y+j))
            break
    for pessoa in listaobjetos:
        if pessoa.ativo ==False:
            pass
        else:
            for aluno in tentar:
                if aluno[0] >= 0 and aluno[0] < len(M) and aluno[1] >= 0 and aluno[1] < len(M[0]):
                    for i in listaobjetos:
                        if i.x == aluno[0] and i.y == aluno[1]:
                            if i.valor < VB.valor:
                                i.ativo = True
                                break
                            else:
                                pass
votosValidos = 0
totalVotos = len(listaobjetos)
for i in listaobjetos:
    if i.ativo == True:
        votosValidos +=1
if votosValidos > totalVotos/2:
    print(votosValidos,'maioria')
else:
    print(votosValidos)

    


