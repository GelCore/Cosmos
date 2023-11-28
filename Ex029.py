velocidade = float(input('Digite a velocidade: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você está acima do limite e foi multado em R${:.2f}, dirija com cuidado'.format(multa))
else:
    print('Você está dentro do limite da velocidade. Dirija com cuidado!')

