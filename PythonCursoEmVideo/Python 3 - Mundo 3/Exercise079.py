# DESAFIO 079 - Valores únicos em uma Lista
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

numeros =[]

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    yesNo =  str(input('Quer continuar? [S/N] '))[0]
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros}')