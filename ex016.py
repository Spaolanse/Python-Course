'''from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}.'.format(hypot(oposto, adjacente)))'''

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (oposto**2 + adjacente**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
