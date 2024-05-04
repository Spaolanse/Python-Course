print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(primeiro, razao*10, razao):
    print('{} -'.format(c), end=' ')
print('Acabou!')
