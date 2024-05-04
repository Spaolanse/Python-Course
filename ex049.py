soma = 0
contador = 0
for c in range(1, 7):
    numero = int(input('Digite {} número: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} números pares e a soma foi {}.'.format(contador, soma))
