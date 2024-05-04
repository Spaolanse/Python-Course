lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    for i, v in enumerate(lista):
        if v in lista[i+1:]:
            lista.remove(valor)
            print('Valor repetido, não irei adicionar na lista!')
    continuar = str(input('quer continuar? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(input('quer continuar? [S/N] ')).upper().split()[0]
    lista.sort()
    if continuar != 'S':
        print(f'Você digitou os valores {lista}')
        break
