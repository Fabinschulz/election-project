"""Candidatos a presidencia"""
from vereadores import votar_Vereador
from result import show_Result_Prefeitos

def votar_prefeito():
    
    prefeito_Pernalonga = 0
    prefeito_Patolino = 0
    prefeito_Taz = 0
    voto_null = 0
    voto_Branco = 0
    
    print("====Eleição Presidente====")
    print('[01] - Pernalonga')
    print('[02] - Patolino')
    print('[03] - Taz')
        
    candidato = input("Digite o numero do candidato a Presidencia ou [0] para votar em Branco: ")
    
    match candidato:
        case '0': 
            voto_Branco += 1 
            print("Voto em Branco \n")
            votar_Vereador()
            show_Result_Prefeitos(prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz, voto_null, voto_Branco)
            
        case "01":
            prefeito_Pernalonga += 1
            print('Candidato a prefeito Pernalonga - Patido LT \n')
            votar_Vereador()
            show_Result_Prefeitos(prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz, voto_null, voto_Branco)
    
        case "02": 
            prefeito_Patolino += 1
            print('Candidato a prefeito Patolino - Patido PLT \n')
            votar_Vereador()
            show_Result_Prefeitos(prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz, voto_null, voto_Branco)
            
        case "03": 
            prefeito_Taz += 1
            print('Candidato a prefeito Taz  - Partido PD\n')
            votar_Vereador()
            show_Result_Prefeitos(prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz, voto_null, voto_Branco)
            
        case _: 
            print(f'Número {candidato} inválido, o seu voto será computado como NULO. \n')
            
            votos = input("Digite o SIM para confirmar ou NÃO para retornar: \n")
            while True:
                
                if votos == "sim" or votos == "SIM" or votos == "Sim":
                    voto_null += 1
                    show_Result_Prefeitos(prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz, voto_null, voto_Branco)
                    break
                else: 
                    votar_prefeito()
                    break

        
                
