cont = 1
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    cont += 1

print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i + 1}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i + 1}...', end='')
