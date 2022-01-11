import pyautogui
import time


def iniciar_bomb_ind():
    # 01 - INÍCIO
    pyautogui.alert("Pressione Ok nesta mensagem e depois não toque no mouse ou no teclado! Obrigado!")
    # 02 - ABRIR O GOOGLE CHROME
    pyautogui.press('winleft')
    time.sleep(0.5)
    pyautogui.write('chrome')
    time.sleep(0.5)
    pyautogui.press('enter')
    # 03 - ACESSAR O BOMB
    time.sleep(0.5)
    pyautogui.write('https://app.bombcrypto.io/')
    pyautogui.press('enter')
    pyautogui.press('f11')
    # 04 - CLICAR EM CONECTAR CARTEIRA
    time.sleep(20)
    pyautogui.moveTo(954, 668)
    time.sleep(0.1)
    pyautogui.click()
    # 05 - ASSINAR
    time.sleep(10)
    pyautogui.moveTo(1782, 696)
    pyautogui.click()
    # 06 - CLICAR EM CAÇA TESOURO
    time.sleep(20)
    pyautogui.moveTo(959, 446)
    pyautogui.click()
    i = 0
    x = 0
    a = 0
    while i < 150:
        i += 1
        x += 1
        a += 1
        # 07 - MOSTRAR HERÓIS
        time.sleep(1)
        pyautogui.moveTo(951, 785)
        pyautogui.click()
        # 08 - CLICAR EM HERÓIS
        time.sleep(1)
        pyautogui.moveTo(949, 762)
        pyautogui.click()
        # 09 - COLOCAR HERÓIS PARA TRABALHAR
        # 09.01 - COLOCAR HERÓI 01 PARA TRABALHAR
        while a == 1:
            time.sleep(10)
            pyautogui.moveTo(848, 322)
            pyautogui.click()
            a += 1
        # 09.02 - COLOCAR HERÓI 02 PARA TRABALHAR
        while a == 3:
            time.sleep(10)
            pyautogui.moveTo(848, 419)
            pyautogui.click()
            a += 1
        # 09.03 - COLOCAR HERÓI 03 PARA TRABALHAR
        while a == 5:
            time.sleep(10)
            pyautogui.moveTo(847, 504)
            pyautogui.click()
            a += 1
        # 09.04 - COLOCAR HERÓI 04 PARA TRABALHAR
        while a == 7:
            time.sleep(10)
            pyautogui.moveTo(846, 598)
            pyautogui.click()
            a += 1
        # 09.05 - COLOCAR HERÓI 05 PARA TRABALHAR
        while a == 9:
            time.sleep(10)
            pyautogui.moveTo(846, 682)
            pyautogui.click()
            a += 1
        # 09.06 - COLOCAR HERÓI 06 PARA TRABALHAR
        while a == 11:
            time.sleep(10)
            #ARRASTAR
            pyautogui.moveTo(584, 685)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423)
            pyautogui.mouseUp()
            #FIM DO ARRASTE
            pyautogui.moveTo(847, 504)
            pyautogui.click()
            a += 1
        # 09.07 - COLOCAR HERÓI 07 PARA TRABALHAR
        while a == 13:
            time.sleep(10)
            # ARRASTAR
            pyautogui.moveTo(584, 685)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423)
            pyautogui.mouseUp()
            # FIM DO ARRASTE
            pyautogui.moveTo(846, 598)
            pyautogui.click()
            a += 1
        # 09.08 - COLOCAR HERÓI 08 PARA TRABALHAR
        while a == 15:
            time.sleep(10)
            # ARRASTAR
            pyautogui.moveTo(584, 685)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423)
            pyautogui.mouseUp()
            # FIM DO ARRASTE
            pyautogui.moveTo(846, 682)
            pyautogui.click()
            a -= 15
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
            x -= 6

    #pyautogui.alert("O código acabou de rodar, pode utilizar seu computador de novo!")
def finalizar_bomb():
    exit(iniciar_bomb_ind())

