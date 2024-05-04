valor = float(input('Preço das compras: R$'))
pagamento = int(input('FORMAS DE PAGAMENTO\n'
                      '[ 1 ] à vista dinheiro/cheque\n'
                      '[ 2 ] à vista cartão\n'
                      '[ 3 ] 2x no cartão\n'
                      '[ 4 ] 3x ou mais no cartão\n'
                      'Qual é a opção? '))
if pagamento == 1:
    print('Sua compra de R${:.2f} irá custar R${:.2f} com 10% de desconto.'.format(valor, (valor - (valor * 10/100))))
elif pagamento == 2:
    print('Sua compra de R${:.2f} irá custar R${:.2f} com 5% de desconto.'.format(valor, (valor - (valor * 5/100))))
elif pagamento == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(valor / 2))
    print('Sua compra custará R${:.2f}, para esta opção não há desconto e nem juros.'.format(valor))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = valor + (valor * 20/100)
    vezes = juros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com 20% DE JUROS.'.format(parcelas, vezes))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, juros))
else:
    print('Opção inválida. Por favor digite uma opção válida.')
