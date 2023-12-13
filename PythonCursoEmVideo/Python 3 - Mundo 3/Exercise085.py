# DESAFIO 085 - Listas com pares e ímpares
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

listaPrinc = [[], []]
j = 0

for c in range(1,8):
    num = int(input(f'Digite o {c}o. valor: '))
    if num % 2 == 0:
        listaPrinc[0].append(num)       
    else:
        listaPrinc[1].append(num)

listaPrinc[0].sort()
listaPrinc[1].sort()
print(f'Os valores pares digitados foram: {listaPrinc[0]}')
print(f'Os valores ímpares digitados foram: {listaPrinc[1]}')