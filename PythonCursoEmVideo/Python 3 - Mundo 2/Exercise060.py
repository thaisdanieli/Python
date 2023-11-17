# DESAFIO 060 - Cálculo do Fatorial
# Faça um programa que leia um número qualquer e mostre o seu fatorial.

number = c = int(input('Digite um número para calcular seu Fatorial: '))
value = 1

print('Calculando {}! = ' .format(number), end = '')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end = '')
    value *= c
    c-= 1
print('{}' .format(value))