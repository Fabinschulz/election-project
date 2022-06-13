# Zeresima
from tkinter import *

def candidatos_eleicao():
    menu_zeresima = Tk()
    menu_zeresima.title("Candidatos")
    menu_zeresima.geometry("800x450")

    label_titulo = Label(
                         text="Candidatos a Eleição - 2022",
                         font="Time 15",
                         fg="#000000",
                         width=45,
                         height=2,
                         anchor=E)

    # Candidatos a Prefeito
    label_1 = Label(menu_zeresima,
                    text=" Candidatos a Prefeito:",
                    font="Time 10 bold",
                    fg="#000000",
                    width=21,
                    height=2,
                    anchor=E)
    label_2 = Label(menu_zeresima,
                    text="Pernalonga = 0 votos",
                    font="Arial 10",
                    fg="#000000",
                    width=17,
                    height=2,
                    anchor=E)

    label_3 = Label(menu_zeresima,
                    text="Patolino = 0 votos",
                    font="Arial 10",
                    fg="#000000",
                    width=14,
                    height=2,
                    anchor=W)

    label_4 = Label(menu_zeresima,
                    text="TazMania = 0 votos",
                    font="Arial 10",
                    fg="#000000",
                    width=25,
                    height=2,
                    anchor=CENTER)

    # Nome candidatos a Vereador
    label_5 = Label(menu_zeresima,
                    text="Candidatos a Vereador:",
                    font="Time 10 bold",
                    fg="#000000",
                    width=30,
                    height=2,                  
                    anchor=W)
    label_6 = Label(menu_zeresima,
                    text="Piu-Piu = 0 votos",
                    font="Arial 10 ",
                    fg="#000000",
                    width=25,
                    height=2,                  
                    anchor=W)

    label_7 = Label(menu_zeresima,
                    text="Hector = 0 votos",
                    font="Arial 10 ",
                    fg="#000000",
                    width=25,
                    height=2,
                    anchor=W)

    label_8 = Label(menu_zeresima,
                    text="Frajola = 0 votos",
                    font="Arial 10 ",
                    fg="#000000",
                    width=25,
                    height=2,
                    anchor=W)

    label_9 = Label(menu_zeresima,
                    text="Vovó = 0 votos",
                    font="Arial 10 ",
                    fg="#000000",
                    width=25,
                    height=2,
                    anchor=W)

    label_10 = Label(menu_zeresima,
                    text="Bulldog = 0 votos",
                    font="Arial 10",
                    fg="#000000",
                    width=25,
                    height=2,
                    anchor=W)

    label_11 = Label(menu_zeresima,
                    text="Papa-Léguas= 0 votos",
                    font="Arial 10",
                    fg="#000000",
                    width=25,
                    height=2,
                    anchor=W)

    label_12 = Label(menu_zeresima,
                     text="Coiote= 0 votos",
                     font="Arial 10",
                     fg="#000000",
                     width=25,
                     height=2,
                     anchor=W)

    label_13 = Label(menu_zeresima,
                     text="Ligeirinho= 0 votos",
                     font="Arial 10",
                     fg="#000000",
                     width=25,
                     height=2,
                     anchor=W)

    label_14 = Label(menu_zeresima,
                     text="Marvin= 0 votos",
                     font="Arial 10",
                     fg="#000000",
                     width=25,
                     height=2,
                     anchor=W)

    label_15 = Label(menu_zeresima,
                     text="Lola= 0 votos",
                     font="Arial 10",
                     fg="#000000",
                     width=25,
                     height=2,
                     anchor=W)

    # grid Textos
    label_titulo.grid(row=0, column=1)

    label_1.grid(row=1, column=1)
    label_2.grid(row=2, column=1)
    label_3.grid(row=3, column=1)
    label_4.grid(row=4, column=1)

    label_5.grid(row=1, column=2)
    label_6.grid(row=2, column=2)
    label_7.grid(row=3, column=2)
    label_8.grid(row=4, column=2)
    label_9.grid(row=5, column=2)
    label_10.grid(row=6, column=2)
    label_11.grid(row=7, column=2)
    label_12.grid(row=8, column=2)
    label_13.grid(row=9, column=2)
    label_14.grid(row=10, column=2)
    label_14.grid(row=11, column=2)

    
    menu_zeresima.mainloop()