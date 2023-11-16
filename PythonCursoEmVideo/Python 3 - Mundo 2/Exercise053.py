# Crie um programa que leia uma frase qualquer a diga se ela é um palíndromo, desconsiderando os aspaços.

frase = str(input('Informe a frase que deseja saber se é um palíndromo: ')).strip().upper()

myTuple = frase.split()
x = "".join(myTuple)

#GUANABARA
inverso = ''

#inverso = x[::-1] # FATEAMENTO ':' Inicio ':' Fim '-1' De trás pra frente

# len(x) -1  = De trás pra frente, -1 pois se ele vai de 1 ao 20, na verdade seria de 0 ao 19.
for letra in range(len(x) - 1, -1, -1):
    inverso += x[letra]
print('O inverso de {} é {}' .format(x, inverso))
if inverso == x:
    print('Temos um palíndromo')
else:
    print('A FRASE DIGITADA NÃO É UM PALÍNDROMO')
    
    
#Thais 

for c in range(0, len(x)):
    if x[c] != x[(-c)-1]:
        ok = 'A FRASE DIGITADA NÃO É UM PALÍNDROMO'
    else:
        ok = 'Temos um palíndromo'
print(ok)