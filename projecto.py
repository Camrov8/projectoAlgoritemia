#Este ficheiro contem o programa pedido para o projecto final da desciplina de algoritmia
import os

#Bloco destinado aos varios tipos de pedidos
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

#Função destinada a gerir a criação dos varios pedidos de criação comboios e etc
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
            
#função para criar linha
def criarLinha():
    lerLinhas = open('./carris.csv', 'r')
    linhas = lerLinhas.readlines()

    sair = False
     
    while sair == False:
        print('Indique as duas estações para criar a linha /n Indique estação Inicial')
        estacaoA = input()
        print('insira estação B')
        estacaoB = input()
        criarLinha=''

        existeCarril = False

        # Verificar Carris
        for line in linhas:
            if estacaoA not in line and estacaoB in line:  
                existeCarril = True
                break  
           # else:
        '''        
        if not existeCarril:
            print("não existe linha")
            '''

#Função para gestão da criação de linhas e viagens(incompleto)
def menuLinha():
    escolha = ''
    while escolha!= 'x':
        print('Escolha uma das opções :\n A:criar linhas \n B:Criar viagem \n X:sair')

        escolha = input().lower()
        if escolha == 'a':
            criarLinha()
#Bloco destinado as funções destinadas as listagens
#Função para tratar da listagem das estações
def listaEstacoes():
    lerEstacoes = open('./Estacoes.csv','r')
    estacoes = lerEstacoes.readlines()
    lerEstacoes.close()
    
    for estacao in estacoes:
        print(estacao)

#Função para tratar da listagem das linhas
def listaLinhas():
    lerLinhas = open('./Linhas.csv','r')
    linhas = lerLinhas.readlines()
    lerLinhas.close()
    
    for linha in linhas:
        print(linha)

#Função para tratar da listagem dos Comboios 
def listaComboios():
    lerComboios = open('./Comboios.csv','r')
    comboios = lerComboios.readlines()
    lerComboios.close()
    
    for Comboio in comboios:
        print(Comboio)

#função que vai gerir as listagens
def menuListar ():
    escolha=''
    while escolha !='x' :
        print('inidque o que lista deseja aceder \n A:Estações \n B:Linhas \n C:Comboios \n X:sair')  
        escolha=input().lower()

        if escolha == 'a':
            listaEstacoes()

        if escolha == 'b':
            listaLinhas()

        if escolha == 'c':
            listaComboios()

        if escolha == 'x':
            print('A sair')
#Bloco destinado as varias funções de pesquisa
def procuraComboios():
    lerComboios = open('./Comboios.csv','r')
    comboios = lerComboios.readlines().lower()
    lerComboios.close()
    escolha =''

    while escolha !='x'

    print('Indique o Modelo e/ou numero de passageiros /n X:Sair')
    print('Modelo: ')
    modelo = input().lower
    print('Nº max passageiros: ')
    maxPax = input()

    if len(modelo)< 2 and len(maxPax)< 2 :
        print('valores invalidos insira novamente')
    

#função destinada as pesquisas 
def menuPesquisa ():
    escolha = ''

    while escolha !='x'

        print('Seleccione uma opção \n A:Procurar comboios \n X:Sair'
        escolha = input().lower()

        if escolha == 'a':
              procuraComboios()
              
############ PROGRAMA ############
escolhaPrincipal=''
while escolhaPrincipal != 'x':
    print("Menu informativo \n Escolha uma opção \n A:Gestão \n B:Listagem \n C:Viagens \n D:Criaçao linha/viagem \n E:Pesquisa \n X:sair")

    escolhaPrincipal = input().lower()

    if escolhaPrincipal == 'a':
        menuGestao()

    if escolhaPrincipal == 'b':
        menuListar()

    if escolhaPrincipal =='d':
        menuLinha()

    if escolhaPrincipal =='E':
        menuPesquisa()
                
    elif escolhaPrincipal == 'x':
        print('A sair')
        
    else :
        print('Opção invalida')
                
            





