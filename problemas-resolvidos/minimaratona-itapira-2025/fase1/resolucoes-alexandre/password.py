"""
senha nao deve conter caracteres especiais ou acentos ou espacos
deve conter pelo menos 1 letra maiuscula, 1 minuscula e 1 nu8mero
deve ser entre 6 e  15
nao pode haver sequencias tipo ab ou 12

"""
import string
def contemMaiuscula(texto):
    for chrt in texto:
        if chrt in string.ascii_uppercase:
            return True
    return False

def contemNum(texto):
    for chrt in texto:
        if chrt in string.digits:
            return True
    return False

def contemMinus(texto):
    for chrt in texto:
        if chrt in string.ascii_lowercase:
            return True
    return False

def estaSequencia(texto):
    try:
        for i in range(len(texto)):
            teste = texto[i:i+2]
            if (texto[i:i+2] in string.ascii_lowercase or texto[i:i+2] in string.ascii_uppercase or texto[i:i+2] in string.digits) and len(teste) == 2:
                return True
        return False
    except Exception:
        return False



entradaSenha = input()
if len(entradaSenha) < 6 or len(entradaSenha) > 15:
    print('False.')
else:
    if contemMaiuscula(entradaSenha) and contemMinus(entradaSenha) and contemNum(entradaSenha) and not estaSequencia(entradaSenha):
        print("True.")
    else:
        print('False.')
