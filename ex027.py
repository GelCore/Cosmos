nome = str(input('Digite seu nome completo: ')).strip()
primeiro_nome = nome.split()
print('Seu primeiro nome é: {}'.format(primeiro_nome[0]))
print('Seu último nome é: {}'.format(primeiro_nome[len(primeiro_nome)-1]))