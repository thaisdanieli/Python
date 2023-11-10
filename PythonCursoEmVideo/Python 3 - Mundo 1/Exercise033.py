# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

import random

number1 = int(input('Informe o primeiro número: '))
number2 = int(input('Informe o segundo número: '))
number3 = int(input('Informe o terceiro número: '))

if number1 > number2 and number1 > number3:
    maior = number1 
    menor = number2 if number2 < number3 else number3       
elif number2 > number3:
    menor = number1
    maior = number2
else:
    maior = number3
    menor = number2 if number2 < number1 else number1

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')

