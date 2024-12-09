#Este ficheiro contem o programa pedido para o projecto final da desciplina de algoritmia
import os
ficheiroEstacoes = open('./Estacoes.csv','r')

estacoes = ficheiroEstacoes.readlines()

for estacao in estacoes:
    listaEstacao = estacao.split(',')
    codigoEstacao = listaEstacao[0]
    nomeEstacao = listaEstacao[1]
    coordEstacao = (listaEstacao[2],listaEstacao[3])

    print(codigoEstacao, ' ', nomeEstacao, ' ',coordEstacao, ' ')
 

#Leitura do ficheiro com todos os dados referentes as linhas .

print("Menu informativo \n Escolha uma opção \n A:Gestão \n B:LISTAGEM \n C:Viagens")

escolha = input()






#para suporte para apagar
#PCAM,Porto Campanhã, Latitude: 3, Longitude: 4
