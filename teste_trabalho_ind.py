import pyautogui
import time

tempoabrirchrome = 0.5 #0.5
tempoacessarbomb = 0.5 #0.5
tempoclicaremconectarcarteira = 10 #10
tempoclicaremassinar = 10 #10
tempoclicaremcacaaotesouro = 20 #20
tempomostrarherois = 1 #1
tempoclicaremherois = 1 #1
tempocolocarheroisparatrabalhar = 2 #10
tempocolocarheroiparatrabalhar = 2 #10
tempoclicaremfecharherois = 0.1 #0.1
tempobaixaraba = 1 #1
tempoesperarotrabalho = 10 #580

def testetrabalho():
    i = 0
    x = 0
    a = 0
    while i < 150:
        i += 1
        x += 1
        a += 1
        # 07 - MOSTRAR HERÓIS
        #time.sleep(tempomostrarherois)
        #pyautogui.moveTo(951, 785)
        #pyautogui.click()
        # 08 - CLICAR EM HERÓIS
        #time.sleep(tempoclicaremherois)
        #pyautogui.moveTo(949, 762)
        #pyautogui.click()
        # 09 - COLOCAR HERÓIS PARA TRABALHAR
        # 09.01 - COLOCAR HERÓI 01 PARA TRABALHAR
        # 09.06 - COLOCAR HERÓI 06 PARA TRABALHAR
        while a == 1:
            time.sleep(1.5)
            # ARRASTAR
            pyautogui.moveTo(584, 685)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423, 0.4)
            pyautogui.mouseUp()
            # FIM DO ARRASTE
            pyautogui.moveTo(847, 504)
            pyautogui.click()
            a += 1
        # 09.07 - COLOCAR HERÓI 07 PARA TRABALHAR
        while a == 2:
            time.sleep(1.5)
            # ARRASTAR
            pyautogui.moveTo(584, 685)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423, 0.4)
            pyautogui.mouseUp()
            # FIM DO ARRASTE
            pyautogui.moveTo(846, 598)
            pyautogui.click()
            a += 1
        # 09.08 - COLOCAR HERÓI 08 PARA TRABALHAR
        while a == 3:
            time.sleep(1.5)
            # ARRASTAR
            pyautogui.moveTo(584, 685)
            pyautogui.mouseDown()
            pyautogui.moveTo(578, 423, 0.4)
            pyautogui.mouseUp()
            # FIM DO ARRASTE
            pyautogui.moveTo(846, 682)
            pyautogui.click()
            a = 0
        # 10 - FECHAR
        #time.sleep(tempoclicaremfecharherois)
        #pyautogui.moveTo(1025, 209)
        #pyautogui.click()
        # 11 - BAIXAR ABA
        #time.sleep(tempobaixaraba)
        #pyautogui.moveTo(950, 679)
        #pyautogui.click()
        # 12 - ESPERAR O TRABALHO
        #time.sleep(tempoesperarotrabalho)