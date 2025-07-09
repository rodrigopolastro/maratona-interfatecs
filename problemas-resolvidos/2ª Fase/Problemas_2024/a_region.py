ceps_aceitos = []
ceps_recusados = []
intervalos = []

def int_cep(str_cep):
    partes_cep = str_cep.split('-')
    int_cep = int(partes_cep[0] + partes_cep[1])
    
    return int_cep

qtd_regioes = int(input())
for _ in range(qtd_regioes):
    entrada = input().split(' ') 
    intervalos.append([entrada[0], entrada[1]])
    
qtd_pedidos = int(input())
for _ in range(qtd_pedidos):
    str_cep = input()
    
    foi_aceito = False
    for intervalo in intervalos:
        if int_cep(intervalo[0]) <= int_cep(str_cep) <= int_cep(intervalo[1]):
            ceps_aceitos.append(str_cep)
            foi_aceito = True
        
    if not foi_aceito:
        ceps_recusados.append(str_cep)
    
ceps_aceitos.sort()
ceps_recusados.sort()

for cep_aceito in ceps_aceitos:
    print(f"{cep_aceito} is served by our delivery system")
    
for cep_recusado in ceps_recusados:
    print(f"{cep_recusado} is not served by our delivery system")
    
    
