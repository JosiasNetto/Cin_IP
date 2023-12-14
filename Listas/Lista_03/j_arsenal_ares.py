#Variaveis globais para o codigo 
mochila_clarisse = []
index_objeto_meio = 0
direcao = ''
ultima_arma_olhada = ''
num_giros = 0 
index_objeto_rodado = 0
index_atual = 0
decisao_clarisse = ''


arsenal = input().split('-')
index_objeto_meio = int(len(arsenal) / 2)
index_atual = index_objeto_meio
numero_giradas = int(input())

for num in range(numero_giradas):
    direcao = input()

    for i in range(int(direcao[0:-1])):
       
        if '<' in direcao:
            index_atual -= 1
            if index_atual < 0 - len(arsenal):
                index_atual = -1
            

        if '>' in direcao:
            index_atual += 1
            if index_atual > len(arsenal):
                index_atual = 0

    decisao_clarisse = input()

    if         
    