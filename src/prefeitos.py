# Candidatos a Prefeito
from tkinter import *
from vereadores import votar_Vereador
from finalizar import prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz, voto_null, voto_Branco

def votar_prefeito():
    menu_inicial = Tk()
    menu_inicial.title("URNA ELETRÔNICA")
    menu_inicial.geometry("750x400")

    # Textos / Labels
    label_titulo = Label(menu_inicial,
                         text="Eleição - 2022",
                         font="Time 15",
                         fg="#000000",
                         width=15,
                         height=2,
                         anchor=CENTER)

    label_1 = Label(menu_inicial,
                    text="Candidato a Prefeito(a): ",
                    font="Arial 10",
                    fg="#000000",
                    width=20,
                    height=2,
                    anchor=CENTER)

    label_2 = Label(menu_inicial,
                    text="Justiça Eleitoral",
                    font="Arial 10 bold",
                    fg="#000000",
                    width=12,
                    height=2,
                    anchor=CENTER)

    label_3 = Label(menu_inicial,
                    text="                ",
                    font="Arial 20",
                    fg="#0000ff",
                    bd=1,
                    relief=GROOVE,
                    padx=5,
                    pady=5,
                    anchor=CENTER)

    label_4 = Label(menu_inicial,
                    text="[01] - Pernalonga",
                    font="Arial 10 bold",
                    fg="#000000",
                    width=15,
                    height=2,
                    anchor=E)

    label_5 = Label(menu_inicial,
                    text="[02] - Patolino",
                    font="Arial 10 bold",
                    fg="#000000",
                    width=15,
                    height=2,
                    anchor=CENTER)

    label_6 = Label(menu_inicial,
                    text="[03]-TazMania",
                    font="Arial 10 bold",
                    fg="#000000",
                    width=15,
                    height=2,
                    anchor=CENTER)
    label_7 = Label(menu_inicial,
                    text="",
                    font="Arial 10 bold",
                    fg="#000000",
                    relief=FLAT,
                    padx=5,
                    pady=2,
                    anchor=CENTER)

    # grid Textos
    label_titulo.grid(row=0, column=1)
    label_1.grid(row=1, column=1)
    label_2.grid(row=1, column=3)
    label_3.grid(row=3, column=1)
    label_4.grid(row=3, column=6)
    label_5.grid(row=4, column=6)
    label_6.grid(row=5, column=6)
    label_7.grid(row=4, column=1)            

    def botao_0():
        label_7['text'] = "0"
        prefeito_Pernalonga.append(label_7["text"])

    def botao_1():
        
        label_7['text'] = "01"
        prefeito_Pernalonga.append(1)
        label_3['text'] = "Pernalonga - Patido LT"
        prefeito_Pernalonga.append(label_3["text"])

    def botao_2():
        label_7['text'] = "02"
        prefeito_Patolino.append(1)
        label_3['text'] = "Patolino - Patido PLT"
        prefeito_Patolino.append(label_3["text"])
 
    def botao_3():
        label_7['text'] = "03"
        prefeito_Patolino.append(1)
        label_3['text'] = "TazMania - Partido PD"
        prefeito_Taz.append(label_3["text"])

    def botao_NULL():
        label_3['text'] = "Para votar em NULO,click em Confirmar."
        voto_null.append(label_3["text"])

    def botao_Branco():
        label_3['text'] = "Para votar em Branco, click em Confirmar."
        voto_Branco.append(label_3["text"])

    cmd_01 = Button(menu_inicial,
                    text="1",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_1())

    cmd_02 = Button(menu_inicial,
                    text="2",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_2())

    cmd_03 = Button(menu_inicial,
                    text="3",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_3())

    cmd_04 = Button(menu_inicial,
                    text="4",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_NULL())

    cmd_05 = Button(menu_inicial,
                    text="5",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_NULL())

    cmd_06 = Button(menu_inicial,
                    text="6",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_NULL())

    cmd_07 = Button(menu_inicial,
                    text="7",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_NULL())

    cmd_08 = Button(menu_inicial,
                    text="8",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_NULL())

    cmd_09 = Button(menu_inicial,
                    text="9",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_NULL())

    cmd_10 = Button(menu_inicial,
                    text="0",
                    width=6,
                    height=2,
                    anchor=W,
                    command=lambda: botao_NULL())

    cmd_11 = Button(menu_inicial,
                    text=" CONFIRMAR ",
                    width=11,
                    height=2,
                    anchor=W,
                    bg="#00ff00",
                    command=lambda: votar_Vereador())

    cmd_12 = Button(menu_inicial,
                    text=" CORRIGE ",
                    width=11,
                    height=2,
                    anchor=W,
                    bg="#FFA500",
                    command=lambda: votar_prefeito())

    cmd_13 = Button(menu_inicial,
                    text=" BRANCO ",
                    width=12,
                    height=2,
                    anchor=W,
                    bg="#ffffff",
                    command=lambda: botao_Branco())

    # Botões Grid
    cmd_01.grid(row=3, column=3)
    cmd_02.grid(row=3, column=4)
    cmd_03.grid(row=3, column=5)
    cmd_04.grid(row=4, column=3)
    cmd_05.grid(row=4, column=4)
    cmd_06.grid(row=4, column=5)
    cmd_07.grid(row=5, column=3)
    cmd_08.grid(row=5, column=4)
    cmd_09.grid(row=5, column=5)
    cmd_10.grid(row=6, column=4)
    cmd_11.grid(row=7, column=5)
    cmd_12.grid(row=7, column=4)
    cmd_13.grid(row=7, column=3)


    menu_inicial.mainloop()
