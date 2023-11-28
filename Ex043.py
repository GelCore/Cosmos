print('VEJA SEU IMC')
print()
peso = float(input('Digite aqui seu peso em kg: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Seu IMC é de: {:.2f} você está abaixo do peso ideal.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de: {:.2f} você está dentro do peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é de {:.2f} você está com Sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é de {:.2f} você está obeso'.format())
elif imc > 40:
    print('Você tem obesidade mórbida')
