valor_em_metros = float(input('Digite a quantidade em metros: '))

dm = valor_em_metros * 10
cm = valor_em_metros * 100
mm = valor_em_metros * 1000
dam = valor_em_metros / 10
hm = valor_em_metros / 100
km = valor_em_metros / 1000

print('O valor em decimetro: {:.0f}\n Centrímetro: {:.0f} \n Milímetros: {:.0f} \n Decâmetros: {} \n Hecâmetro: {} \n Kilômetros: {}'.format(dm, cm, mm, dam, hm, km))


