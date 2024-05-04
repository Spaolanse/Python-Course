lista = [[], [], []]
cont = cont1 = 0
valor = pares = tres = 0
for c in range(0, 9):
    valor = (int(input(f'Digite um valor para [{cont}, {cont1}]: ')))
    cont1 += 1
    if valor % 2 == 0:
        pares += valor
    if cont1 == 3:
        cont1 = 0
        cont += 1
    if c < 3:
        lista[0].append(valor)
    if 3 <= c < 6:
        lista[1].append(valor)
    if c >= 6:
        lista[2].append(valor)
tres = lista[0][2] + lista[1][2] + lista[2][2]
print('=-' * 30)
print(f'[ {lista[0][0]:^5} ] [ {lista[0][1]:^5} ] [ {lista[0][2]:^5} ]')
print(f'[ {lista[1][0]:^5} ] [ {lista[1][1]:^5} ] [ {lista[1][2]:^5} ]')
print(f'[ {lista[2][0]:^5} ] [ {lista[2][1]:^5} ] [ {lista[2][2]:^5} ]')
print('=-' * 30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {tres}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')
