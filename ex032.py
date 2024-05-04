"""um = int(input('Digite o primeiro número: '))
dois = int(input('Digite o segundo número: '))
tres = int(input('Digite o terceiro número: '))
lista = [um, dois, tres]
print('O maior número é {}.'.format(max(lista)))
print('O menor número é {}.'.format(min(lista)))"""

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))
