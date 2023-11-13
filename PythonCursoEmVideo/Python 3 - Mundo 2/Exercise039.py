# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço Militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime
sexo = int(input('Informe o sexo: [1] Feminino [2] Masculino: '))

if sexo == 2:
    year = int(input('Informe o ano do seu nascimento:'))
    age  = datetime.now().year - year

    if age < 18:
        print('Quem nasceu em {} tem {} anos em {}' .format(year, age, datetime.now().year))
        print('Ainda faltam {} anos para o alistamento.' .format(18-age))
        print('Seu alistamento será em {}' .format(18-age+datetime.now().year))
    elif age == 18:
        print('Quem nasceu em {} tem {} anos em {}' .format(year, age, datetime.now().year))
        print('Você tem que se alistar IMEDIATAMENTE!')
    else:    
        print('Quem nasceu em {} tem {} anos em {}' .format(year, age, datetime.now().year))
        print('Você já deveria ter se alistado há {} anos.' .format(age-18))
        print('Seu alistamento foi em {}' .format(datetime.now().year-(age-18)))
else:
    print('Alistamento FEMININO não obrigatório!')
