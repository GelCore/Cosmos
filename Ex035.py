print('<>*25')
print('ANALISANDO TRIÂNGULOS')
print('<>*25')
a = float(input('Digite primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
if a+b > c and b+c > a and a+c > b:
    print('As retas informadas podem sim formar um triângulo')
else:
    print('O triângulo não pode ser formado')