from time import sleep
print('{:=^40}'.format('SUPLEMENTOS GCORE'))
print()
valor_produto = float(input('Digite o valor da compra:R$ '))
print('ESCOLHA FORMA DE PAGAMENTO')
print()
sleep(2)
print('''[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Digite a opção desejada: '))
if opçao == 1:
    total_final = valor_produto - (0.1 * valor_produto)
    print('O valor da compra é de {} com o desconto de 10%'.format(total_final))
elif opçao == 2:
    total_final = valor_produto - (0.05 * valor_produto)
    print('O valor da compra é de {} à vista no cartão.'.format(total_final))
elif opçao == 3:
    total_final = valor_produto / 2
    print('O valor da compra é de {} parcelado em 2x SEM JUROS'.format(total_final))
elif opçao == 4:
    total_final = valor_produto + (0.2 * valor_produto)
    print('O valor da compra é de {} com 20% de JUROS'.format(total_final))
