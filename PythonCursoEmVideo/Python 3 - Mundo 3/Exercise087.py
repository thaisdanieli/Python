# DESAFIO 087 - Mais sobre Matriz em Python
# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz = [[], [], []]
somaPar = somaCol = 0

for c in range(0,3):
    for j in range(0,3):
        matriz[c].append(int(input(f'Digite um valor para [{c}, {j}]: ')))
        if matriz[c][j] % 2 == 0:
            somaPar += matriz[c][j]
        if j == 2:
            somaCol += matriz[c][j]
print('-='*20)
for c in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[c][j]}]', end='')
    print()

print('-='*20)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaCol}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

 