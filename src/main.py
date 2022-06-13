"""Menu Inicial"""
import prefeitos
from zeresima import candidatos_eleicao


class main():

    print('Eleição 2022')
    print('[1] - Iniciar a votação')
    print('[2] - Imprimir Zerésima')

    option = input("Digite a opção desejada: ")

    if(option == '1'):
        prefeitos.votar_prefeito()

    if(option == '2'):
        candidatos_eleicao()
