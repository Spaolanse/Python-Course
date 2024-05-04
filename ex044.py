from time import sleep
from random import randrange
print('Suas opções: ')
player = int(input('''[ 0 ]Pedra
[ 1 ]Papel
[ 2 ]Tesoura
Qual é sua jogada? '''))
pc = int(randrange(3))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=' * 15)
if player == 0 and pc == 0:
    print('Computador jogou PEDRA')
    print('Jogador jogou PEDRA')
elif player == 0 and pc == 1:
    print('Computador jogou PAPEL')
    print('Jogador jogou PEDRA')
elif player == 0 and pc == 2:
    print('Computador jogou TESOURA')
    print('Jogador jogou PEDRA')
if player == 1 and pc == 1:
    print('Computador jogou PAPEL')
    print('Jogador jogou PAPEL')
elif player == 1 and pc == 0:
    print('Computador jogou PEDRA')
    print('Jogador jogou PAPEL')
elif player == 1 and pc == 2:
    print('Computador jogou TESOURA')
    print('Jogador jogou PAPEL')
if player == 2 and pc == 2:
    print('Computador jogou TESOURA')
    print('Jogador jogou TESOURA')
elif player == 2 and pc == 0:
    print('Computador jogou PEDRA')
    print('Jogador jogou TESOURA')
elif player == 2 and pc == 1:
    print('Computador jogou PAPEL')
    print('Jogador jogou TESOURA')
print('-=' * 15)

if player == pc:
    print('Empate.')
elif player == 0 and pc == 1:
    print('O computador venceu!')
elif player == 0 and pc == 2:
    print('O jogador venceu!')
elif player == 1 and pc == 0:
    print('O jogador venceu!')
elif player == 1 and pc == 2:
    print('O computador venceu!')
elif player == 2 and pc == 1:
    print('O jogador venceu!')
elif player == 2 and pc == 0:
    print('O computador venceu!')
