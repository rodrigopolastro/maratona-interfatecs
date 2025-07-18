#inicio 9:04   fim 9:38

def montarTurmas(sigla:str,predio,maxturma,manha,tarde,noite):
    respostas = []
    sigla = sigla.upper()
    turmasManha = "ABCDEFGHI"
    turmasTarde = "JKLMNO"
    turmasNoite = "PQRSTUVWXYZ"
    if manha > 0:
        if manha < maxturma:
            respostas.append(sigla+'1'+"A"+predio)
        else:
            for i in range(0,11):
                if manha <= 0:
                    break
                manha -= maxturma
                respostas.append(sigla+'1'+turmasManha[i]+predio)
                
    
    if tarde > 0:        
        if tarde < maxturma:
            respostas.append(sigla+'2'+"J"+predio)
        else:
            for i in range(0,11):
                if tarde <= 0:
                    break
                tarde -= maxturma
                respostas.append(sigla+'2'+turmasTarde[i]+predio)
                
            
    if noite > 0:
        if noite < maxturma:
            respostas.append(sigla+'3'+"P"+predio)
        else:
            for i in range(0,11):
                if noite <= 0:
                    break
                noite -= maxturma
                respostas.append(sigla+'3'+turmasNoite[i]+predio)
    print(" ".join(respostas))
                


def main():
    qtdCasosTeste = int(input())
    for i in range(qtdCasosTeste):
        siglaCurso,predio,qtdMaximaPorTurma,alunosManha,alunosTarde,alunosNoite = input().split()    
        qtdMaximaPorTurma = int(qtdMaximaPorTurma)
        alunosManha = int(alunosManha)
        alunosTarde = int(alunosTarde)
        alunosNoite = int(alunosNoite) 
        montarTurmas(siglaCurso,predio, qtdMaximaPorTurma, alunosManha,alunosTarde,alunosNoite)
    
    
    
main()