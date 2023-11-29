

# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

result = ''
count = 0

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')

while True:    
    print('=-'*15)

    number      = int(input('Diga um valor: '))
    parImpar    = str(input('Par ou ímpar? [P/I] ')).upper()
    comput      = randint(1,10)
    soma        = number + comput

    print('-'*30)
    if soma % 2 == 0:
        print(f'Você jogou {number} e o computador {comput}. Total de {soma} DEU PAR')
        result = "P"

    else:
        print(f'Você jogou {number} e o computador {comput}. Total de {soma} DEU ÍMPAR')
        result = "I"
    print('-'*30)

    if parImpar == result:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        count += 1
    else:
        print('Você PERDEU!')
        break

print('=-'*15)
print(f'GAME OVER! Você venceu {count} vezes.')

