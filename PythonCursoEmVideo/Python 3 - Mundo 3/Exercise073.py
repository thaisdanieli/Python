# DESAFIO 073 - Tuplas com Times de Futebol
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

times = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")
print('-=' * 30)
print(f'Lista de times: {times}')
print('-=' * 30)

for t in times:
    print(t)

print('-='*30)

print(f'os 5 primeiros são {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')