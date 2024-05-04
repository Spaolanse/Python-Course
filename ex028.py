"""velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade <= 80:
    print('Você está dentro do limite.')
else:
    print('Multado! Você excedeu o limite permitido que é 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format((velocidade-80)*7))
print('Tenha um bom dia! Dirija com segurança!')"""


velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é 80Km/h.')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
