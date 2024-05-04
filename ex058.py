primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
finalizar = False
while not finalizar:
    print('[ 1 ] Somar\n'
          '[ 2 ] Multiplicar\n'
          '[ 3 ] Maior\n'
          '[ 4 ] Novos números\n'
          '[ 5 ] Sair do programa')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = primeiro + segundo
        print('A soma entre {} e {} é igual a {}'.format(primeiro, segundo, soma))
        print('=-=' * 10)
    elif opcao == 2:
        mult = primeiro * segundo
        print('A multiplicação de {} e {} é igual a {}'.format(primeiro, segundo, mult))
        print('=-=' * 10)
    elif opcao == 3:
        maior = 0
        if primeiro < segundo:
            maior = segundo
        if primeiro > segundo:
            maior = primeiro
        print('Entre {} e {} o maior é {}.'.format(primeiro, segundo, maior))
        print('=-=' * 10)
    elif opcao == 4:
        print('Informe os números novamente:')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
        print('=-=' * 10)
    elif opcao == 0 or opcao > 5:
        print('Opção inválida, tente novamente.')
        print('=-=' * 10)
    elif opcao == 5:
        print('Fim do programa! Volte sempre!')
        finalizar = True
        print('=-=' * 10)
print('Programa finalizado!')
