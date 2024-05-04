mult = 0
conta = 0
numero = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    mult += 1
    conta = numero * mult
    print('{} x {} = {}'.format(numero, mult, conta))

'''numero = int(input('Digite um número para ver sua tabuada: '))
    for c in range(1, 11):
    print('{} x {:2} = {}'.format(numero, c, numero*c))'''
