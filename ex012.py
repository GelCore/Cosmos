preco = float(input('Digite o valor do produto: R$ '))

desconto = preco - ((preco/100) * 5)

print('O desconto que você terá neste valor é de: R$ {:.2f}'.format(desconto))


