print('<><><><><><><><><><><><><><>')
print('ANALISANDO TRIÂNGULOS')
print('<><><><><><><><><><><><><><>')
lado_a = float(input('Digite primeiro lado do triângulo: '))
lado_b = float(input('Digite segundo lado do triângulo: '))
lado_c = float(input('Digite terceiro lado do triângulo: '))
if lado_a+lado_b > lado_c and lado_b+lado_c > lado_a and lado_a+lado_c > lado_b:
    if lado_a == lado_b == lado_c:
        print('As retas podem formar um triângulo EQUILÁTERO')
    elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
        print('As retas podem formar um triângulo ISÓSCELES')
    elif lado_a != lado_b and lado_b != lado_c and lado_c != lado_a:
        print('As retas podem formar um triângulo ESCALENO')
    else:
        print('Impossível montar um triângulo com esses valores.')
