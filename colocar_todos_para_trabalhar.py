import pyautogui
import time

tempoabrirchrome = 0.5 #0.5
tempoacessarbomb = 0.5 #0.5
tempoclicaremconectarcarteira = 10 #10
tempoclicaremassinar = 10 #10
tempoclicaremcacaaotesouro = 20 #20
tempomostrarherois = 1 #1
tempomostrarherois2 = 0.5 #1
tempoclicaremherois = 1 #1
tempoclicaremherois2 = 0.2 #1
tempocolocarheroisparatrabalhar = 10 #10
tempocolocarheroiparatrabalhar = 10 #10
tempocolocarheroiparatrabalhar2 = 0.2 #10
tempoclicaremfecharherois = 0.2 #0.1
tempobaixaraba = 0.2 #1
tempoesperarotrabalho = 490 #580
tempoesperarotrabalho2 = 30 #580
tempodearrasto = 0.1

def iniciar_bomb_todos():
    # 01 - INÍCIO
    pyautogui.alert("Pressione Ok nesta mensagem e depois não toque no mouse ou no teclado! Obrigado!")
    # 02 - ABRIR O GOOGLE CHROME
    pyautogui.press('winleft')
    time.sleep(tempoabrirchrome)
    pyautogui.write('chrome')
    time.sleep(tempoabrirchrome)
    pyautogui.press('enter')
    # 03 - ACESSAR O BOMB
    time.sleep(tempoacessarbomb)
    pyautogui.write('https://app.bombcrypto.io/')
    pyautogui.press('enter')
    pyautogui.press('f11')
    # 04 - CLICAR EM CONECTAR CARTEIRA
    time.sleep(tempoclicaremconectarcarteira)
    pyautogui.moveTo(954, 668, tempodearrasto)
    time.sleep(0.1)
    pyautogui.click()
    # 05 - ASSINAR
    time.sleep(tempoclicaremassinar)
    pyautogui.moveTo(1782, 696, tempodearrasto)
    pyautogui.click()
    # 06 - CLICAR EM CAÇA TESOURO
    time.sleep(tempoclicaremcacaaotesouro)
    pyautogui.moveTo(959, 446, tempodearrasto)
    pyautogui.click()
    i = 0
    x = 0
    a = 0
    while i < 500000:
        i += 1
        x += 1
        a += 1
        # 07 - MOSTRAR HERÓIS
        time.sleep(tempomostrarherois2)
        pyautogui.moveTo(951, 785, tempodearrasto)
        pyautogui.click()
        # 08 - CLICAR EM HERÓIS
        time.sleep(tempoclicaremherois2)
        pyautogui.moveTo(949, 762, tempodearrasto)
        pyautogui.click()
        # 09 - COLOCAR HERÓIS PARA TRABALHAR
        while a == 1:
            time.sleep(tempocolocarheroiparatrabalhar2)
            pyautogui.moveTo(853, 270)
            pyautogui.click()
            a += 1
        # 10 - FECHAR
        time.sleep(tempoclicaremfecharherois)
        pyautogui.moveTo(1025, 209, tempodearrasto)
        pyautogui.click()
        # 11 - BAIXAR ABA
        time.sleep(tempobaixaraba)
        pyautogui.moveTo(950, 679, tempodearrasto)
        pyautogui.click()
        # 12 - ESPERAR O TRABALHO
        time.sleep(tempoesperarotrabalho2) # 580 = 9 M e 40 S
        a = 0
        while x == 300:
            # 01 - ATUALIZAR A PÁGINA
            pyautogui.hotkey('crtl', 'f5')
            # 02 - CLICAR EM CONECTAR CARTEIRA
            time.sleep(tempoclicaremconectarcarteira)
            pyautogui.moveTo(954, 668, tempodearrasto)
            pyautogui.click()
            # 03 - ASSINAR
            time.sleep(tempoclicaremassinar)
            pyautogui.moveTo(1782, 696, tempodearrasto)
            pyautogui.click()
            # 04 - CLICAR EM CAÇA TESOURO
            time.sleep(tempoclicaremcacaaotesouro)
            pyautogui.moveTo(959, 446, tempodearrasto)
            pyautogui.click()
            x -= 300
    #pyautogui.alert("O código acabou de rodar, pode utilizar seu computador de novo!")
def finalizar_bomb():
    exit(iniciar_bomb_todos())

