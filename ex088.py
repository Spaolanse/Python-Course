lista = list()
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"NO.":<4}{"Nome":<10}{"Média:>8"}')
print('-' * 26)
for i, c in enumerate(lista):
    print(f'{i:<4}{c[0]:<10}{c[2]:>8.1f}')
while True:
    print('-' * 35)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        print('Finalizando...')
        break
    if mostrar <= len(lista) - 1:
        print(f'Notas de {lista[mostrar][0]} são {lista[mostrar][1]}')
print('Programa finalizado!')
