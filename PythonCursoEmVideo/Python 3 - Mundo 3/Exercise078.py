# DESAFIO 078 - Maior e Menor valores na Lista
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
lista = []
mai = 0
men = 0

for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print('-='*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {mai} nas posições ', end = ' ')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end = ' ')
print()   
print(f'O menor valor digitado foi {men} nas posições ', end = ' ')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end = ' ') 
print()







