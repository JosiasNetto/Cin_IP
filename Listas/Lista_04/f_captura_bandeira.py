def posicao_inicial():
    matriz_base = [['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-']]

    percy_y = int(input())
    percy_x = int(input())

    matriz_base[percy_y][percy_x] = 'P'

    clarisse_y = int(input())
    clarisse_x = int(input())

    matriz_base[clarisse_y][clarisse_x] = 'C'

    agua_y = int(input())
    agua_x = int(input())

    matriz_base[agua_y][agua_x] = 'A'    

    bandeira_y = int(input())
    bandeira_x = int(input())

    matriz_base[bandeira_y][bandeira_x] = 'B'

    
    #Fazer calculo de onde ir pela diferença
    #usar as cordenadas ja dadas para basear movimentação
    #Decobir quantas funções vai usar


