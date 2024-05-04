#expressao = input('Digite uma expressão: ')
#if '(' and ')' not in expressao:
#   print('Sua expressão não possui parenteses!')
#else:
#  if expressao.count('(') == expressao.count(')'):
#       print('Sua expressão está correta!')
#    else:
#        print('Sua expressão está incorreta!')


expr = str(input('Digite sua expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')
