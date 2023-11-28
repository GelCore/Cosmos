leia_um_numero = int(input('Digite um número e direi se ele par ou ímpar: '))

#Para saber se um número é par ou ímpar dividi-os por 2 e pegue o resto desta divisão se o resto for 0 = par se 1 = ímpar
par = leia_um_numero % 2 
impar = leia_um_numero % 2
#Condicionais sendo PAR == 0 ELSE para o contrário.
if par == 0:
    print('O número que você digitou é par')
else:
    print('O número digitado é impar')
    