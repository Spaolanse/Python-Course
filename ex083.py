lista = []
pessoas = []
pesada = leve = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesada = leve = pessoas[1]
    else:
        if pessoas[1] > pesada:
            pesada = pessoas[1]
        if pessoas[1] < leve:
            leve = pessoas[1]
    lista.append(pessoas[:])
    pessoas.clear()
    continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break

print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {pesada}Kg. Peso de ', end='')
for p in lista:
    if p[1] == pesada:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {leve}Kg. Peso de ', end='')
for p in lista:
    if p[1] == leve:
        print(f'[{p[0]}]', end='')
