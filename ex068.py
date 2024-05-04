mais_18 = 0
homem = 0
mulher_menos_20 = 0
continuar = ' '
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().split()[0]
    print('-' * 20)
    if idade >= 18:
        mais_18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if continuar == 'S':
        continue
    else:
        break
print(f'Total de pessoas com 18 anos ou mais: {mais_18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher_menos_20} mulheres com menos de 20 anos.')
