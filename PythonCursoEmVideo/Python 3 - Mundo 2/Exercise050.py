# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidera-o.

num = 0
tot = 0

for c in range(1,7):
    number = int(input('Informe o {}º número: ' .format(c)))
    if number % 2 == 0:
        tot += number
        num += 1


print('Você informou {} pares e a soma dos números é {}' .format(num, tot))
