#Funcao relativa a movimentacao do percy
def movendo_percy(direcao,percy_x,percy_y,agua_x,agua_y):

    #Recebe a direcao desejada como parametro
    #Executa a funcao que verifica se ele passou pela agua
    #Soma a respectiva coordenada que percy andou
    if direcao == 'cima':
        percy_y -= 1
        percy_y -= agua_boost(percy_x,percy_y,agua_x,agua_y)
        
    
    elif direcao == 'baixo':
        percy_y += 1
        percy_y += agua_boost(percy_x,percy_y,agua_x,agua_y)

    elif direcao == 'esquerda':
        percy_x -= 1
        percy_x -= agua_boost(percy_x,percy_y,agua_x,agua_y)
    
    elif direcao == 'direita':
        percy_x += 1
        percy_x += agua_boost(percy_x,percy_y,agua_x,agua_y)

    #Retorna as coordenadas do Percy
    return percy_x,percy_y

#Funcao que verifica se percy passou por cima da agua
def agua_boost(percy_x,percy_y,agua_x,agua_y):
    
    #Se passou, retorna o num 1 para adcionar a soma dos passos
    if percy_x == agua_x and percy_y == agua_y:
        print(f'Sinto o poder de Poseidon em minhas veias!')
        return 1
    
    #Se nao, retorna 0 e nada sera somado
    else:
        return 0

#Funcao que verifica se Clarisse esta na mesma coordenada que percy
#Retorna se o jogo acabou e se ela ganhou
def clarisse_ganhou(clarisse_x,percy_x,clarisse_y,percy_y):

    distancia_clarisse_percy_x = clarisse_x - percy_x
    distancia_clarisse_percy_y = clarisse_y - percy_y

    if distancia_clarisse_percy_x == 0 and distancia_clarisse_percy_y == 0:
        clarisse_ganha = True
        jogo_acabou = True
    
    else:
        clarisse_ganha = False
        jogo_acabou = False
    
    return jogo_acabou, clarisse_ganha, distancia_clarisse_percy_x, distancia_clarisse_percy_y

#Funcao que atualiza e imprimi a matriz
#Recebendo tanto a matriz atual, como as novas coordenadas como parametro
def printando_matriz(matriz_base,percy_x,percy_y,clarisse_x,clarisse_y):
    
    #Loop que passa pela matriz e tira os nomes de Percy e Clarisse dela
    for i in range(len(matriz_base)):
        #Segundo loop que passa especificamente por cada elemento da matriz
        for j in range(len(matriz_base[i])):
            #Verifica se o elemento eh = a C ou P, se for, o troca para -
            if matriz_base[i][j] == 'C' or matriz_base[i][j] == 'P':
                matriz_base[i][j] = '-'
    
    #Declara onde Percy e Clarisse estao com base nas novas coordenadas
    if percy_x <= 7 and percy_y <= 7:
        matriz_base[percy_y][percy_x] = 'P'
    
    if clarisse_x <= 7 and clarisse_y <= 7:
        matriz_base[clarisse_y][clarisse_x] = 'C'

    #Loop que passa por cada elemento da matriz e o imprimi
    for i in range(len(matriz_base)):
        for j in range(len(matriz_base[i])):

            #Verifica se eh o ultimo elemento da lista, caso seja, tira a quebra de linha e adciona espaco 
            if j < len(matriz_base) - 1:
                print(matriz_base[i][j],end=' ')
            
            else:
                print(matriz_base[i][j])

    #Retorna a matriz atualizada
    return matriz_base

#Funcao principal
def main():
    
    #Variaveis de Auxilio para o codigo
    matriz_base = [['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-']]
    jogo_acabou = False
    pegou_bandeira = False
    clarisse_venceu = False

    #Recebendo os inputs e adcionando suas respectivas letras na lista
    percy_y = int(input())
    percy_x = int(input())

    #Verificando se a coordenada existe na matriz 8x8, se sim, a adciona 
    if percy_x <= 7 and percy_y <= 7:
        matriz_base[percy_y][percy_x] = 'P'

    clarisse_y = int(input())
    clarisse_x = int(input())

    if clarisse_x <= 7 and clarisse_y <= 7:
        matriz_base[clarisse_y][clarisse_x] = 'C'

    agua_y = int(input())
    agua_x = int(input())

    if agua_x <= 7 and agua_y <= 7:
        matriz_base[agua_y][agua_x] = 'A'    

    bandeira_y = int(input())
    bandeira_x = int(input())

    if bandeira_x <= 7 and bandeira_y <= 7:
        matriz_base[bandeira_y][bandeira_x] = 'B'

    
    #Calculando a distancia x e y entre clarisse e percy
    diferenca_clarisse_percy_x = clarisse_x - percy_x
    diferenca_clarisse_percy_y = clarisse_y - percy_y
    
    #Loop que roda ate que o jogo acabe
    while not jogo_acabou:

        #Verifica se nao estao no mesmo x
        if diferenca_clarisse_percy_x != 0:
            
            #Se a diferenca for maior que 0, clarisse ira para a esquerda
            #Assim, ate a distancia se torne igual a 0
            if diferenca_clarisse_percy_x > 0:
                clarisse_x -= 1

            #Se nao, ira para a direita
            else:
                clarisse_x += 1

        #Se estiver no mesmo x que Percy
        else:

            #Verifica se nao esta no mesmo y que Percy
            if diferenca_clarisse_percy_y != 0:
                #Verifica a diferenca entre suas distancias, se for positiva, vai para cima
                if diferenca_clarisse_percy_y > 0:
                    clarisse_y -= 1
                
                #Se for negativa, vai para baixo
                else:
                    clarisse_y += 1
            
            #Esta no mesmo Y e mesmo X que Percy, Logo Clarisse ganha o jogo
            else:
                jogo_acabou = True
                clarisse_venceu = True

        #Verifica se Clarisse esta na agua, se sim, o jogo acaba
        if clarisse_x == agua_x and clarisse_y == agua_y:
            jogo_acabou = True

        #Executa funcao que verifica se estao no mesmo lugar
        else:
            jogo_acabou,clarisse_venceu,diferenca_clarisse_percy_x,diferenca_clarisse_percy_y = clarisse_ganhou(clarisse_x,percy_x,clarisse_y,percy_y)

        #Apos o movimento de Clarisse, verifica se o jogo nao acabou
        #Se nao acabou, inicia o movimento de Percy
        if not jogo_acabou:

            #Recebe a direcao que percy se movera
            direcao = input()
            #Executa a funcao que retorna as novas coordenadas de Percy
            percy_x, percy_y = movendo_percy(direcao,percy_x,percy_y,agua_x,agua_y)

            #Executa funcao que verifica se estao no mesmo lugar
            jogo_acabou,clarisse_venceu,diferenca_clarisse_percy_x,diferenca_clarisse_percy_y = clarisse_ganhou(clarisse_x,percy_x,clarisse_y,percy_y)
            
            #Verifica se clarisse ou percy venceram, se sim, Imprimi as respectivas msgs de cada
            if clarisse_venceu:
                print('Ah não, Annabeth vai me matar...')
            
            elif jogo_acabou:
                print('Vitória!! Nunca subestime o cabeça de alga!')

            #Se o jogo nao acabou
            else:
                #Verifica se percy ja havia pego a bandeira e agora esta no y = 0
                #Se sim, percy ganha
                if pegou_bandeira and percy_y == 0:
                    jogo_acabou = True

                #Verifica se percy ja havia pego a bandeira anteriormente, mas ainda nao esta no y certo
                #Imprimi a msg que ainda precisa se mover
                elif pegou_bandeira:
                    print('Agora eu só preciso meter o pé daqui!')

                #Verifica se esta nas mesmas coordenadas da bandeira
                #Se sim, imprimi a msg que conseguiu pega-la
                elif percy_x == bandeira_x and percy_y == bandeira_y:
                    print('Isso! Consegui a bandeira!')
                    pegou_bandeira = True

                #Verifica se ainda nao pegou a bandeira
                if not pegou_bandeira:
                    print('Preciso pegar aquela maldita bandeira vermelha.')

                #Se pegou nesta rodada, verifica se ja esta no y = 0
                #Se sim ganha o jogo
                elif percy_y == 0:
                    jogo_acabou = True
                
                #Verifica se percy ganhou o jogo, apos pegar a bandeira
                if jogo_acabou:
                    print('Vitória!! Nunca subestime o cabeça de alga!')
            
        #Se o jogo acabou apos o movimento de clarisse
        #Se sim, verifica qual dos dois ganhou e imprimi as respectivas msgs  
        else:
            if clarisse_venceu:
                print('Ah não, Annabeth vai me matar...')
            
            else:
                print('Vitória!! Nunca subestime o cabeça de alga!')
        
        #No fim do loop, executa a funcao que imprimi a matriz
        printando_matriz(matriz_base,percy_x,percy_y,clarisse_x,clarisse_y)
        
        #Se o jogo nao acabou, quebra linha para o proximo print
        if not jogo_acabou:
            print()

#Executa a funcao principal
main()
