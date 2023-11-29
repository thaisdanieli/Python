# Exercício Python #064 - Tratando vários valores v1.0
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = numbers = cont = 0
numbers = int(input('Informe um número de 1 a 999: '))

while numbers != 999:
    soma += numbers   
    cont += 1
    numbers = int(input('Informe um número de 1 a 999: '))

print('A soma dos números informados é: {}' .format(soma))

