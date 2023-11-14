# DESAFIO 048 - Soma ímpares múltiplos de três
# Faça um programa que calcule a soma entre todos os números impares que SÃO múltiplos de três e que se encontram no intervalo de 1 até 500.

tot = 0
number = 0

for c in range(1,501,2):
    if c % 3 == 0:
        tot += c 
        number += 1
print('A soma total dos números {} impares é {}' .format(number, tot))   
