salario = float(input('Digite o seu salário aqui: '))
if salario > 1320:
    aumento = salario + (salario * 10/100)
    print('Seu salário teve um aumento de 10% e será: {}'.format(aumento))
else:
    aumento_2 = salario + (salario * 15/100)
    print('Seu salário teve um aumento de 15% e será: {}'.format(aumento_2))

    