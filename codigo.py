import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(1)
pyautogui.click(x=509, y=917)

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

pyautogui.click(x=380, y=473)
pyautogui.write('eduardosipiovezani@gmail.com')
pyautogui.press('tab')
pyautogui.write('edu12345')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)

import pandas 

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=702, y=320)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if obs is not "nan":
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    pyautogui.press('enter')

    pyautogui.scroll(5000)






#Uma forma de base para a logica de programação é o passo a passo de como fariamos essa tarefa se dependensse da nossa propria ação
#Apos isso apenas traduzimos nossas ações para  a linguagem que desejamos. Então é bom fazer literalmente o passo a passo que fariamos para fazer determinada ação.
#E trabalahr um passo de cada vez.