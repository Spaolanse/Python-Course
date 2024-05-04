# Forma que eu fiz antes de ver a resolução
lista = [[], [], []]
cont = cont1 = 0
valor = 0
for c in range(0, 9):
    valor = (int(input(f'Digite um valor para [{cont}, {cont1}]: ')))
    cont1 += 1
    if cont1 == 3:
        cont1 = 0
        cont += 1
    if c < 3:
        lista[0].append(valor)
    if 3 <= c < 6:
        lista[1].append(valor)
    if c >= 6:
        lista[2].append(valor)
print(f'[ {lista[0][0]:^5} ] [ {lista[0][1]:^5} ] [ {lista[0][2]:^5} ]')
print(f'[ {lista[1][0]:^5} ] [ {lista[1][1]:^5} ] [ {lista[1][2]:^5} ]')
print(f'[ {lista[2][0]:^5} ] [ {lista[2][1]:^5} ] [ {lista[2][2]:^5} ]')
print('=-' * 30)

# Forma que o curso ensinou na resolução do exercício
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-' * 30)
