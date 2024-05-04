casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, anos, (casa/(anos * 12))))
if casa/(anos * 12) <= salario * 30/100:
    print('Empréstimo APROVADO!')
elif casa/(anos * 12) > salario * 30/100:
    print('Empréstimo NEGADO!')
