# DESAFIO 070 - Estatísticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

fim = ' FIM DO PROGRAMA '
inicio = 'LOJA SUPER BARATÃO'
quant = valueTot = 0
valueProduct = 10

while True:
    print('-'*40)
    print(f'{inicio:^40}')
    print('-'*40)

    name     = str(input('Nome do Produto: '))
    value    = float(input('Preço: R$'))

    valueTot += value

    if value < valueProduct:
        valueProduct = value
        nameProduct = name

    if value > 1000:
        quant += 1

    break

print(f'{fim:-^40}')

print(f'O total da compra foi R${valueTot}')
print(f'Temos {quant} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nameProduct} que custa R${valueProduct:.2f}')