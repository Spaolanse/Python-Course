largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
quantidade_de_tinta = area/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(quantidade_de_tinta))
