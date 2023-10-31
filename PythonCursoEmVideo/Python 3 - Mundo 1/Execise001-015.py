#DESAFIO 1 - Aula 4
name = input('Qual é o seu nome?')
print('Olá ', name, '! Prazer em te conhecer!')
#print('É um prazer te conhecer {}!' .format(name))


#DESAFIO 2 - Aula 4
day     = input('Qual o dia do seu nascimento?')
month   = input('Qual o mês do seu nascimento?')
year    = input ('Qual o ano do seu nascimento?')
print('Você nasceu no dia', day, 'de',month, 'de', year, '. Correto?')

#DESAFIO 3 - Aula 4
number      = int(input('Primeiro número: '))
numberTwo   = int(input('Segundo número: '))
print(number + numberTwo)

#DESAFIO 4 - Aula 6
info = input('Digite algo: ')
print(info)
print('O tipo primitivo desse valor é',type(info))
print('É alphabetico?',             info.isalpha())
print('É um número? ',              info.isnumeric())
print('Está em maiusculo?' ,        info.isupper())
print('Está em minisculo?',         info.islower())
print('Está capitalizada? ',        info.istitle())    
print('Só tem espaços?',            info.isspace())

#DESAFIO 5 - Aula 7
number = int(input('Informe um número: '))
n1 = number-1
n2 = number + 1
print('Antecessor: {} e Sucessor: {}' .format(n1, n2))

#DESAFIO 6 - Aula 7
number = int(input('Informe um número: '))
n1 = number*2
n2 = number*3
n3 = number**(1/2)
print('O dobro do número {} é {} , o triplo é {} e a raiz quadrada é {}' .format(number,n1, n2, n3))

#DESAFIO 7 - Aula 7
media1 = float(input('Informe a primeira nota:'))
media2 = float(input('Informe a segunda nota: '))
number = (media1+media2)/2
print('A media do aluno é {}' .format(number))

# Exercício 8 - Conversor de Medidas
metros  = int(input('Metros: '))
cent    = metros * 100
mili    = metros * 1000
km      = metros / 1000
hm      = metros / 100
dcm     = metros * 10
print('Metros em centimetros: {}' .format(cent))
print('Metros em milimetros: {}' .format(mili)) 
print('Metros em KM: {}' .format(km))
print('Metros em Hectómetro: {}' .format(hm))
print('Metros em Decímetros: {}' .format(dcm))

# Exercício 9 - Tabuada
number = int(input('Informe um número: '))
i = 1
while i < 11:
    result = i*number
    print('{} x {} = {}' .format(number, i, result))
    i +=1

# Exercício 10 - Conversor de Moedas
saldo       = float(input('Informe seu saldo disponivel: R$'))
conversor   = saldo*3.27
print('Seu saldo em Dolares é {}' .format(conversor))

# Exercício 11 - Pintando Parede
largura     = float(input('Informe a largura da parede: '))
altura      = float(input('Informe a altura da parede: '))
metrosQ     = (largura*altura)/2
print('Área: ', metrosQ)
print('Quantidade de tinta necessária para pintar a parede: {} L' .format(metrosQ))

# Exercício 12 - Calculando Descontos
value       = float(input('Informe o valor do produto: R$'))
valueNew    = value-(value*0.05)
print('O Valor atualizado com 5% é R${}' .format(valueNew))

# Exercício 13 - Reajuste Salarial
cash    = float(input('Informe seu salario atual: R$'))
money   = cash + (cash*0.15)
print('Salário com novo reajuste de 15% é R$ {:.2f}' .format(money))

# Exercício 14 - Conversor de Temperaturas
celsius     = float(input('Informe a temperatura em °C: '))
fahrenheit  = (celsius*9/5)+32
print('A temperatura de {} corresponde a {:.1f}°F' .format(celsius, fahrenheit))

# Exercício 15 - Aluguel de Carros
dias    = int(input('Quantos dias alugados? '))
km      = int(input('Quantos KM rodados? '))
value   = (dias*60)+(km*0.15)
print('O total a pagar é de R$ {}' .format(value))
