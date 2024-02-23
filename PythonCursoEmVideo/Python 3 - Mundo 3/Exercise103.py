def ficha(nome='<desconhecido>', gol=0):
    print('-'*30)
    print(f'O jogador {nome} fez {gol} no campeonato.')

# PROGRAMA PRINCIPAL

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

# Verifica se a variável gols contém apenas caracteres numéricos (dígitos) e se não está vazia. 
# Essa condição retorna True se a string gols for composta apenas por números e False se houver pelo menos um caractere que não seja um número ou se a string estiver vazia.
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome,gols)
