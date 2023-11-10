# EXERCISE 022

name = str(input('Informe seu nome completo: '))

print(name.upper())
print(name.lower())

list = name.split()
list = "".join(list)
print(len(list))
print(list)

list = name.split()
print(len(list[0]))

# OUTRA FORMA MELHOR DE SE UTILIZAR

print(f"Seu nome em Maiusculo é: {name.upper()}")
print(f"Seu nome em Minusculo é: {name.lower()}")

print(f"Seu nome tem {len(''.join(name.split()))} caracteres")
print(f"Seu primeiro nome é {name.split()[0]} e ele tem {len(name.split()[0])} letras")

# EXERCISE 023

num = int(input('Informe um número: '))
u = num // 1 % 10 # Divisão inteira por 1
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analizando o número {}' .format(num))
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar:{}' .format(m))

# EXERCISE 024

state = str(input('Informe o nome da Cidade: '))

trueFalse = state.split()
state = trueFalse[0]
print('Santo' in state.title())

# OR
print(f"A cidade {state} começa com o nome Santo? {state.split()[0].upper() == 'SANTO'}")

# EXERCISE 025

name = str(input('Informe o nome: '))
print('SILVA' in name.upper().strip())

# EXERCISE 026
# Faça um programa que leia uma frase e mostre
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira.
# Em que posição ela aparece a última vez.

words = str(input('Informe a frase: '))

print(f'A letra "A" aparece {words.upper().count('A')} vezes na frase')
print(f'A letra "A" aparece a primeira vez na posição {words.upper().find('A')}')
print(f'A última letra "A" aparece na posição {words.upper().rfind('A')}')

# EXERCISE 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro a o último nome separadamente.

words = str(input('Informe o nome completo: '))
print(f'Primeira palavra: {words.split()[0]}')
print(f'última palavra: {words.split()[-1]}')

