nome = str(input('Digite seu nome completo: ')).strip()

nome3 = nome.split()
primeiro_nome = nome3[0]
contador = len(primeiro_nome)

print('ANALISANDO SEU NOME:')

print('Seu nome com as letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é: {} e tem {} letras.'.format(primeiro_nome, contador))
