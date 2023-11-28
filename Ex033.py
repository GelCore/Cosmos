# 3 entradas para ler os valores fornecidos.
numero_1 = int(input('Digite um valor: '))
numero_2 = int(input('Digite o segundo valor: '))
numero_3 = int(input('Digite o último valor: '))
# São criadas 2 variáveis armazenando apenas o primeiro valor. Inicío dizendo que a variável: numero_1 é maior e menor.
# Isso me permite que apenas com a cadeia simples de IF eu vá trocando e embaralhando quem vai ser ou não o menor e maior.
maior = numero_1
menor = numero_1
#Cadeia simples de condições, apenas IF. Se numero_2 for > que o numero_1 então o MAIOR passa a ser a variável numero_2...
if  numero_2 > maior:
    maior = numero_2
if numero_3 > maior:
    maior = numero_3
if numero_2 < menor:
    menor = numero_2
if numero_3 < menor:
    menor = numero_3
#Apenas jogando na máscara {} as variáveis com seus "IFS".
print('O maior número é: {} e o menor é: {}'.format(maior, menor))




