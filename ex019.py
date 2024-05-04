from random import shuffle
primeiro = str(input('Digite o nome do primeiro aluno: '))
segundo = str(input('Digite o nome do segundo aluno: '))
terceiro = str(input('Digite o nome do terceiro aluno: '))
quarto = str(input('Digite o nome do quarto aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
shuffle(lista)
print('A ordem de apresentação será.')
print(lista)
