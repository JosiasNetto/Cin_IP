#Variaveis globais para o codigo 
mochila_clarisse = []
direcao = '' 
index_atual = 0
decisao_clarisse = ''

#Recebendo as entradas do codigo
arsenal = input().split(' - ')
numero_giradas = int(input())

#Pegando o index do objeto que aparecera 
index_atual = int(len(arsenal) / 2)


#Loop que passa pela quantidade de vezes que clarisse girara a roleta
for num in range(numero_giradas):

    #Recebendo o numero de giradas e a direcao
    direcao = input()

    #Loop que passa pelo numero que clarisse digitou, ja que pega tudo da string, menos o ultimo elemento, que é a direção
    for i in range(int(direcao[0:-1])):
       
       #Calculando o index se girar para a esquerda
        if '<' in direcao:
            index_atual -= 1
            #Se o index passar do limite, voltara para a arma do inicio(que é a arma apos ele)
            if index_atual < 0 - len(arsenal):
                index_atual = -1
            
        #Calculando o index da esquerda
        if '>' in direcao:
            index_atual += 1
            if index_atual > len(arsenal) - 1:
                index_atual = 0

    #Recebendo se ira adcionar a arma ou não
    decisao_clarisse = input()

    #Verificando se a arma ja esta na mochila
    if arsenal[index_atual] in mochila_clarisse:
        print(f'{arsenal[index_atual]} já está na mochila. Não seja gananciosa, ou acabará como Midas!')
           
    #Se não estiver, verificando a decisão de clarisse 
    else:
        if decisao_clarisse == 'Adicionar':
            mochila_clarisse.append(arsenal[index_atual])
            print(f'{arsenal[index_atual]} adicionado a mochila!')
        
        elif decisao_clarisse == 'Ignorar':
            print(f'{arsenal[index_atual]} não vai ser tão útil assim!')

#Quando o loop acaba, verifica se a mochila de clarisse esta vazia, e imprimi uma mensagem se estiver
if mochila_clarisse != []:
    print('Com',end='')
    for obj in range(len(mochila_clarisse)):
        print(f' {mochila_clarisse[obj]},',end='')
    print(f' seremos imbatíveis na caça à bandeira!')    

#Se a mochila não estiver vazia, imprimira o nome de cada arma que pegou
else:
    print(f'Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…')

    