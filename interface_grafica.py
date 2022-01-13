import requests
from tkinter import *

import jogar_bomb
from jogar_bomb import iniciar_bomb
import jogar_bomb_personagens_individuais
from jogar_bomb_personagens_individuais import iniciar_bomb_ind
from colocar_todos_para_trabalhar import iniciar_bomb_todos




janela = Tk()
janela.title("Jogar Bomb Crypto")
janela.geometry("400x400")
texto_orientacao = Label(janela, text="Clique para iniciar o game")
texto_orientacao.grid(column=0, row=0, padx=10, ipady=10)
botao = Button(janela, text="Iniciar Bomb", command=iniciar_bomb)
botao.grid(column=0, row=1, padx=10, ipady=10)
botao = Button(janela, text="Iniciar Bomb Ind", command=iniciar_bomb_ind)
botao.grid(column=0, row=2, padx=10, ipady=10)
botao = Button(janela, text="Finalizar Bomb", command=jogar_bomb.finalizar_bomb)
botao.grid(column=0, row=3, padx=10, ipady=10)
botao = Button(janela, text="Iniciar Bomb Todos", command=iniciar_bomb_todos)
botao.grid(column=0, row=4, padx=10, ipady=10)
janela.mainloop()
