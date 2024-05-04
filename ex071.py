
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze',
                                'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    while numero not in range(0, 21):
        numero = int(input('Tente novamente.Digite um número entre 0 e 20: '))

    if numero in range(0, 21):
        print(f'Você digitou o número {extenso[numero]}.')

    continuar = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
print('Fim do programa!')
