# valores = list()
# pares = list()
# impares = list()
# cont = 1
# for l in range(0, 7):
#    valores.append(int(input(f'Digite o {cont}º valor: ')))
#    cont += 1
# for i, c in enumerate(valores):
#    if c % 2 == 0:
#        pares.append(c)
#        pares.sort()
#    else:
#        impares.append(c)
#        impares.sort()
# valores.clear()
# valores.append(pares)
# valores.append(impares)
# print(f'Os valores pares digitados foram: {valores[0]}')
# print(f'Os valores ímpares digitados foram: {valores[1]}')

valores = [[], []]
valor = 0
cont = 1
for c in range(0, 7):
    valor = int(input(f'Digite o {cont}º valor: '))
    cont += 1
    if valor % 2 == 0:
        valores[0].append(valor)
        valores[0].sort()
    else:
        valores[1].append(valor)
        valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
