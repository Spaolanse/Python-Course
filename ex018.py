from random import choice
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
listaalunos = [primeiro, segundo, terceiro, quarto]
print('O aluno escolhido foi {}.'.format(choice(listaalunos)))
