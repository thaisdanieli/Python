# Faça um programa que leia um número inteiro a diga se ele é ou não um número primo.

number = int(input('Informe um número: '))
tot = 0

for c in range(1, number + 1):
    if number % c == 0:
        print('\033[33m', end ='')
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{} ' .format(c), end = '')

print('\n\033[mO número {} foi divisível {} vezes' .format(number, tot))

if tot == 2:
    print('E por isso ele É PRIMO')

else: 
    print('E por isso ele NÃO É primo!')        