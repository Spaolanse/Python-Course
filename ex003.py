algo = input('Digite algo: ')
print('O que foi digitado é apenas número?', algo.isnumeric())
print('O que foi digitado é apenas letras?', algo.isalpha())
print('O que foi digitado é alfanumérico?', algo.isalnum())
print('O que foi digitado é decimal?', algo.isdecimal())
print('O que foi digitado estão todas as letras em minúsculo?', algo.islower())
print('O que foi digitado estão todas as letras em maiúsculo?', algo.isupper())
print('O que foi digitado tem apenas espaço?', algo.isspace())
print('O que foi digitado está capitalizado?', algo.istitle())
print(type(algo))