from time import sleep
print('\033[4;35;40mCONVERSOR DE GRUPOS NÚMERICOS')
print()
decimal = int(input('\033[0;30mDigite um número inteiro qualquer: '))
print('Para converter seu número escolha primeiro as opções digitando o número correspondente:')

print('AGUARDE!!!')
sleep(10)
print('1 - para Binário')
print('2 - para Octal')
print('3 - para Hexadecimal')
sleep(3)
escolha = int(input('Digite o número correspondente: '))
if escolha == 1:
    print('O número {} em binário é igual a: {}'.format(
        decimal, bin(decimal).replace('0b', '')))
elif escolha == 2:
    print('O número {} em Octal é igual a: {}'.format(
        decimal, oct(decimal).replace('0o', '')))
else:
    print('O número {} em Hexadecimal é igual a: {}'.format(
        decimal, hex(decimal)))
