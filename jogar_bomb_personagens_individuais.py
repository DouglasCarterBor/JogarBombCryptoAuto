import pyautogui
import time

tempoabrirchrome = 0.5 #0.5
tempoacessarbomb = 0.5 #0.5
tempoclicaremconectarcarteira = 10 #10
tempoclicaremassinar = 10 #10
tempoclicaremcacaaotesouro = 20 #20
tempomostrarherois = 1 #1
tempoclicaremherois = 1 #1
tempocolocarheroisparatrabalhar = 10 #10
tempocolocarheroiparatrabalhar = 10 #10
tempoclicaremfecharherois = 0.1 #0.1
tempobaixaraba = 1 #1
tempoesperarotrabalho = 500 #580
tempodearrasto = 0.4

def iniciar_bomb_ind():
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
    while i < 150:
        i += 1
        x += 1
        a += 1
        # 07 - MOSTRAR HERÓIS
        time.sleep(tempomostrarherois)
        pyautogui.moveTo(951, 785, tempodearrasto)
        pyautogui.click()
        # 08 - CLICAR EM HERÓIS
        time.sleep(tempoclicaremherois)
        pyautogui.moveTo(949, 762, tempodearrasto)
        pyautogui.click()
        # 09 - COLOCAR HERÓIS PARA TRABALHAR
        # 09.01 - COLOCAR HERÓI 01 PARA TRABALHAR
        while a == 1:
            time.sleep(tempocolocarheroiparatrabalhar)
            pyautogui.moveTo(848, 322, tempodearrasto)
            pyautogui.click()
            a += 1
        # 09.02 - COLOCAR HERÓI 02 PARA TRABALHAR
        while a == 3:
            time.sleep(tempocolocarheroiparatrabalhar)
            pyautogui.moveTo(848, 419, tempodearrasto)
            pyautogui.click()
            a += 1
        # 09.03 - COLOCAR HERÓI 03 PARA TRABALHAR
        while a == 5:
            time.sleep(tempocolocarheroiparatrabalhar)
            pyautogui.moveTo(847, 504, tempodearrasto)
            pyautogui.click()
            a += 1
        # 09.04 - COLOCAR HERÓI 04 PARA TRABALHAR
        while a == 7:
            time.sleep(tempocolocarheroiparatrabalhar)
            pyautogui.moveTo(846, 598, tempodearrasto)
            pyautogui.click()
            a += 1
        # 09.05 - COLOCAR HERÓI 05 PARA TRABALHAR
        while a == 9:
            time.sleep(tempocolocarheroiparatrabalhar)
            pyautogui.moveTo(846, 682, tempodearrasto)
            pyautogui.click()
            a += 1
        # 09.06 - COLOCAR HERÓI 06 PARA TRABALHAR
        while a == 11:
            time.sleep(tempocolocarheroiparatrabalhar)
            #ARRASTAR
            pyautogui.moveTo(584, 685, tempodearrasto)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423, tempodearrasto)
            pyautogui.mouseUp()
            #FIM DO ARRASTE
            pyautogui.moveTo(847, 504, tempodearrasto)
            pyautogui.click()
            a += 1
        # 09.07 - COLOCAR HERÓI 07 PARA TRABALHAR
        while a == 13:
            time.sleep(tempocolocarheroiparatrabalhar)
            # ARRASTAR
            pyautogui.moveTo(584, 685, tempodearrasto)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423, tempodearrasto)
            pyautogui.mouseUp()
            # FIM DO ARRASTE
            pyautogui.moveTo(846, 598, tempodearrasto)
            pyautogui.click()
            a += 1
        # 09.08 - COLOCAR HERÓI 08 PARA TRABALHAR
        while a == 15:
            time.sleep(tempocolocarheroiparatrabalhar)
            # ARRASTAR
            pyautogui.moveTo(584, 685, tempodearrasto)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423, tempodearrasto)
            pyautogui.mouseUp()
            # FIM DO ARRASTE
            pyautogui.moveTo(846, 682, tempodearrasto)
            pyautogui.click()
            a -= 15
        # 10 - FECHAR
        time.sleep(tempoclicaremfecharherois)
        pyautogui.moveTo(1025, 209, tempodearrasto)
        pyautogui.click()
        # 11 - BAIXAR ABA
        time.sleep(tempobaixaraba)
        pyautogui.moveTo(950, 679, tempodearrasto)
        pyautogui.click()
        # 12 - ESPERAR O TRABALHO
        time.sleep(tempoesperarotrabalho) # 580 = 9 M e 40 S
        while x == 6:
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
            x -= 6

    #pyautogui.alert("O código acabou de rodar, pode utilizar seu computador de novo!")
def finalizar_bomb():
    exit(iniciar_bomb_ind())

