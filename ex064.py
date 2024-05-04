media = maior = menor = soma = cont = 0
resp = 'S'
while resp == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar? [S/N] ')).upper().split()[0]
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
