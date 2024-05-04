from random import randint
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
numero = int(input('Em qual número eu pensei? '))
aleatorio = int(randint(1, 10))
if numero == aleatorio:
    print('Parabéns, você acertou!')
else:
    print('Você errou, o número era {}.'.format(aleatorio))
