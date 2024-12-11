#Este ficheiro contem o programa pedido para o projecto final da desciplina de algoritmia
import os
#funcão para tratar adição de estações
def criarEstacao():
    print('Indique codigo da estação')
    codigo = input().upper()
    print('Indique o nome')
    nome = input()
    print('Indique a latitude')
    latitude = input()
    print('Indique a longitude')
    longitude = input()
    estacao = "\n" + codigo + "," + nome + "," + latitude + "," + longitude
    gravarFicheiro = open("estacoes.csv", 'a')
    gravarFicheiro.write(estacao)
    gravarFicheiro.close()

#funcão para tratar adição de carris
def criarCarril():
    print('Indique nome da primeira estação')
    nome1 = input().upper()
    print('Indique o nome da segunda estação')
    nome2 = input()
    print('distancia')
    dist = input()
    carril = "\n" + nome1 + "," + nome2 + "," + dist
    gravarFicheiro = open("carris.csv", 'a')
    gravarFicheiro.write(carril)
    gravarFicheiro.close()
#função para tratar da adição de comboios
def criarComboio():
    print('Indique modelo')
    modelo = input().upper()
    print('Indique nº de serie')
    nSerie = input().upper()
    print('Indique nº de passageiros')
    nPax = input()
    print('indique serviço')
    servico = input().upper()
    comboio = "\n" + modelo + "," + nSerie  + "," + nPax + "," + servico
    gravarFicheiro = open("comboios.csv", 'a')
    gravarFicheiro.write(comboio)
    gravarFicheiro.close()  

#Função destinada a gerir a criação dos varios pedidos comboios e etc
def menuGestao():
    escolhaGestao = ''
    while escolhaGestao != 'x' :
        print('Escolha uma das opções :\n A:Adicionar estação \n B:Adicionar carril \n C:Adicionar comboio \n X:sair')
        escolhaGestao = input().lower()
            
        if escolhaGestao == 'a':
            criarEstacao()
            
        if escolhaGestao == 'b':
            criarCarril()
        
        if escolhaGestao == 'c':
            criarComboio()
            
        elif escolhaGestao == 'x':
            print('A sair')
            
        else :
            print('Opção invalida')

def criarLinha ():
    


#Função para gestão da criação de linhas e viagens
def menuLinha():
    escolha=''
while escolha!='x':
    print('Escolha uma das opções :\n A:criar linha \n B:Criar viagem \n X:sair')

    escolha=input().lower

    if escolha == 'a'
        criarLinha()

while escolhaPrincipal != 'x':
    print("Menu informativo \n Escolha uma opção \n A:Gestão \n B:LISTAGEM \n C:Viagens \n D:Criaçao linha/viagem \n X:sair")

    escolhaPrincipal = input().lower()

    if escolhaPrincipal == 'a':
       menuGestao()

    if escolhaPrincipal =='d':
        menuLinha()
        
                
    elif escolhaPrincipal == 'x':
        print('A sair')
        
    
    else :
        print('Opção invalida')
                
            








#para suporte para apagar
#PCAM,Porto Campanhã, Latitude: 3, Longitude: 4
