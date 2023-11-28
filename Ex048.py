# Acomula a soma entre os números
soma_mult_impares = 0
# Conta quantos são os números ímpares múltiplos de 3
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma_mult_impares += n
        contador += 1
print('A soma entre os valores múltiplos de 3 e impares é: {} e sua quantidade é: {}'.format(
    soma_mult_impares, contador))
