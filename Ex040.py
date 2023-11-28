print('\033[0;34mCALCULANDO SUA MÉDIA')
print()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('Sua média foi igual a: {} REPROVADO'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi igual a: {} RECUPERAÇÃO'.format(media))
elif media >= 7.0:
    print('Média {} APROVADO'.format(media))
