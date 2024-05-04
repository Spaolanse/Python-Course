primeira = float(input('Digite a primeira nota: '))
segunda = float(input('Digite a segunda nota: '))
media = (primeira + segunda) / 2
if media < 5:
    print('A média do aluno é {:.1f}, então ele está REPROVADO.'.format(media))
elif 5 <= media < 7:
    print('A média do aluno é {:.1f}, então ele está de RECUPERAÇÃO.'.format(media))
elif media >= 7:
    print('A média do aluno é {:.1f}, então ele está APROVADO.'.format(media))
