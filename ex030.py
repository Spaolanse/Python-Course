distancia = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia * 0.5))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia * 0.45))


"""distancia = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))"""
