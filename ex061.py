print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -'.format(termo), end=' ')
        cont += 1
        termo += razao
    print('Pausa!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
