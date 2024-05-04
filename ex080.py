lista = []
cont = 0
while True:
    valor = int(input('Digite um valor inteiro: '))
    lista.append(valor)
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print('=-' * 30)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem descrescente são {lista}')
lista.sort()
print(f'E os valores em ordem crescente são {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 NÃO está na lista.')
