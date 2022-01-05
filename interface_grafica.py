import requests
from tkinter import *
from jogar_bomb import iniciar_bomb

janela = Tk()
janela.title("Jogar Bomb Crypto")
texto_orientacao = Label(janela, text="Clique para iniciar o game")
botao = Button(janela, text="Iniciar Bomb", command=iniciar_bomb)
botao.grid(column=0, row=3, padx=10, ipady=10)
janela.mainloop()
