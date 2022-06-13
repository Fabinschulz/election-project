# Candidatos a Vereador
from tkinter import *
from finalizar import finalizar, vereador_Piu_Piu, vereador_Hector, vereador_Frajola, vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas, vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_Branco, voto_null

def votar_Vereador():
    menu_vereadores = Tk()
    menu_vereadores.title("URNA ELETRÔNICA")
    menu_vereadores.geometry("750x400")

    label_titulo = Label(menu_vereadores,
                         text="Eleição - 2022",
                         font="Time 15",
                         fg="#000000",
                         width=15,
                         height=2,
                         anchor=CENTER)

    label_1 = Label(menu_vereadores,
                    text="Candidato a Vereador(a): ",
                    font="Arial 10",
                    fg="#000000",
                    width=20,
                    height=2,
                    anchor=CENTER)

    label_2 = Label(menu_vereadores,
                    text="Vote:",
                    font="Arial 10",
                    fg="#000000",
                    width=5,
                    height=2,
                    anchor=CENTER)

    label_3 = Label(menu_vereadores,
                    text="                     ",
                    font="Arial 15",
                    fg="#0000ff",
                    bd=1,
                    relief=GROOVE,
                    padx=5,
                    pady=5,
                    anchor=CENTER)

    # Nome candidatos a Vereador
    label_4 = Label(menu_vereadores,
                    text=" [11111] - Piu-Piu ",
                    font="Arial 8 bold",
                    fg="#000000",
                    width=15,
                    height=2,                  
                    anchor=W)

    label_5 = Label(menu_vereadores,
                    text="[22222] - Hector",
                    font="Arial 8 bold",
                    fg="#000000",
                    width=15,
                    height=2,
                    anchor=W)

    label_6 = Label(menu_vereadores,
                    text="[33333] - Frajola",
                    font="Arial 8 bold",
                    fg="#000000",
                    width=15,
                    height=2,
                    anchor=W)

    label_7 = Label(menu_vereadores,
                    text="[44444] - Vovó",
                    font="Arial 8 bold",
                    fg="#000000",
                    width=16,
                    height=2,
                    anchor=W)

    label_8 = Label(menu_vereadores,
                    text="[55555] - Bulldog",
                    font="Arial 8 bold",
                    fg="#000000",
                    width=15,
                    height=2,
                    anchor=W)

    label_9 = Label(menu_vereadores,
                    text="[66666] - Papa-Léguas",
                    font="Arial 8 bold",
                    fg="#000000",
                    width=16,
                    height=2,
                    anchor=W)

    label_10 = Label(menu_vereadores,
                     text="[77777] - Coiote",
                     font="Arial 8 bold",
                     fg="#000000",
                     width=15,
                     height=2,
                     anchor=W)

    label_11 = Label(menu_vereadores,
                     text="[88888] - Ligeirinho",
                     font="Arial 8 bold",
                     fg="#000000",
                     width=15,
                     height=2,
                     anchor=W)

    label_12 = Label(menu_vereadores,
                     text="[99999] - Marvin",
                     font="Arial 8 bold",
                     fg="#000000",
                     width=15,
                     height=2,
                     anchor=W)

    label_13 = Label(menu_vereadores,
                     text="[010203] - Lola",
                     font="Arial 8 bold",
                     fg="#000000",
                     width=15,
                     height=2,
                     anchor=W)

    label_14 = Label(menu_vereadores,
                     text="[0] - Nulo",
                     font="Arial 8 bold",
                     fg="#000000",
                     width=15,
                     height=2,
                     anchor=W)

    label_15 = Label(menu_vereadores,
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

    label_4.grid(row=1, column=6)
    label_5.grid(row=3, column=6)
    label_6.grid(row=4, column=6)
    label_7.grid(row=5, column=6)
    label_8.grid(row=6, column=6)
    label_9.grid(row=1, column=7)
    label_10.grid(row=3, column=7)
    label_11.grid(row=4, column=7)
    label_12.grid(row=5, column=7)
    label_13.grid(row=6, column=7)
    label_14.grid(row=7, column=7)
    label_15.grid(row=4, column=1)
    

    def botao_0():
        label_14['text'] = "0"
        vereador_Piu_Piu.append(label_14["text"])

    def botao_1():
        label_7['text'] = "111111"
        vereador_Piu_Piu.append(1)
        label_3['text'] = "Piu-Piu - Partido PLT"
        vereador_Piu_Piu.append(label_3["text"])

    def botao_2():
        label_7['text'] = "22222"
        vereador_Hector.append(1)
        label_3['text'] = "Hector - Partido PLT"
        vereador_Hector.append(label_3["text"])

    def botao_3():
        label_7['text'] = "33333"
        vereador_Frajola.append(1)
        label_3['text'] = "Frajola - Partido LT"
        vereador_Frajola.append(label_3["text"])

    def botao_4():
        label_7['text'] = "44444"
        vereador_Vovo.append(1)
        label_3['text'] = "Vovó - Partido PL"
        vereador_Vovo.append(label_3["text"])

    def botao_5():
        label_7['text'] = "55555"
        vereador_Bulldog.append(1)
        label_3['text'] = "Bulldog - Partido PD"
        vereador_Bulldog.append(label_3["text"])

    def botao_6():
        label_7['text'] = "66666"
        vereador_Papa_Leguas.append(1)
        label_3['text'] = "Papa-Léguas - Partido LT"
        vereador_Papa_Leguas.append(label_3["text"])

    def botao_7():
        label_7['text'] = "77777"
        vereador_Coiote.append(1)
        label_3['text'] = "Coiote - Partido PD"
        vereador_Coiote.append(label_3["text"])

    def botao_8():
        label_7['text'] = "88888"
        vereador_Ligeirinho.append(1)
        label_3['text'] = "Ligeirinho - Partido LT"
        vereador_Ligeirinho.append(label_3["text"])

    def botao_9():
        label_7['text'] = "99999"
        vereador_Marvin.append(1)
        label_3['text'] = "Marvin - Partido PLT"
        vereador_Marvin.append(label_3["text"])

    def botao_10():
        label_7['text'] = "010203"
        vereador_Lola.append(1)
        label_3['text'] = "Lola - Partido PLT"
        vereador_Lola.append(label_3["text"])
    
    def botao_NULL():
        label_3['text'] = "Para votar em NULO,click em Confirmar."
        voto_null.append(label_3["text"])

    def botao_Branco():
        label_3['text'] = "Para votar em Branco,click em Confirmar."
        voto_Branco.append(label_3["text"])

    # Botões / CMD
    cmd_01 = Button(menu_vereadores,
                    text=" 1 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_1())
    cmd_01 = Button(menu_vereadores,
                    text=" 1 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_1())

    cmd_02 = Button(menu_vereadores,
                    text=" 2 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_2())

    cmd_03 = Button(menu_vereadores,
                    text=" 3 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_3())

    cmd_04 = Button(menu_vereadores,
                    text=" 4 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_4())

    cmd_05 = Button(menu_vereadores,
                    text=" 5 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_5())

    cmd_06 = Button(menu_vereadores,
                    text=" 6 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_6())

    cmd_07 = Button(menu_vereadores,
                    text=" 7 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_7())

    cmd_08 = Button(menu_vereadores,
                    text=" 8 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_8())

    cmd_09 = Button(menu_vereadores,
                    text=" 9 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_9())

    cmd_10 = Button(menu_vereadores,
                    text=" 0 ",
                    width=5,
                    height=2,
                    anchor=W,
                    command=lambda: botao_NULL())
    cmd_11 = Button(menu_vereadores,
                    text=" CONFIRMAR ",
                    width=11,
                    height=2,
                    anchor=W,
                    bg="#00ff00",
                    command=lambda: finalizar())
    cmd_12 = Button(menu_vereadores,
                    text=" CORRIGE ",
                    width=11,
                    height=2,
                    anchor=W,
                    bg="#FFA500",
                    command=lambda: votar_Vereador())
    cmd_13 = Button(menu_vereadores,
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


    menu_vereadores.mainloop()