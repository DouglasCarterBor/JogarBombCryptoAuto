import pyautogui
import time


def iniciar_bomb():
    # 01 - INÍCIO
    pyautogui.alert("Pressione Ok nesta mensagem e depois não toque no mouse ou no teclado! Obrigado!")
    # 02 - ABRIR O GOOGLE CHROME
    pyautogui.press('winleft')
    time.sleep(0.3)
    pyautogui.write('chrome')
    pyautogui.press('enter')
    # 03 - ACESSAR O BOMB
    time.sleep(0.3)
    pyautogui.write('https://app.bombcrypto.io/')
    pyautogui.press('enter')
    pyautogui.press('f11')
    # 04 - CLICAR EM CONECTAR CARTEIRA
    time.sleep(8)
    pyautogui.moveTo(954, 668)
    time.sleep(0.1)
    pyautogui.click()
    # 05 - ASSINAR
    time.sleep(8)
    pyautogui.moveTo(1782, 696)
    pyautogui.click()
    # 06 - CLICAR EM CAÇA TESOURO
    time.sleep(20)
    pyautogui.moveTo(959, 446)
    pyautogui.click()
    i = 0
    x = 0
    while i < 150:
        i += 1
        x += 1
        # 07 - MOSTRAR HERÓIS
        time.sleep(1)
        pyautogui.moveTo(951, 785)
        pyautogui.click()
        # 08 - CLICAR EM HERÓIS
        time.sleep(1)
        pyautogui.moveTo(949, 762)
        pyautogui.click()
        # 09 - COLOCAR HERÓIS PARA TRABALHAR
        time.sleep(1)
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
        time.sleep(500)
        while x == 6 or x == 13 or x == 20 or x == 30 or x == 40 or x == 50:
            x += 1
            # 01 - ATUALIZAR A PÁGINA
            pyautogui.hotkey('crtl', 'f5')
            time.sleep(8)
            # 02 - CLICAR EM CONECTAR CARTEIRA
            time.sleep(8)
            pyautogui.moveTo(990, 789)
            time.sleep(0.1)
            pyautogui.click()
            # 03 - ASSINAR
            time.sleep(5)
            pyautogui.moveTo(1806, 696)
            pyautogui.click()
            # 04 - CLICAR EM CAÇA TESOURO
            time.sleep(12)
            pyautogui.moveTo(981, 552)
            pyautogui.click()

    #pyautogui.alert("O código acabou de rodar, pode utilizar seu computador de novo!")
def finalizar_bomb():
    exit(iniciar_bomb)

