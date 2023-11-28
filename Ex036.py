print('\033[0;34mSeu empréstimo para a casa de seus sonhos é aqui DIXNGRA')
print()
valor_da_casa = float(input('\033[0;34;40MDigite o valor da casa:R$ '))
salario_do_comprador = float(input('Digite seu salário:R$ '))
anos_para_pagar = int(input('Em quantos anos deseja pagar? '))
valor_da_prestaçao = valor_da_casa / (anos_para_pagar * 12)
excedente = 0.3 * salario_do_comprador
if valor_da_prestaçao <= excedente:
    print('Para uma casa no valor de R${:.3f} as parcelas serão de R${:.2f}'.format(
        valor_da_casa, valor_da_prestaçao))
    print('\033[0;32;43mAPROVADO')
else:
    print('\033[0;31;40MRECUSADO')
