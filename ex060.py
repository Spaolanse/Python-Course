print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = primeiro
cont = 1
while cont <= 10:
    cont += 1
    n += razao
    print('{} -'.format(n), end=' ')
print('Acabou!')
