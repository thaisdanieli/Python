# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


num = tuple(int(input(f'Digite o {c+1}º número: ')) for c in range(5))
print(f'Você digitou os valores {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1}ª posição' if 3 in num else 'Não foi digitado valor 3')
print('Os valores pares digitados foram:')
print({x for x in num if x % 2 == 0})