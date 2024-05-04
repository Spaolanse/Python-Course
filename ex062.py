termos = int(input('Quantos termos você quer mostrar? '))
ultimo = 1
penultimo = 1
if (termos == 1) or (termos == 2):
    print('1')
else:
    count = 3
    while count <= termos:
        n = ultimo + penultimo
        penultimo = ultimo
        ultimo = n
        count += 1
        print(n)
