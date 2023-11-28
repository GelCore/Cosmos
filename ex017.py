from math import hypot
Hipotenusa = float(input('Digite o comprimento do cat oposto: '))
Hipotenusa_2 = float(input('Agora do adjacente: '))

hipotenusa_3 = hypot(Hipotenusa, Hipotenusa_2)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa_3))
