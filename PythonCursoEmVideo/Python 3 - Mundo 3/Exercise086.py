# DESAFIO 086 - Matriz em Python
#  Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
j = h = 0

for j in range(0,3):
    for h in range(0,3):
        matriz[j].append(int(input(f'Digite um valor para [{j}, {h}]: ')))
j=0
for c in range(0,3):
    while j < len(matriz[c]):
        print(f'[ {matriz[c][j]} ]', end = ' ')
        j+=1
    print()
    j = 0

# GUANABARA
matriz = [[0,0,0], [0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] =  int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end ='')
    print()
