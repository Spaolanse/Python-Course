preco = float(input('Qual é o valor do produto? R$'))
desconto = preco - (preco * 5 / 100)
print(
    'O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, desconto))

# (((100-5)/100)*preco) tbm da pra usar isso no lugar
