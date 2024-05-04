lado1 = float(input('Primeiro segmento: '))
lado2 = float(input('Segundo segmento: '))
lado3 = float(input('Terceiro segmento: '))
if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado1+lado2:
    print('Os segmentos acima PODEM FORMAR um triângulo ',end='')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO!')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
