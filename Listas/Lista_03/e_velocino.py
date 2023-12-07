#Variaveis para funcionamento do codigo
informacoes_deuses = [
    ['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'],
    [100, 90, 80, 70, 60],
    ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']
]
deus_genero = ''
contador = 0
#Recebendo Sequencia do percy
sequencia = input()

#Loop que passa por cada numero que representa cada Deus
for num_deus in sequencia:
    
    #Loop que passa por todos os elementos da lista de Deuses na lista de informações
    for j in range(len(informacoes_deuses[0])):
        
        #Se o numero do deus da sequencia, for igual ao indice seu indice na lista dos deuses, rodara o codigo
        if  int(num_deus) == j:
            #Se for Atenas ou Afrodite, trocara a variavel que se refere ao genero do Deus
            if int(num_deus) == 2 or int(num_deus) == 4:
                deus_genero = "sa"
            else:
                deus_genero = "s"
            
            #Imprimindo as informações do Deus, dependendo do seu genero, e de qual Deus é
            print(f'Deu{deus_genero}:{informacoes_deuses[0][j]}')
            print(f'Poder:{informacoes_deuses[1][j]}')
            print(f'Artefato:{informacoes_deuses[2][j]}')
            contador += 1

            #Verificando se não é a ultima repetição do loop, para quebrar a linha
            if contador != len(sequencia):
                print()