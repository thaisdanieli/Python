# Exercicio 016
import math
import random

ret = random.randint(1,10)
number = math.trunc(ret)
print('Valor gerado pela função random: {:.3f} valor arredondado pela função trunc: {}' .format(ret, number))


# Exercicio 017
import math

a = float(input('Informe o valor do cateto oposto: '))
b = float(input('Informe o valor do cateto adjacente: '))
number = (math.pow(a,2))+(math.pow(b,2))
number = float(math.sqrt(number))

print('A medida da hipotenusa é: {:.2f}' .format(number))

# Outra possibilidade MAIS FÁCIL 
hipot = math.hypot(a, b)
print('A hipotenusa vai medir: {:.2f}' .format(number))

# Exercise 018
import math
angulo = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}' .format(angulo, seno)) 
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSEENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}' .format(angulo, tangente))

# Exercise 019
import random

names = input('Informe o primeiro nome:').split(",")

print ('O aluno escolhido foi {}' .format(random.choice(names)))

#OPÇÃP 2 do Exercicio 019

name1 = input('Informe o primeiro nome:').split(",")
name2 = input('Informe o segundo nome:')
name3 = input('Informe o terceiro nome:')
name4 = input('Informe o quarto nome:')

list_name = [name1, name2, name3, name4]
joke = random.choice(list_name)
print ('O aluno escolhido foi {}' .format(random.choice(name1)))

# EXERCISE 020
import random

name1 = str(input('Informe o primeiro nome:'))
name2 = str(input('Informe o segundo nome:'))
name3 = str(input('Informe o terceiro nome:'))
name4 = str(input('Informe o quarto nome:'))

listOf = [name1, name2, name3, name4]
random.shuffle(listOf)

print('A ordem será:')
print(listOf)

# EXERCISE 021
import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
