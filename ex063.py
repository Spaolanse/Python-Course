cont = 0
n1 = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    n1 += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, n1))
