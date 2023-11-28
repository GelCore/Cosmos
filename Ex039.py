from datetime import date
print('\033[1;32mALISTAMENTO AQUI')
print()
ano_atual = date.today().year
# input para armazenar a data de nascimento
ano_nascimento = int(input('Dgitie seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
TempoFalta = 18 - idade
TempoPassou = idade - 18
if idade == 18:
    print('Você tem {} anos e já se aliste-se JÁ.'.format(idade))
elif idade < 18:
    print('Você ainda não possui a idade você tem {}'.format(idade))
    print('Faltam {} anos para você se alistar'.format(TempoFalta))
elif idade > 18:
    print('Você passou do prazo sua idade é de {}'.format(idade))
    print('Deveria ter se alistado há {} anos'.format(TempoPassou))
