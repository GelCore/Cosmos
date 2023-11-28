'# CALCULANDO A MÉDIA ENTRE DUAS NOTAS DE UM ALUNO #'

('# Foram criadas 3 variáveis nota1 recebendo a primeira nota e nota2 a segunda nota.')
('Por sequinte a variável media recebeu uma equação simples para achar a média entre as duas primeiras. #')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2) /2

print('Sua média é: {:.1}'.format(media))