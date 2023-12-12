#Variaveis globais para o codigo
equipamentos_disponiveis = ['Foice de Hades', 'Talismã de Ícaro', 'Elmo da Invisibilidade', 'Cinto de Hermes', 'Espada Anaklusmos', 'Escudo Aegis', 'Adaga Katoptris']
meio_sangue_e_nao_equipamento = []
equipamento_batalha = []

#Rcebendo input do nome equipamento que o meio sangue não deseja usar
nome_e_equipamento = input()

#Loop que recebe cada input ate parar
while nome_e_equipamento != 'Parar':
    
    #Tranformando o nome e os equipamento em uma lista
    nome_e_equipamento = nome_e_equipamento.split('-')
    equipamento_batalha = equipamentos_disponiveis.copy()
    
    #Loop que passa por cada elemento da lista do input 
    for i in range(len(nome_e_equipamento)):

        #Verifica se o equipamento da lista que o percy nao quer, esta na lista dos equipamentos disponiveis
        if nome_e_equipamento[i] in equipamentos_disponiveis:
            
            #Remove o equipamento da lista da batalha
            #List essa que é copia da lista de equipamento disponiveis
            equipamento_batalha.remove(nome_e_equipamento[i])

    #Verificando quantos equipamentos eles tem para a batalha
    ##Imprimindo-os dependendo da quantidade
    if len(equipamento_batalha) == 0:
        print(f'{nome_e_equipamento[0]} irá batalhar na base do murro!') 
   
    elif len(equipamento_batalha) == 1:
        print(f'{nome_e_equipamento[0]} irá rumo a batalha com o equipamento: {equipamento_batalha[0]}!')
   
    elif len(equipamento_batalha) > 1:
        print(f'{nome_e_equipamento[0]} irá rumo a batalha com os seguintes equipamentos:',end='')

        #Loop que passa pela quantidade de equipamentos, e printa cada um por vez
        ##Verifica se é o penultimo ou ultimo, e muda o print dependendo disso
        for equipamento in range(len(equipamento_batalha)):
            if equipamento < (len(equipamento_batalha) - 2):
                print(f' {equipamento_batalha[equipamento]},',end='')
            elif equipamento == (len(equipamento_batalha)- 2):
                print(f' {equipamento_batalha[equipamento]}',end='')
            elif equipamento == (len(equipamento_batalha) - 1):
                print(f' e {equipamento_batalha[equipamento]}!',end='')
        print()
    
    #Recebendo novamente do Loop
    nome_e_equipamento = input()
