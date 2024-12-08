#Este ficheiro contem o programa pedido para o projecto final da desciplina de algoritmia
import os

def criarEstacao():
    print('Indique codigo da estação')
    codigo = input().upper()
    print('Indique o nome')
    nome = input()
    print('Indique a latitude')
    latitude = input()
    print('Indique a longitude')
    longitude = input()
    estacao = codigo , nome , latitude , longitude
    print(estacao)
     

def menuGestao():
    #Codigo para adicionar estção
    escolhaGestao = ''
    while escolhaGestao != 'x' :
        print('Escolha uma das opções :\n A:Adicionar estação \n X:sair')
        escolhaGestao = input().lower()
            
        if escolhaGestao == 'a':
            criarEstacao()
            
        elif escolhaGestao == 'x':
            print('A sair')
            
        else :
            print('Opção invalida')
        

escolhaPrincipal=''

while escolhaPrincipal != 'x':
    print("Menu informativo \n Escolha uma opção \n A:Gestão \n B:LISTAGEM \n C:Viagens \n X:sair")

    escolhaPrincipal = input().lower()

    if escolhaPrincipal == 'a':
       menuGestao() 
        
                
    elif escolhaPrincipal == 'x':
        print('A sair')
        
    
    else :
        print('Opção invalida')
                
            








#para suporte para apagar
#PCAM,Porto Campanhã, Latitude: 3, Longitude: 4
