from time import sleep
from random import randint
print('{:=^40}'.format('\033[0;35;35mJOKENPO!!!'))
print()
# itens[0] = "pedra", itens[1] = "papel", itens[2] = "tesoura"
itens = ('PEDRA', 'PAPEL', 'TESOURA')
escolha_do_computador = randint(0, 2)
print('ESCOLHA SUA OPÇÃO')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha_do_jogador = int(input('Faça sua jogada: '))
print('JO')
sleep(2)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('<>' * 15)
print('Jogador jogou: {}'.format(itens[escolha_do_jogador]))
print('Computador jogou: {}'.format(itens[escolha_do_computador]))
print('<>' * 15)
if escolha_do_computador == 0:  # Computador jogou PEDRA
    if escolha_do_jogador == 0:
        print('EMPATE')
    elif escolha_do_jogador == 1:
        print('Jogador Venceu')
    elif escolha_do_jogador == 2:
        print('Jogador Perdeu')
    else:
        print('JOGADA INVÁLIDA')
elif escolha_do_computador == 1:  # Computador jogou PAPEL
    if escolha_do_jogador == 0:
        print('Computador Venceu está rodada')
    elif escolha_do_jogador == 1:
        print('EMPATE')
    elif escolha_do_jogador == 2:
        print('Jogador Venceu')
    else:
        print('JOGADA INVÁLIDA')
elif escolha_do_computador == 2:
    if escolha_do_jogador == 0:
        print('Jogador Venceu')
    elif escolha_do_jogador == 1:
        print('Computador Venceu')
    elif escolha_do_jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
