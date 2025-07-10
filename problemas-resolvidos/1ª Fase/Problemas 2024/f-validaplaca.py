import re

placa = input()
padraoAAA_9999 = re.compile(r'[A-Z]{3}[0-9]{4}')
padraoAA_9999 = re.compile(r'[A-Z]{2}[0-9]{4}')
padraoMuitoAntiga = re.compile(r'[AP]{1}[0-9]{1,5}')
padraoNumerica = re.compile(r'[0-9]{1,7}')
padraoMercosul = re.compile(r'[A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2}')
if padraoAAA_9999.match(placa) and len(placa) == 7:
    print('Placa AAA-9999')
elif padraoAA_9999.match(placa) and len(placa) == 6:
    print('Placa AA-9999')
elif padraoMuitoAntiga.match(placa) and len(placa) <= 6:
    print('Placa muito antiga')
elif padraoNumerica.match(placa) and len(placa) <= 7:
    print('Placa numerica')
elif padraoMercosul.match(placa) and len(placa) == 7:
    print('Placa mercosul')
else:
    print('Placa invalida') 


