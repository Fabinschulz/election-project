"""Candidatos a vereador"""
from result import show_Resultados_Vereadores

def votar_Vereador():
     
    vereador_Piu_Piu = 0
    vereador_Hector = 0
    vereador_Frajola = 0
    vereador_Vovo = 0
    vereador_Bulldog = 0
    vereador_Papa_Leguas = 0
    vereador_Coiote = 0
    vereador_Ligeirinho = 0
    vereador_Marvin = 0
    vereador_Lola = 0
    
    print("====Eleição - Vereadores====")
    print("[1] - Piu-Piu ")
    print("[2] - Hector")
    print("[3] - Frajola")
    print("[4] - Vovó")
    print("[5] - Bulldog")
    print("[6] - Papa-Léguas")
    print("[7] - Coiote")
    print("[8] - Ligeirinho")
    print("[9] - Marvin")
    print("[10] - Lola")

    candidato = input("Digite o numero do candidato a Vereador: ")
    
    match candidato:
        case '1':
            vereador_Piu_Piu += 1
            print("Candidato a vereador(a) Piu-Piu \n ")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
        case '2': 
            vereador_Hector += 1
            print("Candidato a vereador(a) Hector \n ")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
        case '3':
            vereador_Frajola += 1
            print("Candidato a vereador(a) Frajola \n")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
    
        case '4': 
            vereador_Vovo += 1
            print("Candidato a vereador(a) Vovó \n")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
        case '5':
            vereador_Bulldog += 1
            print("Candidato a vereador(a) Bulldog \n")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
    
        case '6':
            vereador_Papa_Leguas += 1 
            print("Candidato a vereador(a) Papa-Léguas \n")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
        case '7':
            vereador_Coiote += 1 
            print("Candidato a vereador(a) Coiote \n")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
    
        case '8': 
            vereador_Ligeirinho += 1 
            print("Candidato a vereador(a) Ligeirinho \n")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
        case '9':
            vereador_Marvin += 1 
            print("Candidato a vereador(a) Marvin \n")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
        case '10': 
            vereador_Lola += 1 
            print("Candidato a vereador(a) Lola \n")
            show_Resultados_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola)
            
        case _: 
            print(f'Número {candidato} inválido, Por Favor insira o número do candidato novamente.')