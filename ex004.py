valor = input('Digite algo: ')
print('Este valor é númerico? {}\n '
'Este valor é alfa numerico {}\n '
'Este valor tem espaços? {} ').format(valor.isalnum(), valor.isalnum(), valor.isspace())


