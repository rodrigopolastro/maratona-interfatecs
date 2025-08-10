from string import ascii_lowercase, ascii_uppercase

acentos = 'áéíóúâêôãàçÁÉíóÚÃÔÔÕÀÇ.,!?;:'
MAIUSCULAS = ascii_uppercase
MINUSCULAS = ascii_lowercase
NUMEROS = '0123456789'

def temEspacos(senha):
    for c in senha:
        if c == ' ':
            return True
    return False

def temAcentos(senha):
    for c in senha:
        if c in acentos:
            return True
    return False

def temMaiusculas(senha):
    for c in senha:
        if c in MAIUSCULAS:
            return True
    return False

def temMinusculas(senha):
    for c in senha:
        if c in MINUSCULAS:
            return True
    return False

def temNumeros(senha):
    for c in senha:
        if c in NUMEROS:
            return True
    return False

def tipoChar(c):
    if c in MAIUSCULAS: return 'maiuscula'
    if c in MINUSCULAS: return 'minuscula'
    if c in NUMEROS: return 'numero'

def temValoresSequencia(senha, tamanhoSenha):
    for i in range(tamanhoSenha-1):
        atual, proximo = senha[i], senha[i+1]
        tipoAtual, tipoProximo = tipoChar(atual), tipoChar(proximo)
        if tipoAtual != tipoProximo:
            continue
        
        if tipoAtual == 'maiuscula':
            if MAIUSCULAS.find(atual)+1 == MAIUSCULAS.find(proximo):
                return True
        if tipoAtual == 'minuscula':
            if MINUSCULAS.find(atual)+1 == MINUSCULAS.find(proximo):
                return True
        if tipoAtual == 'numero':
            if NUMEROS.find(atual)+1 == NUMEROS.find(proximo):
                return True
    return False

def senhaValida(senha):
    tamanhoSenha = len(senha)
    if tamanhoSenha < 6 or tamanhoSenha > 15:
        return False
    
    if temEspacos(senha):
        return False
    
    if temAcentos(senha):
        return False
    
    if not temMaiusculas(senha):
        return False
    
    if not temMinusculas(senha):
        return False
    
    if not temNumeros(senha):
        return False
    
    if temValoresSequencia(senha, tamanhoSenha):
        return False
    
    return True
        
senha = input()
if senhaValida(senha):
    print('True.')
else:
    print('False.')