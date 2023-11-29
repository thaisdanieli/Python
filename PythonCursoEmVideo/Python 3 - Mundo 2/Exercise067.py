
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True:
    print('='*40)
    number = int(input('Quer ver a tabuada de qual valor? '))
    print('='*40)
    if number < 0:
        break
    for c in range(11):
        print(f'{number} x {c} = {number*c}')

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

