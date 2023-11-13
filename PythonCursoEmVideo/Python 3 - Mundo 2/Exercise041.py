# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 25 anos: SENIOR
# -Acima: MASTER

from datetime import datetime

year = int(input('Informe o ano de nascimento do atleta: '))

age = datetime.now().year -  year

if age <= 9:
    print('MIRIM')
elif age <= 14:
    print('INFANTIL')
elif age <= 19:
    print('JUNIOR')
elif age <= 25:
    print('SENIOR')
else: 
    print('MASTER')
