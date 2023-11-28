celsius = int(input('Digite a temperatura ºC: '))
fah = int(input('Digite a temperatura em ºF: '))

fahrenheit_conversor = (celsius * 1.8) + 32
celsius_conversor = (5/9) * fah - 32

print('A medida da temperatura em fahrenheit é: {:.0f}ºF \n A medida em graus celsius é: {:.0f}ºC'.format(fahrenheit_conversor, celsius_conversor))
