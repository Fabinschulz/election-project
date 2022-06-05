"""Candidatos a vereador"""
from result import show_Result_Vereadores

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
    voto_null = 0
    voto_Branco = 0
    
    print("====Eleição - Vereadores====")
    print("[01010] - Piu-Piu ")
    print("[20202] - Hector")
    print("[30303] - Frajola")
    print("[40404] - Vovó")
    print("[50505] - Bulldog")
    print("[60606] - Papa-Léguas")
    print("[70707] - Coiote")
    print("[80808] - Ligeirinho")
    print("[90909] - Marvin")
    print("[10101] - Lola \n")

    candidato = input("Digite o numero do candidato a Vereador ou [0] para votar em Branco: ")
    
    match candidato:
        case '01010':
            vereador_Piu_Piu += 1
            print("Candidato a vereador(a) Piu-Piu - Partido PLT \n ")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola,voto_null, voto_Branco)
            
        case '20202': 
            vereador_Hector += 1
            print("Candidato a vereador(a) Hector - Partido PLT \n ")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
        case '30303':
            vereador_Frajola += 1
            print("Candidato a vereador(a) Frajola - Partido LT \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
    
        case '40404': 
            vereador_Vovo += 1
            print("Candidato a vereador(a) Vovó - Partido PL  \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
        case '50505':
            vereador_Bulldog += 1
            print("Candidato a vereador(a) Bulldog - Partido PD \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
    
        case '60606':
            vereador_Papa_Leguas += 1 
            print("Candidato a vereador(a) Papa-Léguas - Partido LT \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
        case '70707':
            vereador_Coiote += 1 
            print("Candidato a vereador(a) Coiote - Partido PD  \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null,voto_Branco)
    
        case '80808': 
            vereador_Ligeirinho += 1 
            print("Candidato a vereador(a) Ligeirinho - Partido LT \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
        case '90909':
            vereador_Marvin += 1 
            print("Candidato a vereador(a) Marvin - Partido PLT \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
        case '10101': 
            vereador_Lola += 1 
            print("Candidato a vereador(a) Lola - Partido PLT  \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
        case '0': 
            voto_Branco += 1 
            print("Voto em Branco \n")
            show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
            
        case _:
            print(f'Número {candidato} para vereador inválido, o seu voto será computado como NULO. \n')
            
            votos = input("Digite o SIM para confirmar ou NÃO para retornar: \n")
            while True:
                
                if votos == "sim" or votos == "SIM" or votos == "Sim":
                    voto_null += 1
                    show_Result_Vereadores(vereador_Piu_Piu, vereador_Hector,vereador_Frajola,
                                       vereador_Vovo, vereador_Bulldog, vereador_Papa_Leguas,
                                       vereador_Coiote, vereador_Ligeirinho, vereador_Marvin, vereador_Lola, voto_null, voto_Branco)
                    break
                else: 
                    votar_Vereador()
                    break
           