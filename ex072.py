times = ('Botafogo', 'Bragantino', 'Palmeiras', 'Flamengo', 'Athletico-PR', 'Grêmio', 'Atlético-MG', 'Fluminense',
         'Fortaleza', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Corinthians', 'Internacional', 'Bahia', 'Goiás',
         'Vasco da Gama', 'Santos', 'Coritiba',  'América-MG')
primeiros = ('Botafogo', 'Bragantino', 'Palmeiras', 'Flamengo', 'Athletico-PR')
ultimos = ('Vasco da Gama', 'Santos', 'Coritiba', 'América-MG')
santos = times.index("Santos") + 1

print(f'Lista de times do Brasileirão 2023: {times}')
print('=-'*20)
print(f'Os 5 primeiros são: {primeiros}')
print('=-'*20)
print(f'Os 4 últimos são: {ultimos}')
print('=-'*20)
print(f'Os times em ordem ficam: {sorted(times)}')
print('=-'*20)
print(f'O Santos está na posição {santos}.')
