# Exercício Python #065 - Maior e Menor valores
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
number = cont = med = Numbermax = Numbermin =  0

while resp != "N":
    number = int(input('Digite um número: '))
    cont += 1
    med += number
    if cont == 1:
        maior = menor = number
    else: 
        if number > Numbermax:
            Numbermax = number
        if number < Numbermin:
            Numbermin = number
    resp = str(input('Quer continuar? ')).strip().upper()[0] # O [0] quer dizer 'Considerar apenas a primeira letra'

med = med/cont

print('Você digitou {} números e a média foi {:.2f}' .format(cont, med))
print('O maior valor foi {} e o menor foi {}' .format(Numbermax, Numbermin))