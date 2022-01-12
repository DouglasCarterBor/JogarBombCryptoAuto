import pyautogui
import time

tempoabrirchrome = 0.5
tempoacessarbomb = 0.5
tempoclicaremconectarcarteira = 10
tempoclicaremassinar = 10
tempoclicaremcacaaotesouro = 20
tempomostrarherois = 1
tempoclicaremherois = 1
tempocolocarheroisparatrabalhar = 10

def iniciar_bomb():
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
    pyautogui.moveTo(954, 668)
    pyautogui.click()
    # 05 - ASSINAR
    time.sleep(tempoclicaremassinar)
    pyautogui.moveTo(1782, 696)
    pyautogui.click()
    # 06 - CLICAR EM CAÇA TESOURO
    time.sleep(tempoclicaremcacaaotesouro)
    pyautogui.moveTo(959, 446)
    pyautogui.click()
    i = 0
    x = 0
    while i < 150:
        i += 1
        x += 1
        # 07 - MOSTRAR HERÓIS
        time.sleep(tempomostrarherois)
        pyautogui.moveTo(951, 785)
        pyautogui.click()
        # 08 - CLICAR EM HERÓIS
        time.sleep(tempoclicaremherois)
        pyautogui.moveTo(949, 762)
        pyautogui.click()
        # 09 - COLOCAR HERÓIS PARA TRABALHAR
        time.sleep(tempocolocarheroisparatrabalhar)
        pyautogui.moveTo(848, 271)
        pyautogui.click()
        # 10 - FECHAR
        time.sleep(0.1)
        pyautogui.moveTo(1025, 209)
        pyautogui.click()
        # 11 - BAIXAR ABA
        time.sleep(1)
        pyautogui.moveTo(950, 679)
        pyautogui.click()
        # 12 - ESPERAR O TRABALHO
        time.sleep(580) # 580 = 9 M e 40 S
        while x == 6:
            x -= 6
            # 01 - ATUALIZAR A PÁGINA
            pyautogui.hotkey('crtl', 'f5')
            # 02 - CLICAR EM CONECTAR CARTEIRA
            time.sleep(10)
            pyautogui.moveTo(954, 668)
            pyautogui.click()
            # 03 - ASSINAR
            time.sleep(10)
            pyautogui.moveTo(1782, 696)
            pyautogui.click()
            # 04 - CLICAR EM CAÇA TESOURO
            time.sleep(20)
            pyautogui.moveTo(959, 446)
            pyautogui.click()

    #pyautogui.alert("O código acabou de rodar, pode utilizar seu computador de novo!")
def finalizar_bomb():
    exit(iniciar_bomb)

