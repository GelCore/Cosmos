numero = int(input('Digite um número entra 0 a 9999 e saiba suas unidades: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('A unidade deste número é: {}'.format(unidade))
print('A sua dezena é: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Mihar: {}'.format(milhar))


