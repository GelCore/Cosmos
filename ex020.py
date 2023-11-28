import random

nome1 = str(input('Digite primeiro nome: '))
nome2 = str(input('Digite próximo aluno: '))
nome3 = str(input('Digite aluno 3: '))
nome4 = str(input('Digite aluno 4: '))

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print(lista)
