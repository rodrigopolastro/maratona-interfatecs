# """ 
# listar requisitos:
# id > nome > media > melhor 
# classe?

# melhor dá para juntar com 00:00 e usar como string mesmo
# media para tempos vamos ter que considerar milisegundos, e contando também que sobre regras de abreviamento (verificar depois) onde com 1 falta vamos ter que transformar onde for
# DNF no pior tempo de jogo que ele teve ( 10 5 4 0 2 vira 10 5 4 10 2 )
# para decidir o melhor ordenado por média vai ter que ser no final dos registros de cada lista



# estrutura base?
# classe que contenha:
# -id
# -nome
# -*pontuações
# -melhor

# também tenho que conseguir definir pontuações para ordenar, pode ser mais facil, então:

# -pontuacao

# como a ideia é organizar de 'melhor para pior', algo que seja multiplicado,
# então a prioridade é a média, multiplicamos ela por 100, a segunda prioridade é tempo, então multiplicamos por 100.000, e dnf equivale a 10.000.000
# uma vez esses numeros em sua pontuação, posso definir que eles serão organizados por sua pontuação e retornados, onde, uma vez armazenados os atributos posso voltar com eles
# para o print



# como vou fazer estrutura para os participantes? uma função / array externo ou interno? talvez um array externo e um array interno onde o array interno eu procuro com uma função
# interna de classe e o array externo eu uso apenas para armazenar a 'key' (que no caso é o id) de cada participante para saber quem devo modificar/chamar/procurar
# """
class Participante:
    def __init__(self,id,nome,pontuacoes:list):
        self.id = id
        self.nome = nome
        pont = Participante.formatarDNF(pontuacoes)
        self.rank = Participante.ranking(pont)
        self.media = Participante.unix_to_string(Participante.calc_media(pont))
        self.melhor = Participante.pegar_melhor(pont)

    def __str__(self):
        return f'id > {self.id}\nnome>{self.nome}\nrank>{self.rank}\nmedia>{self.media}\nmelhor>{self.melhor}'
    def ranking(pontuacao:list):
        retornar = 0
        for i in pontuacao:
            if i == 'DNF':
                retornar+=10000000000000000000000000000
            else:
                retornar+=Participante.string_to_unix(i)
        return retornar
    def formatarDNF(pontuacoes:list):
        retornar = []
        for i in pontuacoes:
            if i == '0:00:000':
                retornar.append('DNF')
            else:
                retornar.append(i)
        return retornar


    def string_to_unix(time:str):
        try:
            time = time.split(':')

            return (int(time[0])*60)*1000 + int(time[1])*1000 + (int(time[2]))
        except:
            return 'DNF'



    def unix_to_string(time):
        try:
            time = int(time)
        except:
            return 'DNF'
        minutos = time//1000//60
        segundos = time//1000
        milisegundos = time%1000
        if minutos == 0:
            if segundos < 10:
                return f'0{segundos}:{milisegundos:0<3}'
            else:
                return f'{segundos}:{milisegundos:0<3}'
        else:
            if segundos < 10:
                return f'{minutos}:0{segundos}:{milisegundos:0<3}'
            else:
                return f'{minutos}:{segundos}:{milisegundos:0<3}'
            

    def calc_media_somartudo(lista):
        retornar = 0
        for i in lista:
            retornar+=i
        return retornar
    def calc_media(pontuacoes:list):
        if pontuacoes.count('DNF') > 1:
            return 'DNF'
        elif pontuacoes.count('DNF') == 1:
            lista_pontuacoes = []
            for i in pontuacoes:
                if i == 'DNF':
                    pass
                else:
                    lista_pontuacoes.append(Participante.string_to_unix(i))
            lista_pontuacoes.append(max(lista_pontuacoes))
            lista_pontuacoes.sort()
            lista_pontuacoes.pop()
            lista_pontuacoes.pop(0)
            return Participante.calc_media_somartudo(lista_pontuacoes)/3
        else:
            lista_pontuacoes = []
            for i in pontuacoes:
                lista_pontuacoes.append(Participante.string_to_unix(i))
            lista_pontuacoes.sort()
            lista_pontuacoes.pop()
            lista_pontuacoes.pop(0)

            return Participante.calc_media_somartudo(lista_pontuacoes)/3
    def pegar_melhor(lista:list):
        while 'DNF' in lista:
            lista.remove('DNF')
        if not lista:
            return 'DNF'
        else:
            lista.sort()
            return lista[0]
            
                
    def remover(lista:list,index):
        for i in range(index,len(lista)+1):
            if lista[i] == '-':
                lista.pop(i)
                break
        
        
    def organizar(lista):
        retornar = list('-'*len(lista))
        for i in lista:
            contador = 0
            for j in lista:
                if i.rank > j.rank:
                    contador+=1
            retornar.insert(contador,i)
            Participante.remover(retornar,contador)
        return retornar


def main():
    numero_participantes = int(input())

    participantes = dict()
    for i in range(1,numero_participantes+1):
        try:
            participantes[i]=' '.join(input().split(' ')[1:])
        except:
            participantes[i]=' '.join(input().split(' ')[1])
    while True:
        

        try:
            participantes_modalidade = input().split(' ')
 
            part = int(participantes_modalidade[0])
            modalidade = participantes_modalidade[1:]
        except:
            break       
       
        quem_participar = []
        for i in range(part):
            entrada_tempos_participantes = input().split(' ')
            quem_participar.append(Participante(int(entrada_tempos_participantes[0]),participantes[int(entrada_tempos_participantes[0])],entrada_tempos_participantes[1:]))
        quem_participar = Participante.organizar(quem_participar)
            
        print(f'.Id.Nome.......................Media......Melhor')
        print(f'{' '.join(modalidade)}')
        
        for participante in quem_participar:
            print(f'{participante.id:>3} {participante.nome:<20}{participante.media:>12}{participante.melhor:>12}')
main()
