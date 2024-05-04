print('-' * 20)
print('Loja Super Baratão')
print('-' * 20)
cont1000 = 0
total = 0
barato = 0
cont = 0
produto_barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    if preco >= 1000:
        cont1000 += 1
    total += preco
    if cont == 1:
        barato = preco
        produto_barato = produto
    else:
        if preco < barato:
            barato = preco
            produto_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if continuar == 'S':
        continue
    else:
        break
print('{:-^40}'.format('FIM DO PROGRAMA!!'))
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {cont1000} produtos custando acima de R$1000.00.')
print(f'O produto mais barato foi {produto_barato} no valor de {barato:.2f}.')
