"""Mostra o Resultado Final dos Votos para cada candidato"""
from tkinter import *
 
import prefeitos

prefeito_Pernalonga = []
prefeito_Patolino = []
prefeito_Taz = []
voto_null = []
voto_Branco = []

vereador_Piu_Piu = []
vereador_Hector = []
vereador_Frajola = []
vereador_Vovo = []
vereador_Bulldog = []
vereador_Papa_Leguas = []
vereador_Coiote = []
vereador_Ligeirinho = []
vereador_Marvin = []
vereador_Lola = []



def finalizar():
    menu_inicial = Tk()
    menu_inicial.title("URNA ELETRÔNICA")
    menu_inicial.geometry("700x400")

    def bot_fin(): 
        if(prefeito_Pernalonga):
             print(f"Prefeito eleito: {prefeito_Pernalonga[1]}.")
             print(f'candidato a prefeito Pernalonga - teve {prefeito_Pernalonga[0]} votos\n')

        if(prefeito_Patolino):
             print(f"Prefeito eleito: {prefeito_Patolino[1]}.")
             print(f'candidato a prefeito Patolino - teve {prefeito_Patolino[0]} votos\n')

        if(prefeito_Taz):
             print(f"Prefeito eleito: {prefeito_Taz[1]}.")
             print(f'candidato a prefeito Pernalonga - teve {prefeito_Taz[0]} votos\n')


        if(vereador_Piu_Piu):
             print(f"Vereador eleito: {vereador_Piu_Piu[1]}.")
             print(f'candidato a vereador Piu Piu - teve {vereador_Piu_Piu[0]} votos \n')

        if(vereador_Hector):
             print(f"Vereador eleito: {vereador_Hector[1]}.")
             print(f'candidato a vereador Hector - teve {vereador_Hector[0]} votos \n')

        if(vereador_Frajola):
             print(f"Vereador eleito: {vereador_Frajola[1]}.")
             print(f'candidato a vereador Frajola - teve {vereador_Frajola[0]} votos \n')

        if(vereador_Vovo):
             print(f"Vereador eleito: {vereador_Vovo[1]}.")
             print(f'candidato a vereador Vovó - teve {vereador_Vovo[0]} votos \n')

        if(vereador_Bulldog):
             print(f"Vereador eleito: {vereador_Bulldog[1]}.")
             print(f'candidato a vereador Bulldog - teve {vereador_Bulldog[0]} votos \n')

        if(vereador_Papa_Leguas):
             print(f"Vereador eleito: {vereador_Papa_Leguas[1]}.")
             print(f'candidato a vereador Papa-Léguas - teve {vereador_Papa_Leguas[0]} votos \n')

        if(vereador_Coiote):
             print(f"Vereador eleito: {vereador_Coiote[1]}.")
             print(f'candidato a vereador Coiote - teve {vereador_Coiote[0]} votos \n')

        if(vereador_Ligeirinho):
             print(f"Vereador eleito: {vereador_Ligeirinho[1]}.")
             print(f'candidato a vereador Ligeirinho - teve {vereador_Ligeirinho[0]} votos \n')

        if(vereador_Marvin):
             print(f"Vereador eleito: {vereador_Marvin[1]}.")
             print(f'candidato a vereador Marvin - teve {vereador_Marvin[0]} votos \n')

        if(vereador_Lola):
             print(f"Vereador eleito: {vereador_Lola[1]}.")
             print(f'candidato a vereador Lola {vereador_Lola[0]} votos \n')

        if(voto_null):
             print(f'Votos em Nulo {voto_null} votos ')
             
        if(voto_Branco):
             print(f'Votos em Branco {voto_Branco} votos \n')

    label_finaliza_voto = Label(menu_inicial,
                        text="FIM",
                        font="Time 20",
                        fg="#000000",
                        width=20,
                        height=2,
                        anchor=CENTER)
                        
    label_retornar_voto = Label(menu_inicial,
                        text="Continuar a Votar",
                        font="Time 20",
                        fg="#000000",
                        width=20,
                        height=2,
                        anchor=CENTER)
                        
    label_finaliza_voto.grid(row=1, column=3)
    label_retornar_voto.grid(row=1, column=4)


    cmd_finaliza = Button(menu_inicial,
                       text=" Clique aqui para finalizar",
                       width=20,
                       height=2,
                       anchor=CENTER,
                       command=lambda: bot_fin())

    cmd_continua = Button(menu_inicial,
                       text=" Clique aqui para continuar",
                       width=20,
                       height=2,
                       anchor=CENTER,
                       command=lambda: prefeitos.votar_prefeito())

    cmd_finaliza.grid(row=2, column=3)
    cmd_continua.grid(row=2, column=4)

    menu_inicial.mainloop()
