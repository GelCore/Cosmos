print('CONFEDERAÇÃO DE ATLETAS')
print()
idade = int(input('Digite sua idade para sabermos sua CATEGORIA: '))
lista = [9, 14, 19, 20]
if idade == 9:
    print('Você tem {} de idade e sua categoria é a MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} de idade e sua categoria é a INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} de idade e sua categoria é a JUNIOR.'.format(idade))
elif idade == 20:
    print('Você tem {} de idade e sua categoria é a SÊNIOR'.format(idade))
elif idade > 20:
    print('Você tem {} de idade e sua categoria é a MASTER.'.format(idade))
else:
    print('Você precisa estar dentro das seguintes lista de idade: {} ou acima de 20 anos.'.format(lista))
