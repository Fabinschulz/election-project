"""Candidatos a presidencia"""
from vereadores import votar_Vereador
from result import show_Resultados_Prefeitos

def votar_prefeito():
    
    prefeito_Pernalonga = 0
    prefeito_Patolino = 0
    prefeito_Taz = 0
    
    print("====Eleição Presidente====")
    print('[01] - Pernalonga')
    print('[02] - Patolino')
    print('[03] - Taz')
        
    candidato = input("Digite o numero do candidato a Presidencia: ")
    
    match candidato:
        case "01":
            prefeito_Pernalonga += 1
            print('Candidato a prefeito Pernalonga \n')
            show_Resultados_Prefeitos(prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz)
            votar_Vereador()
    
        case "02": 
            prefeito_Patolino += 1
            print('Candidato a prefeito Patolino \n')
            show_Resultados_Prefeitos(prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz)
            votar_Vereador()
            
        case "03": 
            prefeito_Taz += 1
            print('Candidato a prefeito Taz \n')
            show_Resultados_Prefeitos(prefeito_Pernalonga, prefeito_Patolino, prefeito_Taz)
            votar_Vereador()
            
        case _: 
            print(f'Número {candidato} inválido, Por Favor insira o número do candidato novamente.')

        
                
