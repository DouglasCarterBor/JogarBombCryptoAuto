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
    pyautogui.moveTo(990, 789)
    time.sleep(0.1)
    pyautogui.click()
    # 05 - ASSINAR
    time.sleep(8)
    pyautogui.moveTo(1806, 696)
    pyautogui.click()
    # 06 - CLICAR EM CAÇA TESOURO
    time.sleep(20)
    pyautogui.moveTo(981, 552)
    pyautogui.click()
    i = 0
    x = 0
    while i < 150:
        i += 1
        x += 1
        # 07 - MOSTRAR HERÓIS
        time.sleep(1)
        pyautogui.moveTo(974, 894)
        pyautogui.click()
        # 08 - CLICAR EM HERÓIS
        time.sleep(1)
        pyautogui.moveTo(970, 864)
        pyautogui.click()
        # 09 - COLOCAR 01 PARA TRABALHAR
        time.sleep(10)
        pyautogui.moveTo(871, 395)
        pyautogui.click()
        # 10 - COLOCAR 02 PARA TRABALHAR
        time.sleep(1)
        pyautogui.moveTo(865, 490)
        pyautogui.click()
        # 11 - COLOCAR 03 PARA TRABALHAR
        time.sleep(1)
        pyautogui.moveTo(871, 580)
        pyautogui.click()
        # 12 - FECHAR
        time.sleep(0.1)
        pyautogui.moveTo(1046, 312)
        pyautogui.click()
        # 13 - BAIXAR ABA
        time.sleep(1)
        pyautogui.moveTo(974, 755)
        pyautogui.click()
        # 14 - ESPERAR O TRABALHO
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

    pyautogui.alert("O código acabou de rodar, pode utilizar seu computador de novo!")

