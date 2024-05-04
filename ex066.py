conta = mult = c = 0
while True:
    print('-' * 37)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*37)
    if num < 0:
        break
    for c in range(1, 11):
        mult += 1
        conta = num * mult
        print(f'{num} x {mult} = {conta}')
    mult = 0
print('Programa de tabuada encerrado!!')
