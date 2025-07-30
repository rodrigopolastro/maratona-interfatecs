################################################################################
# Objetivo:
#
# Autor: Rodrigo
# Data: 16/07/2025
# Duração: (inicio 19:40) - 19:56 (16)
################################################################################

# CODIGOS CURSO FATEC GERAL
# 048 – Análise e Desenvolvimento de Sistemas
# 061 – Sistemas Biomédicos
# 073 – Eletrônica Automotiva
# 074 – Logística
# 080 – Polímeros
# 081 – Processos Metalúrgicos
# 099 – Projetos Mecânicos
# 100 – Fabricação Mecânica

# TURNOS FATEC GERAL
# manha -> 1
# tarde -> 2
# noite -> 3

# CODIGOS CURSOS SOROCABA
# AD – Análise e Desenvolvimento de Sistemas (manhã)
# AN – Análise e Desenvolvimento de Sistemas (noite)
# SD – Sistemas Biomédicos (manhã)
# LT – Logística (tarde)
# PL – Polímeros (tarde)
# PD – Projetos Mecânicos (manhã)
# PN – Projetos Mecânicos (noite)
# OD – Fabricação Mecânica (manhã)
# ON – Fabricação Mecânica (noite)


MAP_CURSOS_SOROCABA = {
    'AD': ['048', '1'],
    'AN': ['048', '3'],
    'SD': ['061', '1'],
    'LT': ['074', '2'],
    'PL': ['080', '2'],
    'PD': ['099', '1'],
    'PN': ['099', '3'],
    'OD': ['100', '1'],
    'ON': ['100', '3']
}

qtdCasos = int(input())
for _ in range(qtdCasos):
    raSorocaba = input() #formato: CCAASNNN
    
    siglaCurso = raSorocaba[0:2]
    anoIngresso = raSorocaba[2:4]
    semestre = raSorocaba[4]
    numeroAluno = raSorocaba[5:8]
    # print(siglaCurso, anoIngresso, semestre, numeroAluno)


    codigoCurso, turno = MAP_CURSOS_SOROCABA[siglaCurso]
    raNovo = '003' + codigoCurso + anoIngresso + semestre + turno + numeroAluno
    print(raNovo)
    


