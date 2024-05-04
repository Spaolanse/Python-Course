lista = []
pares = []
impares = []
while True:
    valor = (int(input('Digite um valor: ')))
    lista.append(valor)
    continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
for i, c in enumerate(lista):
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'A lista completa é {lista}')
print(f'A lista de ímpares é {impares}')
print(f'A lista de pares é {pares}')
