from random import randint
cont = 0
while True:
    print('=-'*15)
    print('Vamos Jogar Par ou Ímpar')
    print('=-' * 15)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).upper().split()[0]
    print(f'Você jogou {jogador} e o computador {computador} total {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
