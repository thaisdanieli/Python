# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

number = int(input('Informe um número para a tabuada: '))

print('MULTIPLICAÇÃO')
for c in range(1, 11):
    result = number*c
    print('{} x {} = {}' .format(number, c , result))
    
print('')

print('DIVISÃO')
for c in range(1 ,11):
    result = number / c
    print('{} / {} = {:.3f}' .format(number, c, result))

print('')

print('SUBTRAÇÃO')
for c in range(1, 11):
    result = number - c
    print('{} - {} = {}' .format(number, c, result))

print('')

print('SOMA')
for c in range(1, 11):
    result = number + c
    print('{} + {} = {}' .format(number, c, result))