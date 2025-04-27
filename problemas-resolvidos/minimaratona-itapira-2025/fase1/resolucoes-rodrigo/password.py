import unicodedata
from string import ascii_lowercase, ascii_uppercase

def tem_acentos(texto):
    for c in unicodedata.normalize('NFD', texto):
        if unicodedata.category(c) == 'Mn':
            return True
    return False

def tem_maiuscula(texto):
    for maiuscula in ascii_uppercase:
        if maiuscula in texto:
            return True
        
    return False

def tem_minuscula(texto):
    for minuscula in ascii_lowercase:
        if minuscula in texto:
            return True
        
    return False

def tem_numero(texto):
    for numero in range(10):
        if str(numero) in texto:
            return True

    return False

def senhaEhValida(senha):
    if tem_acentos(senha):
        return False

    if len(senha) < 6 or len(senha) > 15:
        return False
    
    for i in range(len(senha)-1):
        if abs(ord(senha[i]) - ord(senha[i+1])) == 1:
            return False
        
    if not tem_maiuscula(senha):
        return False
    
    if not tem_minuscula(senha):
        return False
    
    if not tem_numero(senha):
        return False
    
    return True
        
senha = input()
if senhaEhValida(senha):
    print("True.")
else:
    print("False.")



    