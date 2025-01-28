################################################################################
# Objetivo: Determinar para qual divindade de sonambulismo vai aquela determinada pessoa a dormir
# OBS: basicamente é fazer resto de divisão
#///////////////////////////////////////////////////////////////
#/// Regras:                                                 ///
#/// a primeira pessoa a dormir vai para a divindade Carlos  ///
#/// a segunda pessoa a dormir vai para a divindade Zeca     ///
#/// a terceira pessoa a dormir vai para a divindade Pedro   ///
#/// a quarta pessoa a dormir vai para a divindade Mara      ///
#/// e assim por diante                                      ///
#///////////////////////////////////////////////////////////////
# Autor: Alexandre
# Data: 28/01/2025
# Duração: 3min
################################################################################
#inicio= 7:24PM / término=  7:27PM

while True:
    entrada = int(input())
    if entrada == 0:
        break
    divindades = {
        1:"Carlos",
        2:"Zeca",
        3:"Pedro",
        0:"Mara"
    }
    print(divindades[entrada%4])