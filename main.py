"""Menu Inicial"""
from prefeitos import votar_prefeito

print('Eleição 2022')
print('[1] - Iniciar a Eleição')
print('[2] - finalizar a Eleição')

option = input("Digite a opção desejada: ")

if(option == '1'):
    votar_prefeito()

if(option == '2'):
    pass