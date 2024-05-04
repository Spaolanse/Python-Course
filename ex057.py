from random import randint
aleatorio = int(randint(1, 10))
contador = 1
print('Sou seu computador...')
print('Vou pensar em um número entre 0 e 10. Tente adivinhar.')
numero = int(input('Qual é o seu palpite? '))
while numero != aleatorio:
    contador += 1
    if numero > aleatorio:
        numero = int(input('Menos...Tente mais uma vez. '))
    elif numero < aleatorio:
        numero = int(input('Mais...Tente mais uma vez. '))
print('Parabéns, você acertou com um total de {} tentativas.'.format(contador))
