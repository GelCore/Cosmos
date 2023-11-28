km_percorrido = float(input('Quantos KM tem sua viagem? '))
valor_passagem = km_percorrido * 0.50
valor_passagem_2 = km_percorrido * 0.45
if km_percorrido <= 200:
    print('Sua viagem custou: R$ {}'.format(valor_passagem))
else:
    print('Sua viagem custou: R$ {}'.format(valor_passagem_2))

    