# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Informe um número:'))

if (number % 2) == 0:
    print('Este número {} é PAR' .format(number))
else:
    print('Este número {} é ÍMPAR' .format(number))
