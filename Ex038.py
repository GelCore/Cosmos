print('\033[0;34;36mCOMPARANDO OS INTEIROS')
numero1 = int(input('\033[0;40mDigite um número inteiro: '))
numero2 = int(input('\033[0;40m30Digite o segundo número inteiro: '))
if numero1 > numero2:
    print('Os números digitados são: {} e {}. {} é maior que {}.'.format(
        numero1, numero2, numero1, numero2))
elif numero2 > numero1:
    print('Os números digitados são: {} e {}. {} é maior que {}'.format(
        numero1, numero2, numero2, numero1))
elif numero1 == numero2:
    print('Os números {} e {} são iguais.'.format(numero1, numero2))
