import pyautogui 
from time import sleep

# - Passos manuais para realizar este process?
# 1 - Clicar e digitar meu usuário
pyautogui.click(361,371,duration=1)
pyautogui.write('thaisdanieli')

# 2 - Clicar e digitar minha senha
pyautogui.click(356,398,duration=1)
pyautogui.write('1234')

# 3 - Clicar em "Entrar"
pyautogui.click(252,425,duration=1)

# Abrir arquivo > Iterar cada arquivo > # 4 - Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto     = linha.split(',')[0] # Quando ele localizar uma virgula, ele irá separar como se fosse "um campo" que ele deve separar a informação
        quantidade  = linha.split(',')[1] 
        preco       = linha.split(',')[2] 

            # 	1 - Clicar e digitar produto
        pyautogui.click(204,360,duration=0.5)
        pyautogui.write(produto)
            # 	2 - Clicar e digitar quantidade
        pyautogui.click(204,388,duration=0.5)
        pyautogui.write(quantidade)
            # 	3 - Clicar e digitar preço
        pyautogui.click(202,414,duration=0.5)
        pyautogui.write(preco)
            # 	4 - Clicar em registrar
        pyautogui.click(104,570,duration=1)