dados = {}
dados['nome'] = str(input('Digite o nome do aluno: '))
dados['nota'] = float(input('Digite a média do aluno: '))
print('-=' * 15)
print(f'- Nome é igual {dados["nome"]}')
print(f'- Média é igual a {dados["nota"]:.1f}')
if dados['nota'] < 5:
    print('- Situação: Reprovado!')
elif 5 < dados['nota'] < 7:
    print('- Situação: Recuperação!')
else:
    print('- Situação: Aprovado!')
