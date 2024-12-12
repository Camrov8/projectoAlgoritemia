lerLinhas = open('./carris.csv', 'r')
linhas = lerLinhas.readlines()


existeCarril = False

# Verificar Carris
for line in linhas:
    if 'Porto' not in line and 'Coimbra' in line:  
        existeCarril = True
        break  


if not existeCarril:
    print("não existe linha")
