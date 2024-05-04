numero = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha uma das bases para conversão:\n'
                    '[ 1 ] converter para BINÁRIO.\n'
                    '[ 2 ] converter para OCTAL.\n'
                    '[ 3 ] converter para HEXADECIMAL.\n'
                    'Sua opção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')
