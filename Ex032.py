from datetime import date
ano = int(input('Digite um ano e direi se ele é bissexto ou digite 0 pra saber se o ano atual é Bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} não é BISSEXTO'.format(ano))

