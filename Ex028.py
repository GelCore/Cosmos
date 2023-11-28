from random import randint
from time import sleep
numero = int(input('Tente adivinhar o número que estou pensando entre 0 e 5: '))
numero_randomico = randint(0,5)
if numero == numero_randomico:
    print('PROCESSANDO... AGURDE.')
    sleep(3)    
    print('Parabéns você acertou eu realmente pensei no {}'.format(numero_randomico))
else:
    print('PROCESSANDO... AGURDE.')
    sleep(3)    
    print('Você errou eu estava pensando no {}'.format(numero_randomico))




