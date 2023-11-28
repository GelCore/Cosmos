frase = str(input('Digite sua frase aqui: ')).upper().strip()

print('Está frase tem {} letras A.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A posição que o A aparece pela última vez é a {}º'.format(frase.rfind('A')+1))