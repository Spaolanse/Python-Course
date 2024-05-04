from datetime import date
atual = date.today().year
mulher = 0
homem = 0
menor = 0
maior = 0
media = 0
somaidade = 0
velho = 0
nome_velho = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    media = somaidade / 4
    if idade < 20:
        menor += 1
    else:
        maior += 1
    if sexo == 'F':
        mulher += 1
    else:
        homem += 1
    if c == 1:
        velho = idade
    if idade > velho:
        velho = idade
        if velho == velho:
            nome_velho = nome

print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nome_velho))
print('O grupo possui {} mulheres com menos de 20 anos e {} pessoas com mais de 20 anos.'.format(menor, maior))
