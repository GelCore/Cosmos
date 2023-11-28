nome_da_pessoa = str(input('Digite seu nome completo: ')).strip()
detector_de_silva = ('silva' in nome_da_pessoa.lower())
print('Seu nome tem Silva? {}'.format(detector_de_silva))