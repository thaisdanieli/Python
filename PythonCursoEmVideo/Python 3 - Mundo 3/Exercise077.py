# DESAFIO 077 - Contando vogais em Tupla
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 
         'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for t in tupla:
    print(f'\nNa palavra {t.upper()} temos ', end = ' ')
    for letra in t:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')

