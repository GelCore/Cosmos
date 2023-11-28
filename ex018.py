'''PROGRAMA TESTE PARA OBTENÇÃO DOS VALORES DE SENO, COSSENO E TANGENTE'''

import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('<><><><><>RESULTADOS<><><><><><>')

print('O seno de {} é igual a: {}'.format(angulo, seno))
print('O cosseno é igual a: {}'.format(cosseno))
print('E sua tangente é: {}'.format(tangente))


